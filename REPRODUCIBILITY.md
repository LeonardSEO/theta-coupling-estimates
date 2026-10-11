# Reproducibility

Use the `v1.0.0` tag or the version-specific Zenodo archive for this frozen publication. The default branch may contain a later DOI citation update.

## Manuscript build

The standalone source is `paper/coupling-estimates.tex`; its bibliography is embedded and no additional project files are required. The frozen PDF was generated with **Tectonic 0.17.0**. Standard packages used by the article are supplied by the compiler's TeX bundle.

```sh
cd paper
tectonic coupling-estimates.tex
```

The source was also checked successfully with the Codex desktop document compiler. The final PDF has 14 pages. Its author, theorem scope, bibliography and cross-references were inspected; no unresolved reference markers or overfull boxes remain in the export build. Representative title, lower-proof and bibliography pages were inspected visually. PDF creation metadata can prevent a fresh compiler run from producing the same binary hash.

## File and release integrity

```sh
shasum -a 256 -c SHA256SUMS
python3 scripts/build_release_artifacts.py
(cd dist && shasum -a 256 -c SHA256SUMS)
```

The release builder uses only Python's standard library. It sorts file paths, fixes tar ownership, modes and timestamps, fixes the gzip timestamp, and checks each archived member's name and bytes against its input before writing the archive. The PDF asset is copied from the frozen publication PDF. No dependency installation is needed for packaging.

## Mathematical reproduction

The analytic proofs are entirely in the article. The effective constants consist of finite derivative polynomials, convergent theta integrals and positive finite matrices; the stated positivity is proved analytically. No numerical approximation, zero-height verification or external certificate supplies a premise to the main theorem.

The proof checks and artifact checks have different scope. Compilation, file hashing and archive reconstruction do not verify a mathematical theorem or establish scientific originality. No machine formalization or external peer review is claimed.
