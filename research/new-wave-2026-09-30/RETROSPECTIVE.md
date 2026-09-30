---
title: "Research retrospective: model validity, theorem strength, and premature completion"
date: 2026-09-30
author: "Nolan Downard — AI-assisted research audit"
tags: [research/audit, formal-methods, computational-psychology, model-validity, theorem-strength]
status: "Source-grounded critique; no new Lean build"
---

# 0. Executive summary

**Verdict:** the work contains real, preserved formal developments, but its components have very different scientific reach. The central weakness is the gap between a verified consequence of a stipulated model and a model that captures the mechanism motivating the research. The workflow also needs an explicit search for stronger conclusions before completion.

The most important findings:

1. **The current social/psychological corpus is on main: 85 declarations, including the earlier 16.** It contains 51 foundations declarations and 18 clinical-fragment declarations. These are not 85 discoveries. A reviewed GitHub Actions run at the audited head succeeded.
2. **The biology-side predictive-state work is substantially stronger than the social toy models.** It includes a general coarsest exact deterministic representation and stochastic preservation of full finite observation/action histories. Its exact transition-law premise is restrictive; approximate preservation remains a written, unmechanized target.
3. **The CBT extension checks a genuine published-code fragment.** A fresh transcription check passed for ten matrices and six selected source assignments. It does not reconstruct the inference, policy selection, or learning responsible for simulated therapeutic change.
4. **Identity and symbols are mathematically irrelevant to the current cooperation model by construction.** They do not enter its payoff function. Those results establish logical possibilities under that restriction, not empirical insignificance of identity or symbols.
5. **The Nanuq continuation was preserved.** Main contains all-level computer-assisted results, a sharp five-taxon testing cutoff for a particular parameter criterion, and a sharp raw-matrix noise radius. The full all-level source theorem is not end-to-end Lean checked.

**Evidence bands:** High confidence for inspected source definitions, blob identity, and freshly executed arithmetic/transcription/replay checks. Moderate confidence for the current theorem-to-source interpretation and selected biological-model assessment. Provisional confidence for unrebuilt proof dependencies and the complete Nanuq graph-to-enumeration bridge. No new empirical evidence of clinical efficacy, molecular mechanism, or psychological construct validity is supplied. These are audit bands, not a clinical GRADE assessment.

**Highest-leverage next actions:** finish the approximate stochastic-abstraction theorem; specify an actual source-linked CBT learning question before extending the fragment; revise claims whose target variables are absent; introduce a theorem-strength review that requires boundary tests, attempted generalization, and a stopping justification. Preserve useful verification work while evaluating discoveries separately.

# Research retrospective: from verified equations to behavioral models

# 1. Abstract

This audit examines the three repositories named by Nolan, focusing on psychological interpretation, the biological-to-behavioral bridge, and the tendency to finish intermediate tasks without seeking a stronger result. Sixty-four retrieved files were checked against Git blob identities, including published MATLAB source. All current social/clinical formal modules were inspected; selected biological, predictive-memory, and Nanuq artifacts were reviewed. Fresh checks reproduced the CBT transcription and the saved finite Nanuq replay, with additional exact-arithmetic stress witnesses. This is a targeted technical audit, not a systematic literature review, complete reproof of the Samuel Alexander corpus, or empirical validation study.

# 2. Introduction: what Nolan's criticism identifies

The complaint concerns **premature acceptance of an intermediate theorem**: a level-specific result can sometimes become all-level, a sufficient constant can sometimes become sharp, and a construction can sometimes become a necessary-and-sufficient characterization. Better documentation alone does not perform that search.

The earlier conversational assessment undercounted what was already implemented. It treated the program too much as a future ambition and did not inspect its live artifacts. The corrective standard is to name the current definition, theorem, evidence, and missing correspondence.

