# Formalizing Soft Sciences

Research in psychology and the social sciences, with readable explanations, source evidence, and precisely scoped Lean proofs.

## Read the current work

- **[Start here: Foundations I](projects/foundations/README.md)** — 51 new checked theorem declarations covering measurement, identification, causality, learning, collective action, and aggregation. [Research report](projects/foundations/report.md) · [every new theorem explained](projects/foundations/theorem-guide.md) · [research problem register](projects/foundations/open-problems.md).
- **[What Lean proves: the original solidarity guide](projects/solidarity-at-scale/formal/what-lean-proves.md)** — The initial 16 proofs explained, the psychology section, established prior work, and the original Durkheim model proposal. [Guide PDF](projects/solidarity-at-scale/outputs/what-lean-proves.pdf) · [editable DOCX](projects/solidarity-at-scale/outputs/what-lean-proves.docx). These downloads document the initial development; the new foundations guide is linked above.
- **[Solidarity at scale: paper](projects/solidarity-at-scale/paper/manuscript.md)** — How can cooperation extend beyond people we know? Identity, cultural signs, material interests, institutions, and political coalitions.
- **[Evidence and political decision report](projects/solidarity-at-scale/report/research-report.md)** — Start with its executive brief. The recommendation is conditional on equal rights, non-domination, and broadly shared gains.
- **[Paper PDF](projects/solidarity-at-scale/outputs/solidarity-at-scale-paper.pdf)** and **[report PDF](projects/solidarity-at-scale/outputs/solidarity-at-scale-report.pdf)** — Readable downloads with references; editable DOCX versions are in the same folder.
- **[Original Lean specification](projects/solidarity-at-scale/formal/specification.md)** — What the original 16 theorems establish and where their assumptions stop.
- **[Psychology section and import status](psychology/README.md)** — Preserving the prior mathematics-of-psychology project is an explicit requirement.
- **[Full project index](projects/solidarity-at-scale/README.md)** — 35 sources, 24 typed claims, historical comparisons, proposed studies, bibliography, and staged notes.

## What is established so far

The project has **67 theorem declarations checked with Lean 4.19.0: 16 preserved and 51 new**. This count includes supporting lemmas and concrete examples. The original module distinguishes network reach, memberships, and incentives. The six new modules establish restricted results about measurement bias, observational ambiguity, discriminating evidence, complementary capabilities, acceptable allocations, and aggregation reversals. See the [foundations verification receipt](projects/foundations/verification.md).

These are elementary formal results and useful counterexamples, not new empirical laws or solutions to field-level open problems. The [research problem register](projects/foundations/open-problems.md) identifies precise next tasks and the evidence needed before claiming a broader scientific advance.

The research documents are an initial targeted synthesis, not a completed systematic review or peer-reviewed publication. Sources distinguish full readings from abstracts and reading leads. The complete political recommendation has not been tested as one intervention.

## Preservation and publication status

This repository is the requested home for work extending beyond psychology. The earlier research package is preserved and the foundations expansion adds separate modules. The larger pre-existing psychology corpus described by Nolan has **not yet been located or imported**; these new developments must not be presented as its replacement. Existing source repositories and branches remain intact.

The published package and plain-language guide are on main for reading and discussion. The [publication record](projects/solidarity-at-scale/publication/README.md) distinguishes public files, the prepared share note, and future review or archival steps. GitHub availability is not journal publication or peer review.

## Reproduce the formal checks

With the pinned toolchain installed, run `lake build` and `lake env lean SocialScience/Audit.lean` from this repository's root. The audit covers all 67 declarations. Run `python3 scripts/check_foundations.py` for source hashes, theorem-to-explanation coverage, and documentation checks. The [original verification receipt](projects/solidarity-at-scale/formal/verification-report.md) remains available for the initial package.
