# Proof-of-Control: arXiv Preprint

LaTeX source for *Proof-of-Control: An Open Standard for Runtime Verifiability and
Cryptographic Oversight in Autonomous AI Execution*.

**Status: working draft for co-author review — not yet submitted.**

**Prose style.** The paper is written in the plain, concrete, direct register associated with
Richard Feynman's expository writing: examples before abstractions, ordinary words for technical
things, and explicit statements of what is *not* known or claimed. All technical content —
theorems, proofs, tables, measurements, citations — is unchanged; only the prose register
differs. Section titles are plain declaratives ("The Problem", "Does It Actually Work?",
"What We Still Don't Know").

The measured results in Section 9 come from the reference implementation in
[`../impl/`](../impl/README.md); regenerate them with `python3 bench/bench.py` and
`python3 attacks/run_attacks.py` from that directory.

## Build

```bash
tectonic -Z shell-escape main.tex   # shell-escape needed for minted (pygments)
```

Output: `main.pdf` (a compiled copy is committed for convenience).

## Before Submission — Required Steps

1. **Co-author consent.** The author list mirrors the Advanced AI Society leadership, board,
   and advisory board as published at [advancedaisociety.org/about](https://advancedaisociety.org/about),
   with Jim Schwoebel as first author. Every listed individual must review the draft and
   consent to authorship; remove anyone who does not. The title-page footnote states this.
2. **Citation verification.** Entries in `references.bib` marked `[verify]` (Bandara et al.
   AI Trust OS, Chen et al. TraceSafe-Bench, Xie et al. SCR-Bench, Web 7.0 Verifiable Trust
   Circles, Catena-X AI Service KIT, MindXO KRI, and the arXiv:2603.16586 author list) carry
   metadata reported in secondary sources — confirm against the primary literature and fill
   in full author lists, venues, and identifiers.
3. **Numbers refresh.** The requirement count (111), threat count (32), and coverage table
   are generated from the specification repository. Re-run
   `python3 mappings/compute_coverage.py` and `python3 tools/generate_checklist.py` and update
   Section 7 / the abstract if the working group changes the requirement set.
4. **arXiv metadata.** Suggested categories: cs.CR (primary), cs.AI, cs.SE. License: CC BY 4.0
   to match the specification.

## Files

| File | Purpose |
| --- | --- |
| `main.tex` | The paper (compiles with tectonic, XeTeX engine) |
| `references.bib` | Complete bibliography: RFCs, NIST/ISO/EU documents, frameworks, and the 2026 research corpus |
| `figures/aai-logo.png` | Advanced AI Society logo asset (reference; the cover mark is drawn in TikZ) |
| `figures/*.pdf` | Paper figures, converted from the repo's SVGs: `rsvg-convert -f pdf images/diagrams/<name>-light.svg -o paper/figures/<name>.pdf` |
| `main.pdf` | Compiled output |
