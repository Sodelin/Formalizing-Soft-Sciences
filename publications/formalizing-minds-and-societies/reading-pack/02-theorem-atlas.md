## 4.7 The complete atlas — all 67 declarations

This atlas expands the shorter tables in *How We Formalized Questions About Society*. Each entry gives the actual declaration name, its mathematical content, the proof idea, and the scientific question it makes clearer. The source for all 67 entries is the pinned project release (Sodelin, 2026); the earlier guide provides the narrative baseline (Formalizing Soft Sciences Project, 2026). The numbering is a reading order used in this edition; Lean identifies results by their namespace and name.

The atlas can be read in two directions. The network section follows the original question of how cooperation extends beyond direct acquaintance. Readers interested in psychological methodology can begin with measurement (17–25), identifiability (26–34), and causality (35–40), then connect those results to learning and aggregation.

Numerical examples are synthetic constructions chosen to make the mathematical relationships transparent. Proof-method descriptions are explanations of the inspected source, not additional proofs created for this edition.

### A. Solidarity — 16 declarations

[Pinned source: Solidarity.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/Solidarity.lean)

The network uses natural-number labels: 0, 1, 2, and onward. Two labels are adjacent when they differ by one. `Reach` means there is a finite chain of these links. Membership is a predicate, trust is a separate relation, and the final six results concern a two-person donation game. The module deliberately keeps these meanings separate. Its network is undirected and has no travel cost. Its labels and trust relation are independent of the payoff mechanism, allowing logical relationships between those concepts to be examined directly.

### 01. `adj_symm` — a direct link goes both ways

**Claim:** if A is adjacent to B, B is adjacent to A. **Why:** the definition allows either number to be one greater than the other; exchanging the two alternatives proves symmetry. **Use:** this establishes that the example is an undirected network. It is a supporting lemma for later path proofs.

### 02. `reach_trans` — two routes can be joined

**Claim:** if A can reach B and B can reach C, A can reach C. The proof follows the second route step by step and extends the first route. **Example:** a referral chain from one service to another can be concatenated with a further chain as a graph-theoretic possibility.

### 03. `reach_symm` — a route can be reversed

**Claim:** any finite path can be followed in the opposite direction. The proof uses symmetric adjacency and route concatenation. **Use:** it turns routes from the starting vertex into routes back to it, enabling the general connectivity proof.

### 04. `zero_reaches` — every numbered position is reachable from zero

**Claim:** for any natural number `n`, vertex 0 reaches vertex `n`. The proof is induction: 0 reaches itself, and a route to `n` extends one step to `n + 1`. **Intuition:** a finite trip can reach any particular point along an indefinitely extended chain.

### 05. `path_connected` — any two vertices are connected

**Claim:** every A reaches every B. The proof goes from A back to 0 and from 0 to B. **Use:** this is the main connectivity result for the example. It shows that a network's global extent need not equal the number of people directly known by one member.

### 06. `at_most_two_neighbors` — local contact is tightly bounded

**Claim:** if B is adjacent to A, B must be `A + 1` or `A − 1`. The formal result gives an explicit two-candidate bound on adjacent labels. At vertex 0 there is only one actual adjacent vertex. **Use:** paired with global reach, this separates local and global structure.

### 07. `unbounded_reachable` — bounded local contact permits unbounded reach

**Claim:** for any proposed numerical bound, some larger numbered vertex remains reachable from 0. Choose the next number and apply result 04. Together with result 06, it gives a counterexample to the claim that bounded direct contacts necessarily bound an entire connected population.

### 08. `membership_nesting` — inclusion is transitive

**Claim:** if every A-member belongs to B and every B-member belongs to C, every A-member belongs to C. The proof composes the two inclusion assumptions. **Example:** if a study's recruitment strata genuinely nest inside its sampling frame, the resulting inclusion follows.

### 09. `overlapping_memberships` — groups can overlap without being identical

**Claim:** there exist groups with a shared member and an exclusive member on each side, all within one population. The witnesses are A = {0,1}, B = {0,2}, with the common population containing every natural number. **Use:** this permits multiple intersecting memberships. It is a logical basis for representing someone as a researcher, musician, and community member.

### 10. `connected_without_trust` — a connection does not entail trust

**Claim:** a connected network can coexist with a trust relation in which person 0 does not trust person 1. The proof chooses a relation that is false everywhere; the stated conclusion only requires that particular missing trust relation. **Use:** it blocks the inference from network connectivity alone to trust.

