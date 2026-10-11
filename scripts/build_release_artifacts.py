#!/usr/bin/env python3
"""Build deterministic release archives and the repository SHA-256 manifest."""

from __future__ import annotations

import gzip
import hashlib
import io
from pathlib import Path
import shutil
import tarfile


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = "v1.0.0"
PREFIX = f"theta-coupling-estimates-{VERSION}"
PDF_ASSET = DIST / f"{PREFIX}-paper.pdf"


def regular_files(paths: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for path in paths:
        if path.is_file():
            files.add(path)
        elif path.is_dir():
            files.update(
                item
                for item in path.rglob("*")
                if item.is_file()
                and "__pycache__" not in item.parts
                and item.suffix not in {".pyc", ".pyo"}
                and item.name != ".DS_Store"
            )
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def archive(name: str, files: list[Path]) -> Path:
    destination = DIST / name
    tar_buffer = io.BytesIO()
    with tarfile.open(fileobj=tar_buffer, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for path in files:
            relative = path.relative_to(ROOT)
            data = path.read_bytes()
            info = tarfile.TarInfo(name=f"{PREFIX}/{relative.as_posix()}")
            info.size = len(data)
            info.mtime = 0
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            info.mode = 0o755 if path.suffix == ".py" else 0o644
            tar.addfile(info, io.BytesIO(data))
    with tarfile.open(fileobj=io.BytesIO(tar_buffer.getvalue()), mode="r:") as check:
        expected = {f"{PREFIX}/{p.relative_to(ROOT).as_posix()}": p.read_bytes() for p in files}
        assert set(check.getnames()) == set(expected)
        for member in check.getmembers():
            assert member.isfile() and member.mtime == 0
            assert check.extractfile(member).read() == expected[member.name]
    with destination.open("wb") as handle:
        with gzip.GzipFile(
            filename="", mode="wb", fileobj=handle, mtime=0, compresslevel=9
        ) as compressed:
            compressed.write(tar_buffer.getvalue())
    return destination


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    paper_pdf = ROOT / "paper" / "coupling-estimates.pdf"
    if not paper_pdf.is_file():
        raise SystemExit("paper/coupling-estimates.pdf is missing")
    source_files = regular_files([
        ROOT / name for name in (
            "README.md", "RELEASE_NOTES.md", "CITATION.cff", ".zenodo.json",
            ".gitignore", "NOTICE", "REPRODUCIBILITY.md",
            "PROVENANCE.md", "paper", "scripts",
        )
    ])
    (ROOT / "SHA256SUMS").write_text("\n".join(
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in source_files
    ) + "\n", encoding="utf-8")
    shutil.copyfile(paper_pdf, PDF_ASSET)
    release_assets = [
        PDF_ASSET,
        archive(f"{PREFIX}-latex-source.tar.gz", regular_files([
            ROOT / "paper" / "coupling-estimates.tex", ROOT / "NOTICE",
        ])),
        archive(f"{PREFIX}-source.tar.gz", sorted(
            source_files + [ROOT / "SHA256SUMS"],
            key=lambda path: path.relative_to(ROOT).as_posix(),
        )),
    ]
    (DIST / "SHA256SUMS").write_text("\n".join(
        f"{sha256(path)}  {path.name}" for path in release_assets
    ) + "\n", encoding="utf-8")
    for path in release_assets:
        print(f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
