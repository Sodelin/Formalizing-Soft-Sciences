# 10. References

The references are generated in alphabetical order in the finished manuscripts. The accompanying BibTeX and RIS files preserve the same source identities. The source register records access depth, and the relationship file explains how the sources contribute to the argument.

# 11. Metacognitive Review of the Evidence Process

## Process Integrity Assessment

The strongest part of this review is the direct alignment between the source, the theorem inventory, and the verification record. Every theorem-bearing file was inspected at a fixed commit, and the 67 declarations were matched to the audit. That creates a reproducible object of discussion: another reader can inspect the same statement, definition, and proof.

The literature review was designed as a targeted evidence map. It established precedents in the named fields and identified research relevant to the proposed AI applications. It used primary papers and official sources, with an explicit distinction between directly inspected full material and abstract-level access.

An author-defined checklist gives the process 8 out of 12 possible points: provenance 2/2; search reproducibility 1/2; selection rules 1/2; theorem-extraction fidelity 2/2; critical appraisal 1/2; independent reproducibility 1/2. The partial scores identify concrete improvements: a preregistered scope, specialist database searches, complete source access, independent extraction, and a separately reproduced build. The checklist is a descriptive self-assessment. AMSTAR 2 has a different purpose: appraisal of systematic reviews of healthcare interventions (Shea et al., 2017).

PRISMA 2020 supplies useful reporting questions about search procedures, selection, and synthesis (Page et al., 2021). For this targeted map, those questions support a recorded search log, explicit inclusion purposes, and per-source access information. A systematic extension would add a preregistered protocol and comprehensive database strategy.

Risk-of-bias tools should follow the object being appraised. RoB 2 addresses randomized trials (Sterne et al., 2019), while this source audit evaluates traceability, extraction fidelity, semantic interpretation, and reproducibility. A future evidence synthesis connecting a formal model to intervention studies would add the corresponding study-design appraisal.

## Biases That Matter for This Project

An enthusiasm for formal methods can favor questions that are easy to encode. That selection can produce a polished library while leaving the most important scientific ambiguity untouched. The remedy is to choose extensions by their effect on a real research decision and to invite domain review before investing heavily in proof engineering.

The opposite bias is to judge a minimal model only by the richness it omits. That misses the value of isolating a mechanism. A small model can establish a universal conditional result, expose an impossibility, or make a counterexample decisive. The appropriate assessment asks whether the chosen abstraction preserves the distinction the research needs.

The corpus also risks familiarity bias: elementary results can appear more novel when restated in a new application. The report therefore distinguishes implementation, interpretation, and mathematical discovery. The first two can be valuable contributions in their own right; a priority claim would require a dedicated comparison of statements and assumptions.

# 12. Metacognitive Reflection on Inference Robustness

## Robustness Verdict

The verdict has three levels. The source inventory and CI status have strong direct support. The model consequences are exact within their formal definitions and accepted logical foundations. The proposed benefits for empirical research and AI transfer are promising hypotheses with specified paths to evaluation.

This distinction allows strong claims where the evidence is strongest. Result 39 quantifies over all estimators of the specified input object, so its conclusion is not tied to the weakness of a particular algorithm. Result 24 applies across all integer inputs satisfying its premises. Result 34 identifies all pairs in the stated parameter space. Their generality is mathematical and explicit.

The library's scientific interpretation can be stress-tested by changing what the models contain. Add stochastic observations to the measurement and learning modules. Make identity affect payoffs rather than remain an independent label. Add capacity to task coverage. Change the information available to a causal estimator. Each modification creates a precise question about which earlier conclusions persist.

## Meta-Analytic Questions and Their Appropriate Role

There are no commensurable empirical effect sizes to pool in this audit. Fixed- versus random-effects models, Cochran's Q, tau-squared, I-squared, funnel plots, and Egger tests therefore have no numerical application to the 67 declarations. A theorem count is not a sample size, and dependent lemmas are not independent studies.

For a future AI-transfer experiment, the analysis should define the outcome before training. A proportion of unsupported claims, a paired accuracy difference, or a calibrated error score could be appropriate. Multiple scenario families would create structured heterogeneity. A hierarchical model or cluster-aware uncertainty procedure could reflect that design, while sensitivity analyses would examine family composition and evaluator judgments. These are protocol recommendations, not results of a completed analysis.

Publication bias would become relevant if multiple independent transfer studies existed and were synthesized. A funnel plot over related prompts from one training run would not answer that question. Similarly, an apparent subgroup advantage discovered after many comparisons should be treated as exploratory until replicated.

## What Would Change the Assessment

The argument for research utility would become stronger if an extension changed an experimental design, exposed a consequential error in a published derivation, or enabled an independently reproduced result. It would weaken if domain review showed that the formal variables routinely failed to preserve the distinctions needed by the intended applications.

The argument for AI transfer would strengthen with preregistered gains on held-out model families, fewer unsupported empirical claims, and independent semantic review. It would narrow if improvement appeared only on familiar syntax, duplicated theorem patterns, or easier test distributions. A rise in proof success accompanied by poorer interpretation would favor additional semantic training and evaluation rather than a broad success claim.

These counterfactuals make the project falsifiable at the level where practical benefits are proposed. The formal results remain inspectable while the use claims are tested.

# 13. Zotero and Obsidian Integration

The reading pack includes `references.ris` and `references.bib`. Import either file into a Zotero collection named “Formalizing Minds and Societies.” Use the other as an interchange backup rather than importing both into the same collection without deduplication.