### 11. `cooperation_stable_iff` — the exact incentive threshold

**Claim:** mutual contribution resists a unilateral payoff-improving deviation exactly when contribution cost is no larger than the defection sanction. If the other person contributes, contributing pays `benefit − cost`; defecting pays `benefit − sanction`. The benefit cancels. **Example:** benefit 3, cost 1, sanction 2 gives payoffs 2 versus 1.

### 12. `no_sanction_failure` — removing the sanction changes this game's incentive

**Claim:** when contribution has strictly positive cost and sanction is zero, mutual contribution fails the defined stability test. Result 11 would require a positive cost to be no greater than zero, a contradiction. **Use:** it isolates which term sustains the equilibrium in this payoff specification.

### 13. `heterogeneous_cooperation_exists` — different labels can coexist with stable cooperation

**Claim:** two players can receive different Boolean labels while mutual contribution is stable at benefit 3, cost 1, sanction 2. The proof assigns different labels and invokes the threshold theorem. **Use:** it defeats an unrestricted claim that identical labels are logically necessary for cooperation.

### 14. `homogeneous_cooperation_can_fail` — identical labels do not guarantee cooperation

**Claim:** two players can share a label while mutual contribution is unstable at benefit 3, cost 1, sanction 0. The proof gives both the same label and applies result 12. **Use:** similarity and incentives are separate ingredients in this vocabulary.

### 15. `symbols_alone_insufficient` — a shared marker changes nothing if it changes no mechanism

**Claim:** two players can share marker 7 and still face the unstable game with positive cost and no sanction. **Use:** this makes a research question visible: through which causal route would a symbol matter—expectations, preferences, coordination, or enforcement?

### 16. `mutual_gain` — both can do better under mutual contribution

**Claim:** if `cost < benefit + sanction`, the payoff under mutual contribution exceeds the payoff under mutual defection. These are `benefit − cost` and `−sanction`, respectively. Algebra gives the stated inequality. **Use:** it separates a comparison of outcomes from an incentive to reach or maintain an outcome.

**Research implications.** Two people can share a social marker without trusting one another; trust can exist without a profitable action; a profitable joint outcome can exist without individual incentives to maintain it. Those distinctions are the reusable achievement. A richer theory of identity can now specify how labels affect expectations, payoffs, or the network itself.

### B. Measurement — 9 declarations

[Pinned source: Measurement.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Measurement.lean)

The entire module uses `response = latent + intercept`, with integer values, loading one, and no random error. One psychological interpretation concerns the distinction between an underlying judgment process and response-scale use. That interpretation suggests measurements through which the model can be developed.

### 17. `common_intercept_preserves_order` — a shared offset preserves ranking

**Claim:** with the same intercept, A's response is no larger than B's exactly when A's latent value is no larger than B's. The proof cancels the shared addition. **Example:** adding 20 to both 40 and 60 keeps their order. **Use:** it identifies one sufficient measurement condition for ranking comparisons.

### 18. `common_intercept_preserves_difference` — a shared offset preserves the gap

**Claim:** subtracting the two responses gives exactly the latent difference when their intercepts match. **Example:** latent scores 7 and 4 become 10 and 7 after adding 3; the gap remains 3. **Use:** change or group comparisons can be robust to a common additive offset.

### 19. `shift_invariance` — the origin can move without changing an observation

**Claim:** adding any shift to a latent score and subtracting the same shift from the intercept preserves the response. **Example:** latent 4 plus intercept 3 and latent 6 plus intercept 1 both produce 7. **Use:** a single observed sum cannot fix the absolute origin of both components.

### 20. `population_shift_invariance` — more people do not automatically fix the origin

**Claim:** shifting every person's latent value by the same amount and compensating in the shared intercept preserves the entire response function. The proof applies result 19 to every person and then uses equality of functions. **Use:** increasing sample size alone cannot remove this structural ambiguity.

### 21. `known_intercept_identifies` — a fixed intercept removes one ambiguity

**Claim:** two latent values with the same specified intercept must be equal if their responses are equal. Cancellation proves it. **Use:** once the intercept is fixed, the response mapping is injective in the latent value.

### 22. `anchor_identifies_intercept` — a fixed latent anchor can calibrate an offset

