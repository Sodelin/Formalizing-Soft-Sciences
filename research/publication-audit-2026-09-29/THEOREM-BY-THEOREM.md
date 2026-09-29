# Every declaration accounted for

Source snapshot: `7835157627548823f03f29dd3987e55601807b55`. All 85 declarations were compared with their formal statements and proofs. Roles below are within-package roles, not counts of discoveries. Exact signatures, assumptions, source hashes and immutable line links are in [JSON](theorem-audit.json) and [CSV](theorem-audit.csv). See [publication judgment](README.md) and [source comparisons](SOURCES.md).

## Solidarity (16)

Question: Project solidarity specification. Specified natural-number path, separate trust/labels, integer one-shot donation payoffs. No empirical behavioral conclusion.

Elementary graph, inclusion and payoff reasoning; original guide N01-N04 give broader formalization precedents.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 1 | [adj_symm](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L14) | support | Symmetry of the successor/predecessor relation; supplies the undirected graph convention. |
| 2 | [reach_trans](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L16) | support | Concatenation is proved by induction on the second path. |
| 3 | [reach_symm](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L21) | support | Path reversal follows from adjacency symmetry and concatenation. |
| 4 | [zero_reaches](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L27) | support | Induction reaches every natural number from zero. |
| 5 | [path_connected](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L32) | endpoint | The natural-number ray is connected; finite paths join every pair. |
| 6 | [at_most_two_neighbors](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L36) | endpoint | Every neighbor is one of a+1 or a-1; this is containment, not a separate degree-cardinality formalization. |
| 7 | [unbounded_reachable](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L43) | endpoint | For every bound, bound+1 supplies a reachable vertex beyond it; no communication-time or human-capacity bound follows. |
| 8 | [membership_nesting](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L50) | consequence | Transitivity of supplied set inclusions; geographic and psychological membership assumptions are not inferred. |
| 9 | [overlapping_memberships](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L55) | witness | Sets {0,1} and {0,2} exhibit shared and exclusive members inside a common population. |
| 10 | [connected_without_trust](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L68) | witness | The trust relation is independently chosen to be empty; the result identifies a missing logical premise. |
| 11 | [cooperation_stable_iff](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L85) | endpoint | The payoff comparison cancels the other player's benefit, leaving cost <= sanction; equality is weak stability. |
| 12 | [no_sanction_failure](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L95) | consequence | Positive cost and zero sanction violate that exact threshold in the specified one-shot payoff model. |
| 13 | [heterogeneous_cooperation_exists](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L102) | witness | Different labels coexist with StableCC 3 1 2 because labels do not enter this payoff function. |
| 14 | [homogeneous_cooperation_can_fail](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L108) | witness | Equal labels coexist with failure of StableCC 3 1 0; the model assigns labels no incentive mechanism. |
| 15 | [symbols_alone_insufficient](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L114) | witness | A constant marker and the same unstable game exhibit the same omitted-mechanism point; not an independent behavioral discovery. |
| 16 | [mutual_gain](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/Solidarity.lean#L120) | consequence | The mutual-contribution payoff exceeds mutual defection when cost < benefit+sanction; this comparison differs from unilateral stability. |

## Identifiability (9)

Question: B01. Exact deterministic predictions and declared parameter/probe spaces; no noisy inference guarantee.

F02 motivates model recovery; the equal-sum witness and cancellation are project examples of established identification reasoning.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 17 | [equivalent_refl](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L13) | support | Reflexivity of equality at every permitted probe. |
| 18 | [equivalent_symm](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L17) | support | Symmetry of equality at every permitted probe. |
| 19 | [equivalent_trans](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L21) | support | Transitivity of equality at every permitted probe. |
| 20 | [restrict_design](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L26) | support | Universal agreement restricts to an included set of probes. |
| 21 | [more_probes_preserve_identification](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L31) | consequence | An injective observation design remains identifying when probes are added. |
| 22 | [postprocess_preserves_equivalence](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L37) | support | A common deterministic function preserves equal outputs; this is the exact information-loss mechanism used later. |
| 23 | [baseline_ambiguous](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L47) | witness | The distinct integer pairs (1,0) and (0,1) have the same sum. |
| 24 | [baseline_not_identified](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L53) | endpoint | The sum observation is non-injective on the declared parameter space; witnessed by the preceding pair. |
| 25 | [both_probes_identify](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Identifiability.lean#L60) | endpoint | The first-coordinate probe plus the sum determines both coordinates by subtraction. |

## Measurement (9)

Question: B02. Unit-loading additive integer indicator, theorem-specific bias premises; no empirical bias bound or construct validation.

F03, scalar-invariance section: intercept equality is an established comparability issue. The repository uses an independently derived integer additive special case.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 26 | [common_intercept_preserves_order](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L8) | consequence | Adding a common integer intercept preserves and reflects order. |
| 27 | [common_intercept_preserves_difference](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L13) | consequence | The common intercept cancels in subtraction. |
| 28 | [shift_invariance](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L18) | support | A latent shift compensated by the opposite intercept shift leaves one response unchanged. |
| 29 | [population_shift_invariance](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L23) | consequence | Function extensionality applies the same compensated shift at every person. |
| 30 | [known_intercept_identifies](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L30) | endpoint | Cancellation identifies a latent value when the intercept is specified and common. |
| 31 | [anchor_identifies_intercept](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L35) | endpoint | Cancellation identifies the intercept from a specified latent anchor. |
| 32 | [group_intercepts_can_reverse_order](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L41) | witness | A concrete bias difference reverses the underlying ordering; it is synthetic arithmetic. |
| 33 | [bounded_bias_interval](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L45) | endpoint | The assumed differential-bias interval translates into a latent-difference interval of the same radius. |
| 34 | [difference_exceeding_bias_identifies_order](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Measurement.lean#L52) | endpoint | Only an upper bound on differential bias is needed for this one-sided sign conclusion. |

## Causality (6)

Question: B03. Treatment equals binary background observationally; effects defined on the complete response function; no probability or general graphical calculus.

F04 sections 1-2 supplies a richer network non-identification predecessor; this deterministic binary example is not its resolution or full formalization.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 35 | [observational_equivalence](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Causality.lean#L23) | witness | Treatment-copy and background-copy models agree when treatment equals background. |
| 36 | [intervention_disagreement](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Causality.lean#L27) | witness | Setting treatment true and background false distinguishes the two models. |
| 37 | [treatment_effect_numerator](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Causality.lean#L30) | support | Enumeration gives effect numerator 2 for the treatment-copy model; the uniform-background average would be 1. |
| 38 | [common_cause_numerator](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Causality.lean#L32) | support | Enumeration gives effect numerator 0 for the background-copy model. |
| 39 | [no_universal_observational_estimator](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Causality.lean#L35) | endpoint | Every estimator of the given observational function fails on at least one candidate with the same observations and a different effect numerator. |
| 40 | [all_responses_identify](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Causality.lean#L47) | endpoint | Agreement at all treatment/background pairs is equality of the complete deterministic outcome function. |

## Learning (9)

Question: B04. Deterministic hypotheses, finite labeled lists and exact consistency; no noise model or statistical generalization bound.

F08 Mitchell version-space reasoning. Related Lean version-space properties also occur in the current Cslib module linked in SOURCES.md.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 41 | [fits_empty](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L9) | support | Universal agreement on an empty evidence list is vacuous. |
| 42 | [fits_cons_iff](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L13) | support | Consistency with a new item splits into its label equation and consistency with the old list. |
| 43 | [fits_append_iff](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L29) | support | Consistency over concatenated lists is conjunction of their consistency constraints. |
| 44 | [more_evidence_narrows_models](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L44) | consequence | Every candidate consistent with the larger list is consistent with an included sublist. |
| 45 | [truth_survives_correct_label](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L49) | consequence | A truth function already fitting the old evidence survives its own correctly labeled observation. |
| 46 | [distinguishing_query_eliminates_rival](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L54) | endpoint | A query at which two hypotheses disagree removes the rival after the truth's label is recorded. |
| 47 | [conflicting_labels_impossible](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L60) | consequence | A deterministic function cannot assign two distinct labels to the same input. |
| 48 | [incorrect_label_excludes_truth](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L67) | consequence | One wrong exact label suffices to remove the truth function from the version space. |
| 49 | [duplicate_evidence_same_models](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Learning.lean#L74) | consequence | Repeating identical constraints does not change exact consistency; this does not model repeated independent noisy measurements. |

## CollectiveAction (10)

Question: B05. Fixed uncongested capabilities, integer transfers without sign constraints, zero outside options; no equilibrium or enforcement process.

Project capability/participation model; established set monotonicity and linear feasibility rather than an external open conjecture.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 50 | [adding_members_preserves_feasibility](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L17) | consequence | Task coverage is monotone when capabilities are fixed and task congestion is absent. |
| 51 | [restricting_members_preserves_acceptance](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L25) | consequence | Removing agents preserves the retained agents' inequalities with unchanged costs and rewards. |
| 52 | [union_accepts_iff](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L30) | support | Universal participation inequalities over a union split into the two groups. |
| 53 | [indispensable_member_withdrawal](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L41) | endpoint | If every capable group member for a task must be the removed agent, the retained group cannot cover that task. |
| 54 | [complementary_pair_feasible](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L52) | witness | Both Boolean specialists together cover the two matching roles. |
| 55 | [no_specialist_alone_feasible](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L56) | witness | One Boolean specialist cannot cover the other role. |
| 56 | [aggregate_surplus_not_participation](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L72) | witness | Total rewards 3 exceed total costs 2 while the agent rewarded zero refuses the stipulated inequality. |
| 57 | [repaired_allocation_ready](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L81) | witness | Rewards (1,2) restore both inequalities while preserving task coverage. |
| 58 | [two_person_budget_iff](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L88) | endpoint | An unrestricted integer transfer exists exactly when total budget covers the sum of costs; share=costA is a witness. |
| 59 | [acceptable_share_interval](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/CollectiveAction.lean#L96) | endpoint | The acceptable first-agent share lies between costA and budget-costB; no bargaining mechanism is supplied. |

## Aggregation (8)

Question: B06. Synthetic positive-denominator counts; no empirical prevalence claim or universal causal adjustment rule.

F09 Simpson (1951), sections 8-11, is historical aggregation context. The strict numerical reversal here is a separately constructed example.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 60 | [reversal_cells_valid](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Aggregation.lean#L10) | integrity | Positive denominators and success counts bounded by sample sizes license the rate interpretation. |
| 61 | [first_stratum_advantage](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Aggregation.lean#L14) | support | Exact cross multiplication verifies 9/10 > 80/100. |
| 62 | [second_stratum_advantage](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Aggregation.lean#L18) | support | Exact cross multiplication verifies 20/100 > 1/10. |
| 63 | [pooled_reversal](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Aggregation.lean#L22) | support | Exact cross multiplication verifies 81/110 > 29/110 after pooling. |
| 64 | [simpson_reversal](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Aggregation.lean#L26) | endpoint | Packages the three comparisons into one checked synthetic aggregation reversal. |
| 65 | [equal_weight_addition_preserves_order](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Aggregation.lean#L32) | consequence | Addition of two integer inequalities; no unequal-rate or causal-adjustment assertion is hidden here. |
| 66 | [aggregate_cannot_identify_components](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Aggregation.lean#L36) | reuse | Direct reuse of baseline_not_identified, not an additional independent non-identification discovery. |
| 67 | [recoding_cannot_restore_components](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/SocialScience/Aggregation.lean#L41) | reuse | Instantiates postprocess_preserves_equivalence with the already checked equal-sum pair. |

## PublishedCBT (14)

Question: Source-derived fragment verification. Spider-present deterministic four-time-point fragment, fixed policy and two danger states; symbolic integer weights. Full inference/learning and clinical efficacy are outside the proof.

Smith, Moutoussis and Bilek (2021), model section/Figure 2, Ineffective CAB interactions, Discussion; upstream CBT_model.m pinned at 82a0a3d.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 68 | [approach_trajectory](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L77) | support | The pinned transition columns generate start, stimulus, approach, interact over four time points. |
| 69 | [avoidance_trajectory](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L80) | support | The pinned avoidance transition columns generate start, stimulus, avoid, safetyCost. |
| 70 | [avoidance_observational_equivalence](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L84) | witness | Safe and dangerous states have identical complete four-modality observations along the declared avoidance trajectory. |
| 71 | [avoidance_no_perfect_classifier](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L88) | endpoint | The identical trajectory cannot be mapped to the correct danger Boolean for both states by any deterministic classifier. |
| 72 | [approach_observations_differ](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L99) | witness | Enumeration finds different observed trajectories under the two states when approach is fixed. |
| 73 | [approach_identifies_state](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L103) | endpoint | Among these two latent states, equality of the complete fixed approach observations forces equality of the states. |
| 74 | [safe_columns_total_mass](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L108) | integrity | Each reconstructed safe weight column sums to 10*u algebraically, for all integer u,c. |
| 75 | [danger_columns_total_mass](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L112) | integrity | Each reconstructed danger weight column sums to 10*u algebraically, for every integer u. |
| 76 | [safe_columns_nonnegative](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L116) | integrity | Positive u and 0 <= c <= 10*u make every component of the safe weights nonnegative. |
| 77 | [danger_columns_nonnegative](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L121) | integrity | Positive u makes every component of the fixed danger weights nonnegative. |
| 78 | [implicit_mappings_equal_at_tenth](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L126) | consequence | Putting c=u makes both symbolic implicit mappings identical at every phase; u>0 supplies the CABi=0.1 interpretation. |
| 79 | [approach_implicit_equality_iff](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L131) | endpoint | Equality of the approach weight columns holds iff c=u; the algebraic theorem has no positivity premise, while its normalized parameter interpretation needs u>0. |
| 80 | [avoidance_implicit_columns_equal](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L141) | consequence | Both avoidance-phase implicit columns ignore c and the safe/danger label in this fragment. |
| 81 | [explicit_prior_weights](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/PublishedCBT.lean#L147) | integrity | The two unnormalized prior weights are nonnegative and sum to scale under the specified bounds; normalization is an interpretation. |

## SourceBridge (4)

Question: Source transcription correspondence. Bounded extraction and scaling bridge; no proof of MATLAB/SPM semantics, complete upstream simulation or model selection.

Pinned upstream MATLAB tables extracted without execution, followed by Lean equality checks; source_bridge.py specifies ten matrices and six guards.

| # | Declaration | Role | Audited contribution |
|---|---|---|---|
| 82 | [source_sensory_columns](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/SourceBridge.lean#L26) | integrity | All six phases match the four selected upstream spider/arousal matrices column by column. |
| 83 | [source_affective_columns](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/SourceBridge.lean#L33) | integrity | All six phases match the selected upstream safe/danger affect matrices column by column. |
| 84 | [source_transition_columns](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/SourceBridge.lean#L38) | integrity | Both reconstructed transition functions match all columns of the selected upstream transition matrices. |
| 85 | [source_implicit_columns](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/7835157627548823f03f29dd3987e55601807b55/clinical/ClinicalModels/SourceBridge.lean#L43) | integrity | Both symbolic weight functions match every selected upstream implicit column after the explicit scaling translation. |

