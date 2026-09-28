# Formalizing Soft Sciences

Research in psychology and the social sciences, with readable explanations, source evidence, and precisely scoped Lean proofs.

## Read the current work

- **[Start here: what Lean proves](projects/solidarity-at-scale/formal/what-lean-proves.md)** — All 16 proofs explained, the psychology section, what is established prior work, and how Durkheim could guide the next model. [Guide PDF](projects/solidarity-at-scale/outputs/what-lean-proves.pdf) · [editable DOCX](projects/solidarity-at-scale/outputs/what-lean-proves.docx).
- **[Solidarity at scale: paper](projects/solidarity-at-scale/paper/manuscript.md)** — How can cooperation extend beyond people we know? Identity, cultural signs, material interests, institutions, and political coalitions.
- **[Evidence and political decision report](projects/solidarity-at-scale/report/research-report.md)** — Start with its executive brief. The recommendation is conditional on equal rights, non-domination, and broadly shared gains.
- **[Paper PDF](projects/solidarity-at-scale/outputs/solidarity-at-scale-paper.pdf)** and **[report PDF](projects/solidarity-at-scale/outputs/solidarity-at-scale-report.pdf)** — Readable downloads with references; editable DOCX versions are in the same folder.
- **[Lean proofs and their meaning](projects/solidarity-at-scale/formal/specification.md)** — What the current 16 theorems establish and where their assumptions stop.
- **[Psychology section and import status](psychology/README.md)** — Preserving the prior mathematics-of-psychology project is an explicit requirement.
- **[Full project index](projects/solidarity-at-scale/README.md)** — 35 sources, 24 typed claims, historical comparisons, proposed studies, bibliography, and staged notes.

## What is established so far

The current Lean source builds successfully with Lean 4.19.0. It shows that limited direct contacts can coexist with unbounded indirect reach, that group memberships can nest or overlap, and that cooperation in a specified two-person game depends on an explicit incentive threshold. These are elementary formal results, not new empirical laws of psychology or a proof that one political ideology is correct.

The research documents are an initial targeted synthesis, not a completed systematic review or peer-reviewed publication. Sources distinguish full readings from abstracts and reading leads. The complete political recommendation has not been tested as one intervention.

## Preservation and publication status

This repository is the requested home for work extending beyond psychology. The current research package was carried forward from this session's working copy. The larger pre-existing psychology corpus described by Nolan has **not yet been located or imported**; the current 16 theorems must not be presented as its replacement. Existing source repositories and branches remain intact.

The published package and plain-language guide are on main for reading and discussion. The [publication record](projects/solidarity-at-scale/publication/README.md) distinguishes public files, the prepared share note, and future review or archival steps. GitHub availability is not journal publication or peer review.

## Reproduce the formal checks

With the pinned toolchain installed, run `lake build` and then `lake env lean Solidarity.lean` from this repository's root. The [verification receipt](projects/solidarity-at-scale/formal/verification-report.md) records successful runs both in the original working repository and here on main.
