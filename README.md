# Sharp logarithmic coupling estimates for theta equality frames

**In a signed Weil-form realization · Leonard van Hemert · Mathematical preprint · Version 1.0.0 · 11 October 2026**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23298499.svg)](https://doi.org/10.5281/zenodo.23298499)

[Read the paper](paper/coupling-estimates.pdf) · [Version 1.0.0 release](https://github.com/LeonardSEO/theta-coupling-estimates/releases/tag/v1.0.0) · [LaTeX source](paper/coupling-estimates.tex) · [Citation metadata](CITATION.cff)

We prove the sharp size of the finite-frame Schur correction for the first $m$ pole-killing odd derivatives of the actual Riemann theta kernel. For every fixed $m\ge1$,

$$
\lVert E_{m,\beta}\rVert\asymp_m
\beta\bigl(\log(1/\beta)\bigr)^{4m+5/2}
\qquad (\beta\downarrow0).
$$

The two-sided order has explicitly defined positive constants and a specified full parameter interval. For the first jet, the exponent is **13/2**. The result quantifies an exact coupling cost in the complete signed Weil form.

**RH status: unresolved.** The theorem is unconditional for each fixed frame. The sign of the remaining complementary form is an independent open obligation.

## Principal results

| Result | Exact scope |
| --- | --- |
| **Sharp coupling rate** | Theorem 1.1 gives matching upper and lower bounds $a_m\beta L^{4m+5/2}\le\lVert E_{m,\beta}\rVert\le A_m\beta L^{4m+5/2}$ for $L=\log(1/\beta)$ and every $0<\beta\le e^{-\ell_m}$. Constants and thresholds depend on the fixed $m$. |
| **Constructive charge cancellation** | Lemma 3.1 cancels both half-line source charges, proves actual membership in $\mathrm{Ran}(G^{1/2})$ and controls the entire integrated theta-tail error. Proposition 3.2 gives the full-symbol resolvent upper rate. |
| **Matching actual theta lower bound** | Lemma 4.1 and Proposition 4.2 use finite derivative polynomials, the complete theta lattice and odd box tests. No simplicity or location assumption on zeta zeros is used. |
| **Low-energy spectral mass** | Theorem 1.1 gives a pointwise upper bound for $\lVert U^*\mathbf{1}_{(0,t]}(G)U\rVert$. A matching pointwise lower bound is not asserted. |
| **Exact signed Schur reduction** | Lemma 5.1 and Proposition 5.2 retain the prime-shift operator, all prime powers and both pole terms, and identify the exact finite correction. |
| **Exact change of metric** | Proposition 7.1 eliminates the known equality space before gamma normalization. The correction cancels exactly, while the same logarithmic growth appears in $\lVert V_\beta\rVert^2-1$. The remaining signed form is unchanged by congruence. |

All definitions, domain arguments, constants and proofs are in the standalone **14-page manuscript**. The conclusion states the limits: no common constants for growing frames, no complementary-form sign and no unconditional positivity theorem for all Li coefficients.

## Read and download

The tagged release contains:

- `theta-coupling-estimates-v1.0.0-paper.pdf` — compiled manuscript;
- `theta-coupling-estimates-v1.0.0-latex-source.tar.gz` — standalone LaTeX source and rights notice;
- `theta-coupling-estimates-v1.0.0-source.tar.gz` — complete publication source package;
- `SHA256SUMS` — checksums of the three release assets.

**Version 1.0.0 DOI:** [10.5281/zenodo.23298499](https://doi.org/10.5281/zenodo.23298499). The [published Zenodo record](https://zenodo.org/records/23298499) preserves the complete tagged repository, including the PDF and LaTeX source. The [all-versions DOI](https://doi.org/10.5281/zenodo.23298498) identifies this publication across future versions.

The Zenodo ZIP was downloaded and checked byte for byte against all 12 files at the release commit. The tag and release assets are frozen. This default branch adds the issued DOI and archive verification in a separate documentation commit; reproduce the original release from `v1.0.0`.

The results are analytic. No numerical certificate is used in their proofs, so the release contains no unrelated numerical experiments or exploratory research records.

## Repository contents

```text
paper/                   Standalone English manuscript and compiled PDF
scripts/                 Deterministic release packaging
CITATION.cff             Machine-readable preferred preprint citation
.zenodo.json             Zenodo preprint metadata
REPRODUCIBILITY.md        Compilation, versions and integrity checks
PROVENANCE.md            Source fingerprints and verification scope
RELEASE_NOTES.md         Version 1.0.0 release description
SHA256SUMS               Checksums of the publication files
NOTICE                   Copyright and rights
```

## Reproduce the release

Use the `v1.0.0` tag for an exact archived-source comparison. Check the publication file bytes with:

```sh
shasum -a 256 -c SHA256SUMS
```

Compile with an existing Tectonic installation:

```sh
cd paper
tectonic coupling-estimates.tex
```

Rebuild the deterministic archives with Python's standard library:

```sh
python3 scripts/build_release_artifacts.py
```

A successful compile or matching hash establishes document or artifact integrity; the mathematical arguments are in the paper. Compiler timestamps can make a newly generated PDF differ bytewise from the frozen PDF.

## Proof, review and originality

The fixed-frame rate, full signed equality transfer and exact metric transformation received separate internal mathematical reconstruction. A lower-order theta expansion was corrected before this release by retaining the exact cosh factor; the sharp exponent and sign thresholds are preserved. See [PROVENANCE.md](PROVENANCE.md) for the precise control scope.

Manuscript development and targeted reconstruction were AI-assisted. Leonard van Hemert is the human author responsible for the publication. No external endorsement, journal acceptance or proof-assistant formalization is claimed.

A focused primary-source comparison examined the related Weil, model-space, Schur and logarithmic-operator settings. Scientific priority has not been established. The paper credits standard spectral and Schur tools and identifies the particular theta-weighted estimate it proves.

## Primary context

The manuscript gives exact application conditions and versioned references, including:

- [Bombieri and Lagarias, *Complements to Li's criterion for the Riemann hypothesis* (1999), author manuscript](https://websites.umich.edu/~lagarias/doc/bombieri.pdf)
- [Romik, *Orthogonal polynomial expansions for the Riemann xi function*, arXiv:1902.06330v3](https://arxiv.org/abs/1902.06330v3)
- [Suzuki, *Li coefficients as norms of functions in a model space*, arXiv:2301.05779v2](https://arxiv.org/abs/2301.05779v2)
- [Suzuki, *Aspects of the screw function corresponding to the Riemann zeta function*, arXiv:2206.03682v4](https://arxiv.org/abs/2206.03682v4)
- [Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3](https://arxiv.org/abs/2606.09096v3)
- [Kim et al., *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator*, arXiv:2607.24830v3](https://arxiv.org/abs/2607.24830v3)
- [Dusson, Sigal and Stamm, *The Feshbach–Schur map and perturbation theory*, arXiv:2105.02058v1](https://arxiv.org/abs/2105.02058v1)

The author's broader [xi zero-detection preprint, version 1.0.0](https://doi.org/10.5281/zenodo.23295277) has a different scope. The present focused paper supplies its own complete proofs.

## Citation and rights

Use [CITATION.cff](CITATION.cff), which identifies the mathematical preprint as the preferred citation, or:

```bibtex
@misc{vanhemert2026thetacoupling,
  author    = {van Hemert, Leonard},
  title     = {Sharp logarithmic coupling estimates for theta equality frames
               in a signed Weil-form realization},
  year      = {2026},
  publisher = {Zenodo},
  version   = {1.0.0},
  doi       = {10.5281/zenodo.23298499},
  url       = {https://doi.org/10.5281/zenodo.23298499},
  note      = {Mathematical preprint}
}
```

Copyright © 2026 Leonard van Hemert. All rights reserved; see [NOTICE](NOTICE). Public access to the paper and source does not grant a new open-content license.
