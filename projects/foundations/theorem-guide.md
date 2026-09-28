# What the 51 new Lean theorems prove

The declarations below were checked with Lean 4.19.0. The [verification receipt](verification.md) gives the exact source revision and audit. A theorem's name is a navigation aid; its statement and definitions determine what it says. Supporting lemmas and examples are included in the count. None is presented as a new empirical law.

Read each section as **model → implication → possible use → boundary**. The [research report](report.md) develops the applications and source context. The [inventory](theorem-inventory.csv) maps every name to its file and explanation. The [original guide](../solidarity-at-scale/formal/what-lean-proves.md) continues to cover the earlier 16 declarations.

## 1 Identifiability — 9 declarations

[Source: Identifiability.lean](../../SocialScience/Identifiability.lean). Namespace: `SocialScience.Identifiability`.

A model parameter predicts an exact output for each probe. A design specifies which probes are available. `Equivalent` means two candidates give the same outputs on that design. `Identified` means no distinct candidates remain equivalent.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `equivalent_refl` | A candidate is observationally equivalent to itself. |
| `equivalent_symm` | If A and B are equivalent, B and A are equivalent. |
| `equivalent_trans` | Equivalence through a third candidate is transitive. |
| `restrict_design` | Candidates equivalent on a larger probe set remain equivalent on a subset. |
| `more_probes_preserve_identification` | Expanding an already identifying probe set preserves identification. |
| `postprocess_preserves_equivalence` | Applying one common function to equal outputs cannot distinguish them. |
| `baseline_ambiguous` | The sum-only probe gives the same output for component pairs `(1, 0)` and `(0, 1)`. |
| `baseline_not_identified` | Therefore the sum-only design does not identify both components over the specified parameter space. |
| `both_probes_identify` | Observing both the sum and the first component identifies the ordered pair exactly. |

**Psychology use:** before collecting data, ask whether the proposed task can distinguish the mechanisms being compared. **Boundary:** a structurally identifying task may still estimate parameters poorly with noisy, finite data. No statistical efficiency or human mechanism is proved here. Generalization is within the specified candidate class; omitted alternatives are not ruled out.

## 2 Measurement — 9 declarations

[Source: Measurement.lean](../../SocialScience/Measurement.lean). Namespace: `SocialScience.Measurement`.

The equation is `response = latent + intercept`, using integer units, a loading of one, and no random error. The latent value is a formal unknown, not a validated psychological construct.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `common_intercept_preserves_order` | With the same intercept, response order and latent order agree in both directions. |
| `common_intercept_preserves_difference` | The response difference equals the latent difference when intercepts match. |
| `shift_invariance` | Adding a shift to the latent value and subtracting it from the intercept leaves the response unchanged. |
| `population_shift_invariance` | The same shift can be made for every person while preserving the entire response function. |
| `known_intercept_identifies` | Equal responses with the same specified intercept imply equal latent values. |
| `anchor_identifies_intercept` | Equal responses for the same specified latent anchor imply equal intercepts. |
| `group_intercepts_can_reverse_order` | A concrete pair of unequal intercepts reverses a latent ordering in the responses. |
| `bounded_bias_interval` | If differential intercept bias lies between `−δ` and `δ`, the latent difference lies within `δ` of the observed difference. |
| `difference_exceeding_bias_identifies_order` | An observed difference larger than an upper bound on differential bias establishes the latent ordering. |

**Psychology use:** separate assumptions about comparable measurement from conclusions about group differences. The bound can support a sensitivity analysis once its size is substantively justified. **Boundary:** these are not results about reliability, factor-model fit, partial scalar invariance, or an actual instrument. An anchor that is only assumed comparable may conceal the very bias being investigated.

## 3 Causality — 6 declarations

[Source: Causality.lean](../../SocialScience/Causality.lean). Namespace: `SocialScience.Causality`.

Both models set observed treatment equal to a binary background variable. One model makes the outcome copy treatment; the other makes it copy background. The observational object is the exact mapping from background to the observed treatment–outcome pair. The effect numerator sums the two treatment contrasts over the two background values.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `observational_equivalence` | The two models have exactly the same observational mapping. |
| `intervention_disagreement` | At treatment true and background false, their intervention outcomes differ. |
| `treatment_effect_numerator` | The treatment-copy model has an effect numerator of 2. |
| `common_cause_numerator` | The background-copy model has an effect numerator of 0. |
| `no_universal_observational_estimator` | No function of this observational mapping returns the correct effect numerator for every candidate binary model. |
| `all_responses_identify` | If two deterministic models agree for every treatment and background combination, their outcome functions, and hence the models, are equal. |

**Social-science use:** identify what additional assumption or observation a causal claim requires. **Boundary:** the last theorem assumes complete exact response information, including background; it is not a proof that any randomized finite experiment recovers a whole causal model. The impossibility result does not prohibit identification in a restricted model class. No full causal graph calculus, sampling distribution, or network process is encoded.

## 4 Learning — 9 declarations

[Source: Learning.lean](../../SocialScience/Learning.lean). Namespace: `SocialScience.Learning`.