Suggested tags distinguish the sources' roles: `formal-methods`, `mathematical-psychology`, `measurement`, `identifiability`, `computational-anthropology`, `social-choice`, `ai-training`, and `normative-reasoning`. An additional access tag, such as `access/abstract` or `access/selected-full-text`, preserves how deeply a source was inspected for this report.

The file `source-relations.csv` records conceptual relationships proposed by this synthesis. For example, model-identification literature motivates the probe-design chapter, and AI theorem-proving studies provide precedent for a training method. These links are interpretive relationships in this reading map, not claims that one original author cited another.

For Obsidian, place the Markdown folder in a vault and open `README.md`. Keep theorem notes linked to the inventory's pinned source URLs. A useful note template records the informal question, formal statement, model assumptions, proof role, empirical bridge, and next extension. A Better Notes workflow can attach those notes to the relevant Zotero item while retaining the source URL and citekey.

The files support independent import and reuse in a reference manager or Markdown knowledge base.

# 14. Appendices

## Appendix A — Verification and Source Map

The audited repository is [Sodelin/Formalizing-Soft-Sciences](https://github.com/Sodelin/Formalizing-Soft-Sciences), commit `780f1b83aef15a9cf455566bab9df2a47d738074`. Its main-commit verification run is [36392008029](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36392008029). The previously cited run 36391937036 belongs to commit a0663d5de45872ca4531067a886928f59ca48e61; both runs reported success.

The seven theorem-bearing modules contain 16, 9, 9, 6, 9, 10, and 8 declarations in the reading order used here. The audit module contains the 67 dependency-printing commands. The source index in the reading pack maps every atlas number to its exact theorem name, namespace, and source file.

To reproduce the project's checks in a checkout with the pinned Lean environment:

```sh
lake build
lake env lean SocialScience/Audit.lean
python3 scripts/check_foundations.py
python3 projects/solidarity-at-scale/scripts/validate_project.py --check-only
```

The standard Lean checks and documentation checks serve different purposes. The former validate proof artifacts; the latter validate coverage and provenance. This report checked the source and recorded workflow status. A separately reproduced local build and an external proof checker would add independent verification layers.

## Appendix B — Relationship to the Earlier Book

This monograph expands *How We Formalized Questions About Society: A Reader's Guide to 67 Lean Proofs, Their Theory, and Their Limits* (Formalizing Soft Sciences Project, 2026). It preserves the earlier distinction between reach, membership, trust, and incentives; the six foundation modules; the theorem identities; and the connection from proof to research question.

The expanded presentation adds a cross-disciplinary account of mathematical and computational modeling, longer worked arguments, a formal AI-evaluation proposal, and integrated discussion of normative reasoning. It also reconciles the earlier book's chronology: its early chapter describes the 16-theorem stage, while later chapters describe the 67-theorem release. Proposed task-complementarity examples in that early discussion subsequently appear as checked results in the collective-action module.

The earlier book records a separate, larger mathematics-of-psychology corpus whose location had not been recovered. That corpus remains outside this 67-theorem audit. This edition neither counts it nor replaces it. Its future integration would require its source, toolchain, provenance, and a reproduced verification record.

## Appendix C — Formal Objects at a Glance

| Object | Exact role in the source |
|---|---|
| `Adj a b` | One natural-number label is the successor of the other |
| `Reach a b` | A finite chain generated by reflexivity and adjacent steps |
| `Included A B` | Every member of A is a member of B |
| `StableCC b c s` | Every unilateral Boolean deviation against a contributor has payoff no larger than contribution |
| `response a i` | Integer addition of latent value and intercept |
| `Equivalent predict design theta phi` | Candidate predictions agree at every permitted probe |
| `Identified predict design` | Equivalent candidates must be equal |
| `Fits hypothesis evidence` | The hypothesis agrees with every listed input–label pair |
| `Feasible canDo group` | Every task has a capable member in the group |
| `Accepts cost reward group` | Every member's reward meets their cost |
| `Ready canDo cost reward group` | Feasibility and acceptance both hold |
| `Higher sa na sb nb` | Cross-multiplied counts satisfy `sb × na < sa × nb` |

The exact source definitions govern interpretation. The notation in this table is a reading aid, with parameter names expanded for clarity.

## Appendix D — A Research Program With Concrete Milestones

**Milestone 1: a validated semantic map.** Have a mathematical reviewer and a domain researcher inspect a small set of paired informal and formal statements. Resolve disagreements about variable meaning before adding extensive proofs.

**Milestone 2: a richer measurement model.** Select one target contrast, state its measurement equation, and distinguish exact identification from finite-data recovery. Develop a sensitivity analysis whose assumptions can be informed by data or substantive knowledge.

**Milestone 3: a design-changing result.** Identify a rival explanation that the initial task cannot separate. Add an observation or intervention with a clearly stated discriminating role. Evaluate its practical recovery properties before collecting a large confirmatory sample.

**Milestone 4: a reusable model artifact.** Package the statement, definitions, proof, interpretation, and verification receipt with an immutable version. Record source licensing and authorship so the artifact can be reused responsibly.

**Milestone 5: a controlled AI evaluation.** Compare representation and checker-access conditions, split by model families, and evaluate both formal correctness and scientific interpretation. Publish failures and successful cases with the same provenance discipline.

These milestones make progress visible through capabilities acquired: a better specification, an identified contrast, an improved design, a reproducible artifact, and a tested reasoning benefit.
