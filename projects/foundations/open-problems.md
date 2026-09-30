# Research problems: completed models and unfinished science

Status at 28 September 2026 UTC. **None of the results in this release is claimed to solve a field-level open problem.** An implementation gap, a proposed modeling question, and an unresolved scientific problem are different statuses. This register keeps them separate.

## A. Restricted questions answered in this release

| ID | Question and exact scope | Answer | Status |
| --- | --- | --- | --- |
| B01 | Can a sum-only probe identify two arbitrary integer components? Can adding the first-component probe help? | No for the first design; yes for both exact probes. | Established mathematical idea; verified model question. |
| B02 | What does an assumed differential intercept-bias bound imply in an additive score equation? | A latent-difference interval; its sign is determined when the observed gap exceeds the bound. | Elementary sensitivity result; verified model question. |
| B03 | Can every deterministic binary model's effect be recovered from the specified observational function? | No: two models have equal observations and different effects. | Standard non-identification argument; verified model question. |
| B04 | Does one discriminating, correctly labeled query eliminate a rival exact-fitting hypothesis? | Yes; a wrong label can also eliminate truth. | Established consistency reasoning; verified model question. |
| B05 | When can a two-person integer budget meet both participation constraints? | Exactly when it covers their combined costs, with the stated unrestricted transfers. | Elementary allocation condition; verified model question. |
| B06 | Can pooling reverse two within-context rate comparisons with valid counts? | Yes; the checked synthetic example supplies a witness. | Established aggregation phenomenon; verified model question. |

These are useful small answers. Calling them new solutions to long-standing open problems would be misleading. Their proofs are in the [theorem guide](theorem-guide.md).

## B. Concrete next formal developments

**30 September reconciliation:** the remembered 67-item package is recovered as 16 solidarity plus 51 foundations declarations; the clinical extension brings the integrated corpus to 85. D01 below now concerns only the distinct older corpus whose original source remains unresolved. This dated clarification preserves the earlier register; see the [current psychology status](../../psychology/README.md) and [source map](../../PUBLICATION-COVERAGE-2026-09-29.md). Source-backed cross-project targets are indexed in the [omnibus catalog](https://github.com/Sodelin/Cross-Scale-Causal-Formalization/blob/main/research/open-problem-catalogs-2026-09-30/README.md).

| ID / priority | Proposed task | Dependencies and completion criterion | Novelty status |
| --- | --- | --- | --- |
| D01 / first | Recover the earlier psychology corpus and map its constructs and theorems. | Original repository, archive, or git bundle; preserve hashes and provenance, reproduce its original build, then identify reusable modules. | Recovery and integration; not a new theorem. |
| D02 / first | Generalize additive measurement to several indicators and explicitly constrained anchors. | Specify parameter transformations and identify an exact invariance class; prove a necessary/sufficient condition for identification in that class, or give a counterexample. | Standard identification literature must be checked before any novelty claim. |
| D03 / first | Formalize distinguishing probe selection for a finite candidate family. | Finite hypotheses and probes; characterize identification as separation of each distinct pair; compare a proposed probe set with that condition. | Likely established combinatorial content; useful infrastructure. |
| D04 / next | Replace exact consistency with bounded corruption or probabilistic evidence. | Choose a noise model and loss; prove a survival/error bound with all sampling assumptions explicit. Extend from compatible toolchain/library support. | Established learning theory is the starting point; no new bound claimed. |
| D05 / next | Model finite tasks with capacity and nonzero outside options. | Explicit assignment function and budget constraints; prove when an assignment and acceptable allocation coexist. Avoid assuming one person has unlimited capacity. | Matching, scheduling, and cooperative-game predecessors need comparison. |
| D06 / next | Prove aggregation conditions under fixed common composition weights. | Positive denominators, common weights, and a specified target estimand; distinguish arithmetic preservation from causal adjustment. | Established statistics and order properties; formalization target. |
| D07 / later | Express a restricted social-network causal identification result. | First formalize the graph, latent variables, probability assumptions, and observation scheme. Reproduce a published positive result before weakening assumptions. | F04–F05 are predecessors; not an unclaimed open theorem. |

No deadline or unattended continuation is implied. These tasks are ordered so later proofs reuse earlier definitions rather than accumulating disconnected examples.

## C. Broader scientific questions that remain unresolved here

**Measurement across settings.** When do different languages, response styles, social roles, and settings preserve the construct being measured? Identification conditional on a measurement equation is not evidence for that equation. A worthwhile project combines formal invariances with instrument-specific validity evidence. F03 is methodological background, not proof that no adequate methods already exist.

**Mechanism discrimination in psychology.** Which feasible tasks distinguish competing theories once noise and model misspecification are allowed? D02–D04 provide possible building blocks. The practical challenges discussed in F01–F02 cannot be solved by treating a model's parameters as observed facts.

**Homophily and social influence.** Which restrictions identify effects in a particular network, and how sensitive are estimates to violations? F04 gives a confounding analysis; F05 gives positive results in restricted settings. F05's preprint also mentions possible extensions involving support conditions and finite-sample bias bounds. Those are **historical research leads**: this search did not establish that they remain open in 2026. They are not advertised as unsolved targets ready for a novelty claim.

**Cultural dependence and comparison.** How should ancestry, diffusion, shared environments, and measurement differences enter a particular causal question? F06–F07 motivate making those pathways explicit. Generic dependence adjustment can answer the wrong question. This release does not estimate a cross-cultural effect or recommend a universal correction.

**Institutional stability and distribution.** Can cooperation persist when rewards, enforcement, outside options, and capabilities change together? The allocation condition here says only that a feasible transfer exists. Existence does not supply a bargaining process, credible commitment, political legitimacy, or a criterion of justice. Each of those requires its own definitions and evidence.

**Composition across social levels.** Which relationships survive moving from individuals to organizations, regions, and nations? A nesting map for memberships is not proof of self-similar causal dynamics. A concrete next case should define the lower-level dynamics, the aggregation map, and the macro-level claim before attempting a preservation theorem.

## D. What would count as an actual advance?

A new theorem would need a precise statement, a comparison against the strongest relevant prior results, a proof, and independent review of both its correctness and novelty. A new empirical result would additionally need valid measures, appropriate data, a credible design, and uncertainty analysis. A new formalization can be valuable without either kind of scientific novelty, but should say exactly which established result it encodes and which prior libraries it reuses.

For this release, the defensible claims are checked elementary results, explicit assumptions, useful counterexamples, and a connected implementation. See [references and access depth](sources/references.md) and [verification](verification.md).