`Fits` means a deterministic hypothesis agrees with every input–label pair in a finite list. This describes exact consistency, not a likelihood or degree of belief.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `fits_empty` | Every hypothesis fits an empty evidence list. |
| `fits_cons_iff` | Fitting a new observation plus the old list is equivalent to matching the new label and fitting the old list. |
| `fits_append_iff` | Fitting two combined lists is equivalent to fitting each separately. |
| `more_evidence_narrows_models` | Any hypothesis fitting a larger evidence list fits its included sublist. |
| `truth_survives_correct_label` | A truth function that fits the old evidence still fits after one correctly labeled example. |
| `distinguishing_query_eliminates_rival` | A rival that disagrees at a queried input cannot fit evidence containing the truth's label there. |
| `conflicting_labels_impossible` | If the list assigns distinct labels to the same input, no deterministic hypothesis fits it. |
| `incorrect_label_excludes_truth` | An incorrect label excludes the truth function from exact-fitting candidates. |
| `duplicate_evidence_same_models` | Appending the same evidence list to itself changes no exact-fitting candidates. |

**Psychology use:** a transparent baseline for concept learning, cultural classification, or designing a discriminating query. **Boundary:** it includes no psychological process, memory constraint, noise model, prior, or finite-sample generalization bound. Repeated independent observations can still be informative in statistical models. The definition treats input meanings as stable; cultural change may violate that assumption.

## 5 Collective action — 10 declarations

[Source: CollectiveAction.lean](../../SocialScience/CollectiveAction.lean). Namespace: `SocialScience.CollectiveAction`.

`Feasible` means every task has a capable group member. `Accepts` means every member's reward meets their cost. `Ready` is their conjunction. The name does not assert a real organization is ready to operate. Costs and rewards are integer tokens; outside options are normalized to zero.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `adding_members_preserves_feasibility` | Adding members cannot destroy task coverage when capabilities are fixed and uncongested. |
| `restricting_members_preserves_acceptance` | Removing members preserves the remaining members' participation inequalities when their rewards and costs stay fixed. |
| `union_accepts_iff` | A union satisfies these inequalities exactly when each component group does, using the same reward and cost functions. |
| `indispensable_member_withdrawal` | If every capable group member for a specified task must be one particular agent, excluding that agent makes coverage impossible. |
| `complementary_pair_feasible` | In the two-role example, the pair covers both tasks. |
| `no_specialist_alone_feasible` | Neither specialist alone covers both tasks. |
| `aggregate_surplus_not_participation` | Costs 1 and 1 with rewards 0 and 3 yield positive aggregate surplus but fail `Ready`. |
| `repaired_allocation_ready` | Rewards 1 and 2 cover both participation constraints in the feasible pair. |
| `two_person_budget_iff` | An acceptable division of an unrestricted integer budget exists exactly when it covers both costs in total. |
| `acceptable_share_interval` | A particular share is acceptable to both exactly when it lies between the first cost and budget minus the second cost. |

**Sociology use:** distinguish complementary roles, feasible production, allocation, and participation. **Boundary:** coverage does not enforce simultaneous scheduling; acceptance is a specified inequality, not a psychological survey response. `Ready` is not a Nash equilibrium or a core allocation. There is no strategic deviation model, property-rights mechanism, endogenous enforcement, or fairness criterion. A single person's withdrawal theorem does not demonstrate the original group was feasible unless that is separately established.

## 6 Aggregation — 8 declarations

[Source: Aggregation.lean](../../SocialScience/Aggregation.lean). Namespace: `SocialScience.Aggregation`.

`Higher` compares rates by cross-multiplying natural-number counts. Positive denominators are required to interpret that predicate as a rate comparison. They are checked for the concrete example; the generic predicate alone does not enforce them.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `reversal_cells_valid` | All four example cells have positive denominators and admissible success counts. |
| `first_stratum_advantage` | A's rate 9/10 exceeds B's rate 80/100 in context 1. |
| `second_stratum_advantage` | A's rate 20/100 exceeds B's rate 1/10 in context 2. |
| `pooled_reversal` | Pooling produces a higher rate for B: 81/110 versus 29/110. |
| `simpson_reversal` | The two within-context advantages and their pooled reversal hold together. |
| `equal_weight_addition_preserves_order` | Adding two integer inequalities with the same unit weights preserves order. This is not a theorem about arbitrary weighted means. |
| `aggregate_cannot_identify_components` | Reuses the proof that a sum-only observation cannot identify both unknown components. |
| `recoding_cannot_restore_components` | Any common recoding of that sum still leaves the demonstrated pair indistinguishable. |

**Anthropology and ethnology use:** scrutinize pooling and the level of an inference before attributing an aggregate pattern to an individual or cultural mechanism. **Boundary:** the example is synthetic, not an estimate of how often reversals occur. It does not decide which adjustment is causally appropriate or model shared ancestry and cultural diffusion.

## How these foundations fit together

Identifiability supplies the language for both informative measurements and lossy summaries. Measurement adds a particular response equation and sensitivity bound. Causality distinguishes observational equivalence from intervention behavior. Learning tracks which candidates remain compatible with exact evidence. Collective action separates capability constraints from participation constraints. Aggregation checks whether a summary preserves the comparison one intended to make.

That is a reusable starting point for formal research. The [problem register](open-problems.md) specifies what would have to be added before claiming a more realistic psychological or sociological result.