**Claim:** if two intercepts produce the same response for the same latent anchor, the intercepts are equal. The anchor cancels. **Use:** an independently grounded reference can distinguish offsets in this model.

### 23. `group_intercepts_can_reverse_order` — measurement differences can reverse a comparison

**Claim:** although latent 0 is below latent 1, response 0 with intercept 2 exceeds response 1 with intercept 0. Lean checks the concrete arithmetic. **Use:** apparent ordering of scores need not equal ordering of the latent values. In a judgments-of-learning (JOL) study, a difference in scale use is one possible rival explanation worth assessing.

### 24. `bounded_bias_interval` — turn a bias assumption into a sensitivity interval

**Claim:** if the intercept difference is between `−delta` and `delta`, the latent difference lies between `observed difference − delta` and `observed difference + delta`. **Example:** observed gap 5 and bias bound 2 imply a latent gap from 3 to 7. **Use:** state how large differential bias must be to change an interpretation.

### 25. `difference_exceeding_bias_identifies_order` — a sufficiently large gap fixes the sign

**Claim:** if differential bias has an upper bound `delta` and the observed A-minus-B gap exceeds it, A's latent value exceeds B's. Only the relevant one-sided bias bound is needed. **Example:** a gap of 5 with an upper bias bound of 2 leaves a positive latent difference.

**Research implications.** An ANOVA or ANCOVA can estimate a response difference under its statistical assumptions. This module asks a prior interpretive question: what does that response difference say about the underlying construct? Neither analysis replaces the other.

### C. Identifiability — 9 declarations

[Pinned source: Identifiability.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Identifiability.lean)

A candidate predicts an exact output for each possible probe. A design chooses the allowed probes. Larger probe sets preserve exact identifying information; finite noisy estimation introduces a further question of precision. `Equivalent` means two candidates agree on every allowed probe. `Identified` means such agreement forces the candidates to be equal. This exact notion of structural information provides the foundation on which a finite-data recovery analysis can be built.

### 26. `equivalent_refl` — a candidate agrees with itself

**Claim:** any candidate is observationally equivalent to itself under any design. Its prediction equals itself at each permitted probe. **Use:** this is the reflexivity component of treating observational indistinguishability as an equivalence relation. Together with the next two lemmas, it supplies the equivalence structure used to reason about whole classes of explanations.

### 27. `equivalent_symm` — indistinguishability goes both ways

**Claim:** if A and B make equal predictions on the design, B and A do too. The proof reverses each equality. **Use:** the model does not privilege one explanation merely because its name appears first.

### 28. `equivalent_trans` — chains of exact agreement remain equivalent

**Claim:** if A agrees with B and B agrees with C on all allowed probes, A agrees with C. The proof composes equalities. **Use:** whole families of candidates can be grouped by what the design can distinguish.

### 29. `restrict_design` — discarding probes cannot distinguish previously identical predictions

**Claim:** candidates equivalent on a larger probe set remain equivalent on any included smaller set. Every smaller-set probe already belongs to the larger set. **Use:** dropping an informative task cannot create structural distinctions that were absent before.

### 30. `more_probes_preserve_identification` — adding exact probes retains existing identification

**Claim:** if a smaller design already identifies every candidate in the class, a larger design containing it also does. Agreement on the larger design implies agreement on the smaller one, which already forces equality. **Use:** a useful probe need not be discarded when adding another.

### 31. `postprocess_preserves_equivalence` — recoding identical outputs cannot create information

**Claim:** applying the same function to identical outputs leaves them identical. **Example:** if two mechanisms both produce 1, converting that score to a category, embedding, or deterministic summary still gives the same transformed result. **Use:** better downstream computation cannot recover a distinction absent from the input.

### 32. `baseline_ambiguous` — a sum admits distinct explanations

**Claim:** when the only probe observes the sum, components `(1,0)` and `(0,1)` both produce 1. **Interpretive example:** a response influenced by familiarity and another social cue could look identical under different combinations. The actual components are just integers. **Use:** one constructive witness can expose an ambiguous design.

### 33. `baseline_not_identified` — no exact recovery of both components from this design

**Claim:** the sum-only design does not identify arbitrary integer pairs. If it did, the two distinct pairs from result 32 would have to be equal, implying `1 = 0`. **Use:** the problem is not merely a small sample or a weak estimator; the observation map loses a distinction.

