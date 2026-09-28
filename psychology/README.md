# Psychology and prior-work preservation

Nolan requested a substantial psychology section and import of the existing mathematics/psychology Lean corpus. That work must be carried forward with its original proofs, documents, toolchain, and provenance. A new elementary sociology example is not a substitute.

## Current evidence

At 27 September 2026 Pacific time, the accessible GitHub repository `Sodelin/Mathematics-of-Psychology-Formalized` has a minimal main README and this session's `research/solidarity-at-scale-2026-09-27` proof branch. Its branch listing and all-state pull-request listing did not expose the larger corpus. Relevant file and continuity searches did not locate an archive or original theorem inventory. The user reports that the corpus exists; its location remains unresolved. This does not imply the work never existed.

No existing branch was reset, force-pushed, or deleted. The original checkout is retained. Until original files are available, the import is **pending**, and no replacement proof inventory will be invented.

## Psychology content available now

The substantial psychology section in [What Lean proves](../projects/solidarity-at-scale/formal/what-lean-proves.md) distinguishes familiarity, symbol recognition, beliefs, preferences, identity structure, and behavior. It explains exactly what the available formal results do and do not establish, and proposes future targets without presenting them as implemented. The guide is available as a [PDF](../projects/solidarity-at-scale/outputs/what-lean-proves.pdf) and [DOCX](../projects/solidarity-at-scale/outputs/what-lean-proves.docx).

The [paper](../projects/solidarity-at-scale/paper/manuscript.md) discusses relational familiarity, cultural-marker learning, identity complexity, and cooperation. Its source register identifies the access depth and limitations of each psychological source. The [proposed study](../projects/solidarity-at-scale/protocol/empirical-study.md) separates these constructs in a possible experiment.

The [current Lean specification](../projects/solidarity-at-scale/formal/specification.md) concerns relationships among formal variables. It does not verify the relational-self theory, estimate a cognitive relationship limit, or establish an empirical effect of identity on behavior. Those claims need observations and a justified connection between the formal variables and psychological measures.

## Import procedure

Obtain the original repository URL and commit, a git bundle, or a project archive including its Lean sources and configuration. Inventory and hash it in an isolated directory. Preserve an unchanged snapshot and import provenance; keep the original repository intact. Reproduce its existing build before any readability or toolchain changes. Map every theorem to its informal meaning, assumptions, source, and check status. Only then reorganize presentation or combine modules. Readability edits must preserve theorem statements and pass the original checks; mathematical changes require explicit explanation.

The next required input is the location or an archive of that original corpus. The import remains incomplete until source-to-import hashes and the original proof inventory can be compared.