“Maximal” must be given a mathematical meaning. A theorem can be stronger by using fewer assumptions, covering more cases, yielding an exact value, attaining an optimal constant, or providing an algorithm. These axes need not be comparable. There may be no single strongest useful theorem. A universal theorem with unrealistic premises may be scientifically less informative than a bounded theorem with measurable conditions.

# 3. Method and audited snapshots

| Repository | Audited main commit | Scope |
|---|---|---|
| [Formalizing Soft Sciences](https://github.com/Sodelin/Formalizing-Soft-Sciences/tree/4cf7366db359317e974416d81a0fe5d6aa258f6e) | `4cf7366db359317e974416d81a0fe5d6aa258f6e` | All current formal social/clinical modules, audit records, source bridge and project status |
| [Mathematics of Psychology Formalized](https://github.com/Sodelin/Mathematics-of-Psychology-Formalized/tree/d75ec0ec75f5e21d112416b1524958f4885b5e10) | `d75ec0ec75f5e21d112416b1524958f4885b5e10` | All 16 solidarity declarations and current source/result account |
| [Work on Samuel Alexander Research](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/tree/35570664221956edd153cceaa5351a9f7d63605f) | `35570664221956edd153cceaa5351a9f7d63605f` | Selected model-scope, predictive-state, stochastic, ancestry, speciation and Nanuq material |

Repository inventories, recent commits, and source files were retrieved through authenticated GitHub access. Retrieved file blob IDs matched the corresponding audited tree entries; exact UTF-8 bytes were locally reconstructed and all 64 Git blob hashes were recomputed successfully. Repository enumeration does not imply every repository on the account was substantively audited.

Fresh execution:

- Published CBT source-table comparison: PASS, ten exact matrices and six selected assignment guards.
- Nanuq finite JavaScript replay: PASS; full parsed JSON equals the saved result.
- Independent exact-arithmetic critique checks: PASS; 343 cooperation parameter cases, 45 sharp measurement intervals, 459 CBT normalized-column cases, a repeated-observation counterexample, and 32 approximation-witness cases.

The Nanuq replay covered 84,076 tree configurations, 2,525,210 occurrence selections, 122 quartet systems, and 24,667 anchor checks, with zero negative coefficients, support mismatches, or boundary failures. These are finite checks, not an independent proof of the infinite-family reduction.

Lean/lake were unavailable in this execution environment. No fresh local Lean build is claimed. The [successful social-sciences workflow at the audited head](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36641227653) is separate evidence from local execution. The published MATLAB file was pinned at commit `82a0a3d75b0bdc08d2b78cdf2201d7aa626c27a3`.

# 4. Findings: exact modeling critique

## 4.1 Cooperation, identity, and symbols

Source: [Solidarity.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/4cf7366db359317e974416d81a0fe5d6aa258f6e/Solidarity.lean).

The payoff is

```math
u(a,b)=B\mathbf1[b=\mathrm{contribute}]
      -C\mathbf1[a=\mathrm{contribute}]
      -S\mathbf1[a=\mathrm{defect}].
```

Given a contributing partner, the unilateral advantage of contribution over defection is exactly (S-C). Therefore `cooperation_stable_iff` establishes (C\le S). The partner benefit cancels.

**Sound result:** an exact incentive threshold for this externally enforced donation game.

**Critical modeling limitation:** labels, cultural markers, identity, beliefs about enforcement, and trust do not enter this equation. The heterogeneous/homogeneous/same-symbol witnesses vary labels while using stipulated payoffs. They cannot distinguish identity-mediated incentives from material incentives, nor estimate the contribution of shared symbols. `connected_without_trust` similarly makes trust an independent relation and chooses it to be false.

**Required improvement:** specify a pathway by which identity or a signal changes beliefs, preferences, expected enforcement, or interaction probability. Then compare a restricted null with a richer alternative. Include an outside option and an enforcement budget before using equilibrium stability as an explanation of voluntary institutional cooperation. An equilibrium can be stable while participation is unattractive.

**Potential stronger mathematical target:** characterize cooperation under uncertain sanctions and observation errors, then add participation and feasible institutional funding. Do not call that an empirical identity result without measurements and a justified model bridge.

## 4.2 Network reach and relationship limits

The natural-number path is connected with at most two neighbors per vertex and arbitrarily distant reachable vertices.

**Sound result:** a bounded local degree does not logically bound the connected population.

**Limitation:** graph reachability has no attention budget, maintenance cost, interaction frequency, transmission loss, or traversal-time constraint. It does not show that two personal relationships suffice for dependable large-scale social coordination. The model also uses an infinite population rather than a finite society with growing size.

**Useful extension:** finite populations with a fixed time/resource constraint, explicit decay or failure, and a quantitative reach guarantee. The exact question should be whether a local resource bound constrains reliable influence or task execution, not merely whether a path exists.

## 4.3 Measurement and construct validity

Source: [Measurement.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/4cf7366db359317e974416d81a0fe5d6aa258f6e/SocialScience/Measurement.lean).

The response is (y=\theta+b), in integer units. Shift invariance exhibits non-identification when both latent score and intercept are free. The differential-bias bound gives

```math
\theta_A-\theta_B\in[(y_A-y_B)-\delta,\ (y_A-y_B)+\delta].
```

**Sound result:** precise ambiguity and an identification interval under a supplied bias bound. The interval endpoints are attained by endpoint bias differences, so this interval can be described as sharp for the unrestricted additive model.

**Limitation:** the bias bound is assumed, not estimated. There is no item loading, nonlinear response, measurement error, test-retest variation, missingness, or empirical anchor validation. Recovering a model parameter does not establish that it measures the intended psychological construct.

**Improvement:** start from an actual measurement instrument and distinguish structural identification, estimation precision, and construct validity. Preserve the additive model as a transparent special case. Generalize only toward the uncertainty or invariance problem that the instrument actually presents.

## 4.4 Identification and causal inference

The two-component model observes either a sum or one component. The additional component probe identifies the pair exactly. The causal example observes treatment equal to background; two response functions agree on those observations but have intervention effects with numerators 2 and 0.

**Sound result:** exact observational non-identification and restoration of identification in the declared examples.

**Limitation:** the added probe has direct access to a component; its feasibility is assumed. The causal example has no treatment overlap and deterministic outputs. It does not diagnose the identification status of a real study. `all_responses_identify` assumes equality of every response function value and then proves structural equality; it is not a feasible-data identification theorem.

**Improvement:** define the actual observation and intervention interface first. For clinical research, identify the assumptions connecting assignment, adherence, observed outcomes, latent state and measurement. State whether the target is a latent parameter, treatment response, or causal contrast; do not interchange them.

## 4.5 Learning, evidence duplication, and noisy data

Source: [Learning.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/4cf7366db359317e974416d81a0fe5d6aa258f6e/SocialScience/Learning.lean).

`Fits` requires every label to agree exactly with a deterministic function. More constraints narrow the version space, a wrong label excludes the truth, and duplicating the identical list changes no constraint.

**Sound result:** exact constraint learning.

**Limitation:** this is not a learning-rate, memory, reinforcement-learning, or Bayesian updating model. “Duplicate evidence adds nothing” applies to duplicated constraints or copied records, not necessarily new independent observations with the same observed value.

**Fresh counterexample:** with prior odds 1:1 and likelihoods 0.8 versus 0.2, one positive observation gives posterior 4/5; two conditionally independent positive observations give 16/17. Copying the first record does not justify squaring its likelihood. Observation provenance and conditional dependence must enter any noisy extension.

**Improvement:** define sampling and error before adding robustness. Ask for posterior concentration, identification, or prediction under a specified noise model rather than claiming a general psychological theory of learning.

## 4.6 Published CBT reconstruction

Sources: [PublishedCBT.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/4cf7366db359317e974416d81a0fe5d6aa258f6e/clinical/ClinicalModels/PublishedCBT.lean), [SourceBridge.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/4cf7366db359317e974416d81a0fe5d6aa258f6e/clinical/ClinicalModels/SourceBridge.lean), [pinned MATLAB](https://github.com/rssmith33/Simulating_Cognitive_Behavioral_Therapy/blob/82a0a3d75b0bdc08d2b78cdf2201d7aa626c27a3/CBT_model.m).

Smith, Moutoussis and Bilek (2021) simulate interactions among belief, affect, avoidance and exposure using active inference. Their therapeutic predictions depend on learning and decision dynamics. The present Lean extension selects deterministic observation/transition tables and unnormalized belief weights; it omits those dynamics.

**Real contribution:** avoidance produces the same selected observation transcript under the two declared states, so no deterministic transcript classifier is correct for both. Approach distinguishes the states. The transcription bridge ties this statement to particular published tables instead of a wholly invented example.

**Main limitation:** the variable named `dangerous` selects a declared source-table condition. Its connection to an organism's belief or objective environmental danger must be specified, particularly when translating the result into clinical language. The proof is about supplied trajectories, not the agent's endogenous choice to avoid or approach. Deterministic distinguishability is not noisy clinical classification accuracy.

**Additional limitation:** source correspondence is not correctness of the complete MATLAB/SPM execution. A hash check and table extractor do not verify floating-point inference, stochastic trials, parameter updating, or treatment outcomes.

**Available stronger consequences, not newly Lean checked here:**

- Repeated continuation under the fixed avoidance transition remains observationally identical at every finite horizon. This needs a short induction; the current endpoint fixes four time points.
- Any randomized classifier based only on the identical transcript has the same prediction distribution in both states. Under equal priors its best accuracy is 1/2; under unequal priors it can exploit the prior but not the transcript.
- For the normalized implicit approach column, with (u>0) and (0\le c\le10u), total-variation distance between the two columns is exactly ( |c-u|/(10u) ). The interact column has the same value. This quantifies the existing equality boundary (c=u), rather than merely stating it.

These observations do not prove that exposure changes beliefs or that a therapy works. **Next meaningful clinical target:** select a source equation for updating or policy selection and formulate a claim about it, with a counterexample/search domain and a source-correspondence contract. Generalizing the easy observation lemma indefinitely would reproduce the same incremental-completion failure Nolan identifies.

## 4.7 Deterministic predictive state: the strongest bridge

Sources: [PredictiveState.lean](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/35570664221956edd153cceaa5351a9f7d63605f/research/open-problems/time-self-reference/predictive-memory/PredictiveState.lean), [RESULTS.md](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/35570664221956edd153cceaa5351a9f7d63605f/research/open-problems/time-self-reference/predictive-memory/RESULTS.md).

The model identifies two states when every finite common intervention word produces identical observations. Its quotient is coarsest by factorization among exact output-preserving controlled representations. The source also contains action restriction, distinguishing-word and stabilization results.

**Why this is stronger:** it moves beyond a chosen Boolean memory example to a general statement about what information any exact representation must retain. An action-dependent notion of retained state is a useful interface for behavioral modeling.

**Limits:** transitions are known, total and deterministic; the action/output vocabulary is fixed. For infinite state spaces, existence of a distinguishing word does not give an algorithm or uniform experiment length. Quotient minimality is not minimal physical storage, entropy, metabolic cost, consciousness, or biological implementation.

The concrete prime/wait/probe/reset parity example demonstrates the general concept under stipulated rules. It should remain an illustration rather than evidence about cells or cognition.

## 4.8 Stochastic abstraction: strong theorem, restrictive correspondence

Source: [StochasticAbstraction.lean](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/35570664221956edd153cceaa5351a9f7d63605f/research/open-problems/time-self-reference/predictive-memory/StochasticAbstraction.lean).

The central premise is actionwise pushforward equality:

```math
q_*K(a,x)=L(a,q(x)).
```

With output decoding and a policy that uses retained history, the development preserves complete finite observation/action transcript laws. It also distinguishes matching marginals, matching output traces, and an exact commuting state quotient.

**Sound and useful:** a rigorous criterion for transporting a controlled stochastic model across levels, including a joint transition/measurement interface.

**Central limitation:** equality must hold globally across the declared states/actions. Estimation error, partial interventions, hidden confounding, context drift, and misspecification are not automatically covered. A PMF framework does not directly cover arbitrary non-atomic continuous distributions. Controller memory and persistent sensor state must be retained or justified by the interface.

**Highest-priority mathematical extension:** the existing scope review proposes finite-horizon approximate preservation. Under matching policy/decoder interfaces, initial total-variation error (\delta) and uniform one-step error (\varepsilon), the written target is

```math
\mathrm{TV}(P_{0:n},\bar P_{0:n})
\le1-(1-\delta)(1-\varepsilon)^n
\le\min(1,\delta+n\varepsilon).
```

The saved review supplies a sharp absorbing-state witness and identifies coupling and transcript-support obligations. This is already a bounded, useful target, not a new conjecture invented for this retrospective. This audit checked exact arithmetic of selected witness cases; it did not mechanize the general theorem. Even a completed theorem would still require evidence that the uniform error premise is satisfied in the application.

## 4.9 Biology and social science: a pincer with an unfinished joint

The ancestry/gARG correspondence is an actual map between formal structures, not merely an analogy. However, destructive ancestry restriction is a data-processing operation; it is not a cell-learning or therapeutic intervention. The finite-view impossibility results concern information insufficiency, not general computational undecidability.

The biological-scope notes distinguish genealogical from genetic ancestry and keep different parenthood graph classes separate. The pure-induction/speciation packet also states that its joint process is stipulated rather than empirically inferred.

**The missing joint:** a shared behavioral model with a declared state, intervention interface and observation map. Biology should supply constrained mechanisms or kernels; social context should supply inputs, policies or interactions; behavior should supply measurable transcripts. At present these pieces are not assembled into a validated multiscale clinical model.

The predictive-state framework is a plausible mathematical interface for that assembly. It does not itself provide a physiological-to-psychological map. The strongest near-term plan is one behavioral task with rival models and a discriminating intervention, rather than a general formalization of biology before any behavioral result can be attempted.

## 4.10 Implemented coverage versus named aspirations

Within the reviewed current formal modules, I found no implemented full DBT model, disorder-level psychopathology model, autism mechanism model, or calibrated metacognitive confidence/control model. The generic learning and predictive-state material can support such work, but should not be relabeled as those specific models.

This is a statement about the inspected artifacts, not proof that no uninspected branch or older file exists. The current psychology README still contains historical recovery wording; the main project index and recent publication records give the more current account of the recovered corpus.

# 5. Conclusion and priorities

| Priority | Action | Concrete finish condition |
|---|---|---|
| P1 | Mechanize the existing approximate stochastic-abstraction target | Joint transcript bound, policy conditions, support/representation proof, sharpness witness and axiom/build receipt |
| P1 | Define one source-linked CBT learning or decision target | Exact source equation, interpretation, proposed theorem, assumption tests and reproducible baseline |
| P1 | Fix interpretations of identity/symbol results | Each claim names which variables enter the model and what observations could distinguish the proposed mechanism |
| P2 | Introduce theorem-strength search before completion | Dominance table, boundary witnesses, failed attempts, and a reason to stop |
| P2 | Build one biological/behavioral correspondence | Measurable task, candidate kernel/state map, held-out prediction and discriminating intervention contract |
| P2 | Reconcile historical documentation | One canonical current inventory; preserve historical records with explicit dates |
| P3 | Expand disorder or social-theory coverage | Only after the new model has a specific question and observable consequences |

# 6. Deconstructive analysis: where premature completion comes from

Nolan's dopamine analogy highlights an observable behavior, but it is not a demonstrated causal account of this assistant.

Human-feedback training can shape model outputs, as shown by Ouyang et al. (2022). That is distinct from claiming that a live chat receives a dopamine-like reward at each completed task, or that custom instructions update the deployed model's weights. We do not have internal telemetry establishing those claims.

A more testable workflow hypothesis is that the process favors **visible, locally verifiable completion**: a small lemma, passing checks, a detailed inventory, and a polished report. Those are easier to assess than novelty, external relevance, or the strongest attainable theorem. They can occupy the budget without advancing the motivating question. This is a proxy-objective concern; it need not involve deliberate cheating.

Possible competing causes include ambiguous task boundaries, conservative claims, missing source context, easy-to-build Std models, verification costs, and turn-level stopping incentives. The transcript alone does not identify their relative contribution. The prior model's purported internal explanation would not be independent evidence.

The hard external-open-problem gate in the current social repository is a useful **discovery-claim filter**, but too restrictive if interpreted as a prerequisite for every valuable model improvement. Source-faithful verification, better identifiability, and a clinically useful reliability bound can matter without closing an externally named open problem. The user-authorized retrospective does not require deleting that gate; the distinction should be made explicit in future project selection.

# 7. Reconstructive analysis: a stronger-result search protocol

Before writing the first lemma, define the scientific question and a target-strength table.

| Axis | Starting result | Required challenge |
|---|---|---|
| Domain | One level, example, parameter region | All levels? Multiple components? Which exclusions are essential? |
| Assumptions | Sufficient premises | Remove each premise; counterexample or stronger theorem? |
| Conclusion | Existence or upper bound | Construction, exact value, iff, uniqueness, or attainment? |
| Constants | Working value | Sharp value plus matching obstruction? |
| Information | Chosen transcript/probe | All horizons? Adaptive interventions? Noisy observations? |
| Representation | Convenient encoding | Actual source-class bridge? Invariance under representation changes? |
| Computation | Search success | Complexity or stopping certificate? |
| Scientific value | Formal consequence | What uncertainty, prediction, or decision changes? |

**Completion protocol:**

1. Pin the source/model and preserve the baseline.
2. Identify the result's strongest already available consequence.
3. Try weakening each substantive assumption and expanding each domain restriction.
4. Seek necessary-and-sufficient conditions, exact constants and attaining examples.
5. Check whether a proposed generalization is already established or scientifically irrelevant.
6. Separate proof integrity, source correspondence, empirical relevance and novelty assessments.
7. Finish with an explicit frontier: proved; refuted with witness; open after a recorded attempt; or deferred for a named cost/dependency.

Allocate a declared part of the task budget to this search before presentation. Treat that allocation as a tunable workflow parameter, not a validated universal percentage. Do not require an infinite search for “maximality.”

The evaluator must propose at least one materially stronger candidate and one substantive countermodel. “Checks pass” is insufficient. Documentation volume and declaration count must not be the discovery metric.

# 8. Middle-out synthesis: connect the levels through a task

A feasible demonstration begins at the behavioral interface. Declare interventions, observations and the outcome of interest. Compare candidate biological kernels or retained states below that interface and candidate policies/social inputs above it.

For a treatment-style approach/avoidance task, three outputs may agree even when mechanisms differ: overt approach, verbal safety belief and physiological arousal. A model should specify their joint distribution and identify an intervention that separates competing explanations. Formal proof can establish what that interface preserves; data must establish whether the interface represents the task adequately.

For the research workflow, run a paired experiment at equal budget: ordinary task instructions versus the theorem-strength protocol. Pin identical starting artifacts. Measure valid generalizations, removed assumptions, sharp constants, failed/corrected claims, reviewer-required follow-up, and cost per surviving contribution. Blind assessment where practical. Audit the assessment criteria separately from the generated results.

Using Nolan's assumed fivefold cost ratio, cost-effectiveness depends on validated contributions per unit cost: a cheaper model wins on this metric when its contribution yield exceeds one fifth of the more expensive model's, before unequal overhead. No current product-price or performance claim is verified here. More calls alone do not establish more research value.

# 9. Glossary

- **Structural identification:** distinct model parameters cannot produce the same permitted exact observations.
- **Construct validity:** evidence that a measure supports its intended psychological interpretation.
- **Source correspondence:** justified mapping between a formal reconstruction and the actual published definitions/code.
- **Lumpability:** states grouped together induce compatible transitions between groups.
- **Total variation:** a measure of difference between probability laws.
- **Sharp bound:** a guarantee paired with evidence that it cannot be uniformly improved in the stated class.
- **Attainment:** an actual admissible example realizes an extremal value.
- **Theorem dominance:** one result implies another on a declared comparison, usually through weaker premises or stronger conclusions.
- **Computer-assisted proof:** a mathematical argument whose finite computational component is part of its evidence; not automatically a Lean proof.

# 10. Bibliography and source relationships

1. Smith, R., Moutoussis, M., & Bilek, E. (2021). *Simulating the computational mechanisms of cognitive and behavioral psychotherapeutic interventions: insights from active inference*. Scientific Reports, 11, 10128. [DOI](https://doi.org/10.1038/s41598-021-89047-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/33980875/). Relationship: published target model; our selected source-table fragment is a partial verification of its implementation. Full body retrieved in successive chunks.
2. Holtgrefe et al. (2025). *Distinguishing Phylogenetic Level-2 Networks with Quartets and Inter-Taxon Quartet Distances*. Bulletin of Mathematical Biology. [DOI](https://doi.org/10.1007/s11538-025-01549-4). Relationship: source theorem/domain comparison for the Nanuq continuation. Targeted theorem and domain passages retrieved; not a fresh exhaustive priority review.
3. Ouyang, L., et al. (2022). *Training language models to follow instructions with human feedback*. [arXiv:2203.02155](https://arxiv.org/abs/2203.02155). Relationship: general training-background evidence; not telemetry about this assistant's current internal reward or online learning.
4. Amodei, D., et al. (2016). *Concrete Problems in AI Safety*. [arXiv:1606.06565](https://arxiv.org/abs/1606.06565). Relationship: conceptual background on reward/proxy specification; not a diagnosis of this run.
5. The three immutable repository snapshots and source links above. Relationship: primary artifacts audited; software/model evidence rather than independent empirical studies.

Prior mathematical relationships in the predictive-state notes include behavioral equivalence, automata minimization, controlled stochastic abstraction and predictive representations. This audit inspected those source relationships as repository records; it did not perform a new comprehensive priority review for the quotient construction.

# 11. Metacognitive review: process integrity

**Judgment:** strong artifact provenance and exact finite replay; incomplete local proof reproduction and bounded external-source coverage. No numerical AMSTAR-2 score is appropriate because this is not an intervention systematic review.

Strengths: immutable repository heads, matched blob identities, complete current social/clinical module coverage, full CBT body retrieval, explicit failed access routes, separation of fresh checks from saved receipts.

Limits: selected rather than complete Samuel Alexander review; no local Lean toolchain; no comprehensive branch recovery or human independent proof review; no preregistered audit protocol; targeted rather than exhaustive literature search. The failed public clone route was replaced by authenticated file retrieval. Nature/PMC web access failed on some routes; rights-eligible PubMed retrieval supplied the CBT body.

Confirmation bias risk: both Nolan's criticism and the prior assistant's polished self-description could steer the judgment. The audit sought cases where the work was stronger than remembered (predictive-state/Nanuq) and where interpretation exceeded model scope (identity/symbols). Exact arithmetic witnesses test substantive inference boundaries, not the number of checked lemmas.

Fixes: reproduce pinned Lean closures in a prepared environment; attach the strongest-result protocol to the next selected task; obtain independent human assessment of source correspondence and significance.

# 12. Metacognitive reflection: robustness of inference

No treatment effects were pooled; heterogeneity statistics, funnel plots and publication-bias tests are inapplicable. The relevant robustness tests are assumption sensitivity, model misspecification, source-class admission, and counterexample search.

**Robust verdict:** the current formal definitions support narrow, inspectable claims. Scientific generality varies sharply by module. The deterministic/stochastic abstraction work is mathematically general but depends on strong interfaces; social and CBT results are more specific and omit important motivating mechanisms.

**What would change the assessment upward:** a reconstructed source learning/policy equation with a substantive verified guarantee; the completed sharp approximate-abstraction bound; measured evidence supporting an application map; independently confirmed source-class Nanuq correspondence.

**What would change it downward:** a mismatch in the source bridge, reliance on a theorem that assumes the intended conclusion, a nonadmissible extremal witness, or a claim of full biological/clinical validation based only on formal correctness.

The reward-signal hypothesis remains causally unestablished. A controlled workflow comparison could support a behavioral effect of changed instructions; it would not reveal an internal dopamine-like mechanism.

# 13. Zotero and Obsidian integration

Save this Markdown note in an Obsidian research-audits folder. Link it to the canonical model notes rather than treating all 85 declarations as independent publications.

In Zotero, add the articles by DOI/arXiv identifier. Suggested tags: `role/source-model`, `role/prior-mathematics`, `role/workflow-hypothesis`, `method/formal-verification`, `status/partial-reconstruction`. Create software/repository items with the audited commit in the version or Extra field.

In Better Notes, use separate claim rows for **formal consequence**, **source match**, **empirical support**, and **novelty**. For CBT, relate the article to the code item and this audit; label the code relationship “partial reconstruction of observation/transition fragment.” For Nanuq, label the current packet “computer-assisted all-level theorem; full source Lean bridge incomplete.” Do not mark a queue submission as peer-reviewed acceptance.

# 14. Appendix: continuation, sharpness, and evidence boundaries

## Nanuq continuation recovered on main

The current continuation record states original NANUQ circularity and displayed-split support for every finite level and multiple blobs in the binary, semidirected LSA, galled, outer-labeled planar class. Older internal source-assessment documents cover an earlier circularity-only checkpoint; the current continuation packet and later support audits must be used for current status.

The [five-taxon result](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/35570664221956edd153cceaa5351a9f7d63605f/research/nanuq-all-level-2026-09-29/FIVE-TAXON-THRESHOLD.md) says universal anchor positivity in the declared four-score family is equivalent to testing representations with at most five total distinct taxa. A five-taxon obstruction shows four are insufficient. The score-independent structural restriction still retains at most six labels. These are different statements; no pointwise five-label structural compression is established.

The [noise refinement](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/35570664221956edd153cceaa5351a9f7d63605f/research/nanuq-all-level-2026-09-29/EXTREMALITY-REPLAY.md) uses integer rounding to recover the exact raw original matrix when entrywise error is strictly below 1/2. A tree/cycle midpoint obstructs uniform recovery at the closed radius 1/2. Support extraction requires the correct circular order. This is deterministic robustness, not empirical sample complexity or an order-estimation guarantee.

The latest continuation record reports submission under review, not catalog acceptance or external peer review. No new submission or researcher message was sent during this audit.

## What the finite replay establishes

Reproducing the saved JSON shows the finite verifier executes and reproduces its declared results. It does not independently certify the completeness of the plane-tree enumeration, the raw graph opening argument, global multi-blob composition, or every written corollary. Those remain separate mathematical obligations.

## What was changed in this retrospective

This audit created this report, exact source-byte/hash records and local critique checks. It did not alter Lean definitions, overwrite existing research, push new theorem claims, or modify repository history. The retrieved commits remain the basis for the judgments above.