### 34. `both_probes_identify` — a discriminating second observation resolves the example

**Claim:** observing both the first component and the total identifies the ordered pair. Equality of first-component outputs fixes the first component; equality of totals then fixes the second. **Example:** total 7 and first component 3 determine second component 4. **Use:** design a measurement to separate explanations before collecting a large dataset.

**Research implications.** A warmth/competence and judgments-of-learning study can ask which rival psychological explanations predict the same observed pattern, then select a task or manipulation that separates them. The model turns an intuitive mechanism question into a design question.

### D. Causality — 6 declarations

[Pinned source: Causality.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Causality.lean)

There is a binary background `U`, treatment `T`, and outcome `Y`. Observed assignment makes `T = U`. In one model, `Y = T`; in the other, `Y = U`. The observational object is an exact mapping, and an effect numerator adds treatment contrasts across both background values. Probability distributions and division are not implemented.

### 35. `observational_equivalence` — the two causal stories produce the same observed mapping

**Claim:** both models return `(U,U)` for the observed treatment–outcome pair. The proof establishes function equality by checking an arbitrary background value. **Use:** even perfect observation of this assignment pattern cannot distinguish the two mechanisms.

### 36. `intervention_disagreement` — forcing treatment separates the stories

**Claim:** set treatment to true while background is false: the treatment-driven model returns true, whereas the background-driven model returns false. Lean checks this Boolean inequality directly. **Use:** an intervention can probe combinations that the observational assignment never produces.

### 37. `treatment_effect_numerator` — the treatment-driven model has numerator two

**Claim:** the sum of outcomes under treatment across both backgrounds minus the corresponding untreated sum is 2. Both background-specific treatment contrasts equal 1. **Interpretation:** if the two backgrounds are equally weighted, the average effect would be 1.

### 38. `common_cause_numerator` — the background-driven model has numerator zero

**Claim:** the same effect numerator is 0 when the outcome copies background and ignores treatment. Holding background fixed, changing treatment changes nothing. **Use:** results 37 and 38 supply the distinct correct answers needed for the impossibility proof.

### 39. `no_universal_observational_estimator` — equal inputs cannot yield two different correct effects

**Claim:** no function taking only the specified observational mapping can return the correct effect numerator for every binary model. Results 35, 37, and 38 force a contradiction: the estimator receives the same input but would need to return both 2 and 0. **Use:** it identifies an information limit shared by all estimators in the defined class.

### 40. `all_responses_identify` — a complete exact response table fixes this model

**Claim:** if two models agree at every treatment/background combination, their outcome functions—and therefore their model structures—are equal. Function equality supplies the proof. **Use:** it identifies sufficient information at the far end of the spectrum from the incomplete observational design.

**Research implications.** A model of why a therapy works needs more than reproducing a before-and-after association. The formal question is which assumptions and observations distinguish a treatment mechanism from alternative causes. Intervention-outcome evidence can then evaluate the treatment claim while the formal analysis clarifies what mechanism has been identified.

### E. Learning — 9 declarations

[Pinned source: Learning.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Learning.lean)

`Fits` means a deterministic hypothesis agrees with every input–label pair in a finite evidence list. The module formalizes consistency constraints on candidate explanations. Probabilistic labels, memory, and graded confidence provide natural extensions beyond this deterministic starting point.

### 41. `fits_empty` — no observations exclude no hypotheses

**Claim:** every hypothesis fits an empty evidence list. There is no listed example on which it can disagree. **Use:** this exposes the difference between consistency and evidential support: with no constraints, even a bad hypothesis fits.

### 42. `fits_cons_iff` — one new example adds one exact constraint

**Claim:** a hypothesis fits a new labeled example followed by the old evidence exactly when it matches the new label and fits the old list. The proof separates membership in the new head from membership in the old tail. **Use:** this is the logical structure of sequential elimination.

### 43. `fits_append_iff` — fitting combined evidence means fitting both parts

**Claim:** a hypothesis fits two concatenated lists exactly when it fits each list separately. The proof divides observations according to which list contains them. **Use:** it supports modular assembly of evidence constraints.

### 44. `more_evidence_narrows_models` — extra exact constraints cannot add fitting candidates

**Claim:** a hypothesis fitting a larger list also fits any included smaller list. Equivalently, the candidate set compatible with the larger list is contained in the earlier set. **Use:** gathering a discriminating observation can shrink the space of explanations.

