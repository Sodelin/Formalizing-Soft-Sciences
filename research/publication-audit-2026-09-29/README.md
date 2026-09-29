# What observations justify: a complete formalization and source audit

**The contribution is an inspectable chain from a scientific question to explicit assumptions, a checked mathematical consequence, and a precise source connection.** This package accounts for every one of the 85 theorem declarations currently preserved in the project: 16 solidarity results, 51 foundations results, and 18 results about a published computational model. It makes the strongest contributions easy to find while retaining the supporting proofs that make them trustworthy.

The central question is practical: when do observations distinguish competing explanations, and what extra information restores that distinction? The package answers exact versions of this question across measurement, causal inference, learning and aggregation, alongside models of network reach and cooperation.

## Results worth leading with

| Contribution | Exact useful outcome | Mathematical status |
|---|---|---|
| Observation design | A sum leaves two components ambiguous; adding a specified component probe restores exact recovery. Postprocessing cannot recover a distinction already erased. | Established identification reasoning, with explicit checked examples. |
| Bias-sensitive measurement | A supplied bound on differential intercept bias becomes a precise interval for the latent difference; a sufficiently large observed gap determines its sign. | Exact consequences of the specified additive model. |
| Causal ambiguity | Two models agree on every permitted observational input but have different intervention effects, so no estimator using that input alone works for both. | Checked standard non-identification construction. |
| Evidence and learning | A discriminating correctly labeled query eliminates a rival; a wrong exact label can eliminate the truth; duplicated constraints add no information. | Established version-space reasoning, formalized transparently. |
| Allocation and cooperation | An acceptable two-person transfer exists iff the budget covers total costs; positive aggregate surplus alone need not make the offered allocation acceptable. | Exact feasibility threshold and witness under the declared payoff/capability assumptions. |
| Aggregation | Valid counts favor one group in both strata and favor the other after pooling. Two declarations explicitly reuse earlier information-loss results. | Synthetic witness of an established phenomenon, with reuse visible. |
| Published-model verification | For the declared four-step observation fragment, avoidance gives the same complete observation record in both states, defeating every deterministic classifier of that record; approach distinguishes the two states. | Source-specific verification of an already discussed mechanism, with a checked transcription bridge. |

The engineering work has a concrete purpose: keeping the informal interpretation, exact declaration, proof dependencies, source tables and verification receipts aligned. That alignment is the feature to present prominently. A large declaration count is useful for coverage, but is not evidence of an equal number of discoveries.

The parallel document-recovery chat has also preserved the [17-page article, 77-page monograph and their PDF/EPUB editions](../../ASTRA-HANDOFF.md). Those books explain the 67-declaration core release; they add explanatory and production artifacts rather than new theorem declarations. This audit covers the complete current 85-declaration corpus, including the clinical extension that is outside those historical editions.

## The theorem-by-theorem judgment

[Every declaration is explained and linked here](THEOREM-BY-THEOREM.md). The [CSV](theorem-audit.csv) and [JSON](theorem-audit.json) additionally record formal signatures, assumptions, within-package roles, source-question connections, immutable line anchors and SHA-256 hashes. They distinguish endpoints, witnesses, supporting lemmas, consequences, reused results and integrity checks. No declaration is discarded for being supporting work.

The audit establishes **zero verified closures of externally posed field-level open problems** in this 85-declaration package. The six B01-B06 questions in the existing register are precise project questions answered by established mathematics in a specified representation. The broader scientific issues that motivate them remain separate research questions. In particular, the social-network example does not resolve general homophily/contagion identification, and the measurement examples do not supply empirical construct validity.

For the clinical extension, fresh full-text reading confirmed that Smith, Moutoussis and Bilek already explain how avoidance prevents informative observations. The additional contribution here is exact verification of the selected observation/weight fragment and its connection to pinned code. The paper's extensions involving uncertainty, attention and learning dynamics remain outside these proofs. [Source comparison and access record](SOURCES.md).

## Publication route and language

Suggested package title: **What observations justify: 85 checked declarations connecting social-science models, information loss and source verification.**

Suggested description: *This reproducible Lean development makes inferential assumptions explicit and connects every declaration to a readable explanation. It checks exact conditions for identification, bias-sensitive ordering, evidence consistency, task participation and aggregation, then verifies an observation fragment against a published computational model's source tables. Complete theorem inventories and source receipts allow reviewers to inspect both the deductions and their interpretation.*

This is a suitable public formalization, reproducibility and educational dossier. VibeMathed's current catalog rules distinguish new answers to open questions from formalizations of established results. The package has been shared as supporting context; it is not presented as 85 new discovery submissions. A future catalog entry would need a qualifying additional mathematical advance and its source comparison. This routing preserves the work and directs attention to its demonstrated value.

## Verification and preservation

- Audited source snapshot: `7835157627548823f03f29dd3987e55601807b55`. The source inspection covered all nine files containing the 85 declarations, including four source-bridge declarations.
- The [foundations receipt](../../projects/foundations/verification-manifest.json) preserves the original 67-declaration build, source hashes and axiom inventory. The [main workflow](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36634412999) also checks the integrated clinical package.
- `python -X utf8 research/publication-audit-2026-09-29/build_inventory.py --check` verifies complete one-to-one declaration coverage and the reproducible audit outputs against the immutable Git snapshot. `python -X utf8 scripts/check_foundations.py` verifies the preserved foundations receipt and documentation.
- This publication pass changes explanatory artifacts, not Lean definitions or proofs. It is an AI-assisted audit; a human statement/novelty review remains a distinct form of evidence.
- The earlier 16-declaration psychology repository is a preserved copy of the solidarity component, not 16 additional results. The remembered 67-item package is accounted for. Any distinct older corpus still requires recovery before its content or size can be asserted.

Source reading is a bounded update of the existing comparison, not an exhaustive priority review. Its retrieved versions, failed routes and remaining access limits are recorded in [the evidence ledger](evidence-ledger.json).
