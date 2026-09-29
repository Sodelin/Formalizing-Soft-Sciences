# Complete publication and source-question map

As of 29 September 2026, this repository preserves **85 checked theorem declarations**: 16 in the original solidarity module, 51 in Foundations I, and 18 in the published-CBT fragment. Supporting lemmas and source bridges are included in those counts. The 67-item package was already on main; the clinical checkpoint was integrated through PR 2 at `4501e21c6b887e376c5adf145aff3f78afea9dbd`.

## What the work accomplishes

The connected theme is inference: what follows from a representation, which observations distinguish competing explanations, and which conclusions need additional assumptions. The foundations give explicit, checked examples across six areas. The clinical extension grounds that approach in tables from an existing published computational model.

| Family | Exact answered question | Source and status |
|---|---|---|
| Solidarity, 16 declarations | Can bounded contact degree coexist with unbounded reach, overlapping membership, and independent trust? When is contribution stable in the specified donation game? | [Original question and theorem guide](projects/solidarity-at-scale/formal/what-lean-proves.md). Project-specified elementary graph, set, and incentive consequences. |
| Identification | Can a sum distinguish its two components, and do two specified probes restore recovery? | [B01](projects/foundations/open-problems.md), [Lean](SocialScience/Identifiability.lean). Established identification reasoning; F02 provides model-recovery motivation. |
| Measurement | What latent-difference interval follows from a bounded differential intercept bias, and when is its sign fixed? | [B02 and source context](projects/foundations/open-problems.md), [Lean](SocialScience/Measurement.lean). Additive sensitivity model; F03 motivates measurement comparability. |
| Causality | Can identical observational functions coexist with different effects? | [B03](projects/foundations/open-problems.md), [Lean](SocialScience/Causality.lean). Standard binary non-identification construction. F04/F05 are richer network predecessors, not problems solved here. |
| Learning | When does a correctly labeled discriminating probe eliminate a rival, and how can a wrong label exclude truth? | [B04](projects/foundations/open-problems.md), [Lean](SocialScience/Learning.lean). Established version-space reasoning; F08 is the predecessor. |
| Collective action | When can a two-person budget satisfy both participation constraints under unrestricted transfers? | [B05](projects/foundations/open-problems.md), [Lean](SocialScience/CollectiveAction.lean). Elementary allocation feasibility; existence alone is not a bargaining mechanism. |
| Aggregation | Can valid pooled counts reverse both within-context comparisons? | [B06](projects/foundations/open-problems.md), [Lean](SocialScience/Aggregation.lean). Checked synthetic witness of the established Simpson phenomenon; F09 is the historical source. |
| Published CBT fragment, 18 declarations | Which of two specified action paths distinguishes the safe/dangerous latent state, and do the transcribed weight columns have the stated mass, bounds and equality conditions? | [Clinical source map below](#clinical-source-map), [Lean](clinical/ClinicalModels/PublishedCBT.lean), [source bridge](clinical/ClinicalModels/SourceBridge.lean). Source-based fragment verification; no author-designated open conjecture is established as solved. |

All 51 foundations declarations have individual explanations in the [theorem guide](projects/foundations/theorem-guide.md) and [machine-readable inventory](projects/foundations/theorem-inventory.csv). The [source register](projects/foundations/sources/references.md) records exact papers and access depth. The broader research questions and historical leads remain explicitly distinguished in the [problem register](projects/foundations/open-problems.md).

## Clinical source map

Ryan Smith, Michael Moutoussis and Edda Bilek (2021), *Simulating the computational mechanisms of cognitive and behavioral psychotherapeutic interventions: insights from active inference*, Scientific Reports 11, 10128. [Published paper](https://doi.org/10.1038/s41598-021-89047-0). The upstream [MATLAB source](https://github.com/rssmith33/Simulating_Cognitive_Behavioral_Therapy/blob/82a0a3d75b0bdc08d2b78cdf2201d7aa626c27a3/CBT_model.m) is pinned at commit `82a0a3d75b0bdc08d2b78cdf2201d7aa626c27a3`, SHA-256 `faba14894224ccf1a20594d390a5f7e3a74eed665205fa24285ddfa1d36513e5`.

The exact result is informative: every classifier restricted to the specified avoidance observation trajectory must fail on at least one of the two states, whereas the specified approach trajectory identifies the state among those two possibilities. This exposes how an action changes information in this model. The theorem checks all four declared observation modalities. It is a statement about the deterministic four-time-point fragment and its exact tables, rather than a treatment recommendation or an empirical efficacy result.

The 18 declarations comprise 14 trajectory, observation and weight results plus four source-bridge results. The weight results include total mass, nonnegativity under explicit bounds, equality of implicit mappings at CABi = 0.1, its approach-column converse, and the prior-weight identity. The extractor checks ten matrices and six selected assignments against the pinned upstream bytes. This is a bounded transcription check, not a proof of MATLAB/SPM semantics or a reproduction of the complete simulation.

## Verification and publication

- [Foundations source receipt](projects/foundations/verification-manifest.json): all 67 declarations, source hashes, explanations and axiom audit.
- [Successful clinical checkpoint run](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36408149787): all foundations and original-document checks, ten upstream matrices and six assignments, clinical build and all 18 axiom reports.
- [Original solidarity manuscript](projects/solidarity-at-scale/paper/manuscript.md) and [decision report](projects/solidarity-at-scale/report/research-report.md), with their preserved PDFs and editable documents.

No field-level open-problem closure or new empirical psychological law is established by these counts. The useful publication claim is a reproducible formalization and source-fragment audit, with precise examples and explanatory documentation. Candidate further research stays in the problem register rather than being relabeled as completed discovery. Public GitHub availability, editorial submission, acceptance and independent peer review are separate statuses.

The 16-declaration psychology repository is an earlier preserved copy, not 16 additional results beyond these 85. A distinct, still earlier psychology corpus mentioned in the historical README remains a separate recovery question; the remembered 67-item package itself is now located and accounted for.