### 45. `truth_survives_correct_label` — correct evidence preserves a fitting truth function

**Claim:** if the true function fits the existing list, adding its own label for a new input preserves the fit. Result 42 reduces the task to an obvious self-equality and the earlier fit. **Use:** it explains why noiseless elimination can retain the target.

### 46. `distinguishing_query_eliminates_rival` — ask where the explanations disagree

**Claim:** if a rival predicts a different label from the truth at an input, adding the truth's label there makes the rival fail exact fit. **Use:** this is the core logic behind a discriminating test. A follow-up task should target predictions that differ, not merely collect more of the same ambiguous response.

### 47. `conflicting_labels_impossible` — a deterministic rule cannot give two unequal answers to one input

**Claim:** if the evidence assigns distinct labels to the same input, no deterministic hypothesis can fit the entire list. Otherwise its one output would equal two unequal labels. **Use:** contradiction can reveal missing context or an unsuitable model class.

### 48. `incorrect_label_excludes_truth` — strict elimination is fragile to error

**Claim:** adding a label unequal to the truth's output makes the truth function fail exact fit. **Use:** this is a reason to treat perfect-label assumptions carefully, including in AI training data and psychological coding.

### 49. `duplicate_evidence_same_models` — copying a list creates no new exact constraint

**Claim:** fitting a list twice is equivalent to fitting it once. Result 43 reduces the claim to the fact that requiring a condition twice adds nothing. **Use:** duplicated records should not be confused with newly informative observations.

**Research implications.** it formalizes what evidence excludes, rather than what a mind experiences while learning. A psychologically richer model would add noise, graded confidence, forgetting, strategy changes, and tests of whether those additions explain behavior.

### F. Collective action — 10 declarations

[Pinned source: CollectiveAction.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/CollectiveAction.lean)

`Feasible` means every required task has a capable group member. `Accepts` means each member's modeled reward covers their modeled cost, relative to a zero outside option. `Ready` requires both. These definitions isolate capability coverage and individual participation. Capacity, scheduling, bargaining, and normative criteria can be introduced as separate layers, creating an explicit mathematical route from interdependence to richer institutional models.

### 50. `adding_members_preserves_feasibility` — existing task coverage survives adding people

**Claim:** a larger group containing a feasible smaller group is feasible. Every earlier capable witness remains available. **Example:** if a team already contains someone for each required role, adding another person does not remove those capabilities in this model.

### 51. `restricting_members_preserves_acceptance` — removing members preserves remaining inequalities

**Claim:** if every member of a larger group has reward at least cost, every member of a subgroup does too. **Use:** acceptance is checked person by person under the same functions.

### 52. `union_accepts_iff` — acceptance over a union decomposes

**Claim:** the union of two groups satisfies the participation inequalities exactly when each group satisfies them. The proof follows whether each member comes from the first group or the second. **Use:** it shows how a property defined pointwise can compose.

### 53. `indispensable_member_withdrawal` — excluding the only possible provider leaves a gap

**Claim:** if any group member capable of a specified task must be one particular person, a group excluding that person cannot cover every task. The proof asks who could perform that task and obtains a contradiction. **Use:** it describes a bottleneck or single point of dependency.

### 54. `complementary_pair_feasible` — two specialists can cover two roles together

**Claim:** in a two-role world, each person can perform exactly the role with their own Boolean label, so the full pair covers both tasks. For each task, choose its matching person. **Use:** it supplies a constructive example of productive complementarity.

### 55. `no_specialist_alone_feasible` — neither role covers the whole system

**Claim:** either specialist alone leaves the other task uncovered. The proof considers which specialist remains and selects the opposite role. **Use:** combined with result 54, it demonstrates a precise kind of interdependence.

### 56. `aggregate_surplus_not_participation` — a good total can conceal a losing participant

**Claim:** costs 1 and 1 with rewards 0 and 3 yield total reward 3 greater than total cost 2, yet `Ready` fails because one person receives less than their cost. **Use:** a proposal described as beneficial overall can still fail an individual participation condition.

### 57. `repaired_allocation_ready` — changing the split can satisfy both constraints

**Claim:** allocate rewards 1 and 2 to the same feasible specialist pair with costs 1 each. Both inequalities now hold, so `Ready` holds. **Use:** it separates generating a surplus from arranging a distribution that meets modeled participation constraints.

### 58. `two_person_budget_iff` — total affordability characterizes existence of an acceptable split

**Claim:** an integer share exists covering A's cost and leaving enough for B exactly when the budget covers their combined costs. If affordable, giving A exactly A's cost constructs a valid split. **Use:** this is a complete necessary-and-sufficient condition for the stated allocation problem.

### 59. `acceptable_share_interval` — characterize every acceptable first share

**Claim:** a particular share satisfies both participation inequalities exactly when it lies between A's cost and `budget − B's cost`. Rearranging B's inequality gives the upper bound. **Example:** costs 2 and 3 with budget 8 allow A's integer share from 2 through 5. **Use:** several allocations may satisfy participation.

**Research implications.** In care coordination, “the service exists,” “someone can perform it,” “the person can access it,” and “the arrangement works for everyone involved” are different questions. The current capability and payoff conditions supply a starting structure. Adding scheduling, transportation, eligibility, and workload would make the representation responsive to more operational questions.

### G. Aggregation — 8 declarations

[Pinned source: Aggregation.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Aggregation.lean)

`Higher` compares natural-number counts by cross multiplication. To interpret it as a rate comparison, denominators must be positive. The concrete example verifies that requirement. The illustration below uses fictional “successes” and does not represent treatment outcomes.

| Context | A | B | Higher rate |
|---|---:|---:|---|
| 1 | 9/10 = 90% | 80/100 = 80% | A |
| 2 | 20/100 = 20% | 1/10 = 10% | A |
| Pooled | 29/110 ≈ 26.36% | 81/110 ≈ 73.64% | B |

### 60. `reversal_cells_valid` — the example contains legitimate counts

**Claim:** each success count is no larger than its denominator, and the denominators 10 and 100 are positive. Lean checks these arithmetic facts. **Use:** the reversal is not an artifact of dividing by zero or having more successes than trials. This is a supporting validation lemma.

### 61. `first_stratum_advantage` — A is ahead in the first context

**Claim:** A's 9 out of 10 exceeds B's 80 out of 100. Cross multiplication compares 900 against 800. **Use:** this establishes one premise of the combined reversal.

### 62. `second_stratum_advantage` — A is ahead in the second context too

**Claim:** A's 20 out of 100 exceeds B's 1 out of 10. The comparison is 200 against 100. **Use:** A's advantage is present in both modeled contexts, not only one.

### 63. `pooled_reversal` — pooling puts B ahead

**Claim:** B's total 81/110 exceeds A's 29/110. A contributes most of its observations from the low-rate context; B contributes most from the high-rate context. **Use:** an aggregate comparison can reverse within-context comparisons.

### 64. `simpson_reversal` — the three comparisons coexist

**Claim:** A's advantage in each context and B's pooled advantage all hold together. The proof packages results 61–63 as a conjunction. **Use:** this is the complete counterexample, making the apparent contradiction inspectable.

### 65. `equal_weight_addition_preserves_order` — consistent unit weighting preserves two inequalities

**Claim:** if `a ≤ b` and `c ≤ d`, then `a + c ≤ b + d` for integers. Arithmetic proves it. **Use:** it contrasts ordinary addition under common unit weights with comparisons whose composition differs.

### 66. `aggregate_cannot_identify_components` — the sum-only ambiguity is reused

**Claim:** observing only the sum does not identify both components of the specified two-component model. The proof directly invokes result 33. **Use:** a result about experimental design also describes information lost through aggregation.

### 67. `recoding_cannot_restore_components` — relabeling a summary cannot recover the lost distinction

**Claim:** any shared recoding of the sum still makes `(1,0)` and `(0,1)` observationally equivalent under the baseline probe. The proof combines the ambiguous pair with postprocessing preservation. **Use:** a more sophisticated representation of the same summary does not supply missing information by itself.

**Research implications.** When evaluating a program, a pooled outcome can change because the cases served changed. Defining the target comparison gives the pooled and context-specific statistics their scientific meaning. The same care applies when comparing model performance across easy and difficult benchmark families.

### What the count means after reading the atlas

The atlas forms seven connected bodies of reasoning. Some results establish a reusable property; some are arithmetic witnesses; some combine or restate earlier results. Their scientific value depends on how they constrain an explanation or improve a decision. `Audit.lean` names the results for dependency checking; it adds no extra social-science theorem to the count.
