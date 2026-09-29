# Abstract

A second measurement can separate explanations that a million repetitions of the first would leave tied. A proof can establish why, identify the needed information, and preserve the argument in a form that another researcher or computer can check. This monograph develops that scientific opportunity through a library of 67 Lean theorem declarations spanning network reach, measurement, identifiability, causality, learning, collective action, and aggregation. It expands the earlier project reader's guide into a sustained account of the definitions, lemmas, counterexamples, and research choices behind the development. The contribution is an integrated, inspectable research artifact and a program for connecting verified consequences to better questions, measurements, and experiments. The models are minimal mathematical representations that isolate relationships and support increasingly rich extensions. A complete source audit confirmed declaration coverage and a successful verification run at a fixed commit. A targeted literature map locates the work across psychology, biology, sociology, anthropology, normative reasoning, and AI theorem proving. Detailed worked arguments lead to a proposed evaluation of whether paired proofs and explanations improve scientific reasoning in AI systems. The resulting framework joins mathematical precision with an open-ended empirical program.

*Keywords:* mathematical psychology, formal verification, Lean, social science, artificial intelligence

# Introduction — the Scientific Opportunity

Two explanations fit every observation. More computation cannot choose between them because the distinction is absent from the information supplied. Then a researcher asks one different question, and the tie breaks. The crucial advance was a better observation. Formal reasoning can show exactly why it worked.

This is the promise of the development examined here. It creates an integrated library in which familiar scientific questions acquire precise mathematical form and checkable answers. The collection's seven modules can be inspected separately and understood together. Definitions, proofs, counterexamples, and source provenance give researchers common objects around which to disagree, revise, and build.

The work is new as a connected project artifact: this implementation, its explanatory map, and its verified path from assumptions to consequences. Its intellectual setting is an established tradition of mathematical and computational inquiry. That tradition supplies tools with which the present library can become a more capable research instrument.

The project connects a psychological question—how people think, judge, learn, and coordinate—to a mathematical question: **what follows from the explanation once we write it precisely?** The strength of that connection comes from making each stage explicit: the intended meaning, its mathematical representation, the consequence, and the observations that can test its use.

Consider the sentence, “Shared identity makes people cooperate.” It might mean that identity changes preferences, changes expectations of others, increases encounters, supplies a common signal, or makes sanctions more credible. Each interpretation suggests a different model. Formalization turns those interpretations into distinct mechanisms that can be compared.

The project currently supplies a vocabulary for asking sharper questions. Can an observation distinguish two mechanisms? Does a score difference survive measurement bias? Does a group have the skills required for a task? Does every necessary participant have an incentive to participate? Could a pooled statistic reverse the within-context comparisons? These are methodological foundations with applications to psychology and society.

Together, these minimal representations provide a basis for increasingly rich accounts of cognition and social organization. They isolate mechanisms, make their consequences exact, and identify the observations needed to connect them with research.

## Three Meanings of “formalization”

| Meaning | What the researcher produces | What it can establish |
|---|---|---|
| Mathematical specification | Equations, sets, relations, probability distributions, or explicit rules | An unambiguous model and deductions, assuming the mathematics is correct |
| Executable computational model | A program that generates predictions or simulates processes | Behavior of the implemented model under examined conditions |
| Machine-checked formal verification | A formal statement plus a proof accepted by a proof assistant, or a property checked by a model checker | That the specified property follows within the formal system and its trust boundary |

Table: Three Complementary Forms of Formalization

These activities complement one another. Mathematics specifies the relationships; execution reveals behavior under selected conditions; verification establishes formally stated properties. A research program can combine all three with empirical evaluation. The disciplinary examples below show the breadth of mathematical modeling and the more specialized role of proof assistants.

## Verification and Validation Answer Different Questions

**Verification** asks whether the stated mathematical or computational object satisfies its specification. **Validation** asks whether that representation is adequate for its intended use in the world. Measurement validation is a further bridge: does the observation actually track the intended construct?

A model earns its role relative to a purpose. Predicting the next choice, explaining how learning occurs, and selecting an intervention place different demands on the same representation. Verification secures the deductive step, while validation investigates how that step serves the intended scientific use. Stating both tasks makes the research program stronger and easier to evaluate.

# Method and Provenance

## What Was Inspected

The source of truth for the theorem explanations is [Formalizing Soft Sciences at commit 780f1b8](https://github.com/Sodelin/Formalizing-Soft-Sciences/tree/780f1b83aef15a9cf455566bab9df2a47d738074). The audit examined `Solidarity.lean`, all six foundation modules, `SocialScience/Audit.lean`, the CI workflow, the verification receipt, and the foundation bibliography. The complete earlier book, *How We Formalized Questions About Society*, was recovered as the baseline for this expanded edition. Its narrative, theorem guide, research register, and source appendix were examined alongside the pinned code.

The public proof files contain 67 `theorem` declarations. The audit names all 67. The current main-commit workflow reports success. Earlier documentation cites run 36391937036; that run also succeeded, but it belongs to commit a0663d5de45872ca4531067a886928f59ca48e61. This report uses the later main-commit receipt to avoid treating two commits as the same object.

The repository workflow rejects `sorry`, `admit`, custom `axiom` declarations, and `native_decide` in the project sources, runs the Lean build and axiom audit, and checks documentation/provenance. The recorded dependencies are standard Lean axioms or no axioms. Such logical axioms differ from substantive modeling assumptions: defining payoffs to ignore identity is a modeling choice even when no custom logical axiom is present. (Lean Project, n.d.; Sodelin, 2026)

## Literature Search

Searches were conducted on 28 September 2026. They combined targeted web queries with direct primary-source retrieval. Topics included the Society for Mathematical Psychology, computational model recovery, formalization of psychological theories, biological model checking, Lean voting theory, kinship algebra, deontic reasoning, and Lean-based AI training. The accompanying search log records the query groups, source selection, and material access failures.

Included evidence had to establish a directly relevant precedent, explain a methodological distinction, or support the AI-training discussion. Primary papers, author-hosted papers, research repositories, and official documentation were preferred. Promotional claims, unrelated search hits, and unverified priority claims were excluded from the synthesis. Some sources were available only as abstracts; their use is restricted accordingly in the bibliography.

The method is a source audit combined with a targeted narrative evidence map. The audited objects are definitions, theorem declarations, dependencies, and verification records. The literature component establishes selected precedents and informs a proposed research program. Search completeness and access depth are assessed in the process review and source register.

# Mathematical and Computational Approaches

## What Mathematical Psychology Does

Mathematical psychology constructs precise accounts of psychological phenomena and investigates their consequences. The Society for Mathematical Psychology explicitly includes mathematical methods, formal logic, and simulation within its scope. Its journals and recurring conferences demonstrate an established research community. (Society for Mathematical Psychology, n.d.)

Examples of its questions include: how choice probabilities depend on preferences; how evidence accumulates before a decision; how learning changes with feedback; whether a measurement scale preserves comparisons; and how confidence relates to accuracy. Mathematics can reveal relationships that are hard to see in verbal descriptions, including parameter tradeoffs and cases where rival explanations make the same prediction.

Here is an illustrative learning equation:

`Q(next) = Q(now) + alpha × (outcome − Q(now))`

The variable `Q` represents an expectation, and `alpha` controls how much it moves toward the observed outcome. If `alpha = 0`, the expectation does not change. If `alpha = 1`, it becomes the latest outcome. Values between zero and one yield a weighted average. These exact consequences identify what the equation predicts and give empirical researchers properties to investigate.

A mathematical investigation could ask whether the expectation remains bounded or converges under particular input sequences. A psychological investigation would additionally ask whether this update rule explains actual behavior better than alternatives and whether the fitted parameter has the interpretation claimed.

## What Computational Psychology Does

Computational psychology emphasizes explicit information-processing mechanisms and executable models: rules that perceive, remember, infer, choose, and learn. It overlaps heavily with mathematical psychology. The difference is an emphasis, not a rigid border. Some models are compact equations; others are simulations, cognitive architectures, neural networks, or symbolic programs.

A useful distinction concerns **modeling a theory** versus **fitting a description of data**. A regression may describe how two variables co-vary without specifying the process producing the relationship. A generative cognitive model specifies a process that could produce responses, errors, or reaction times. Competing generative models can fit similar observations, making model comparison and design central to the investigation. Guest and Martin argue that computational implementation strengthens theory building by requiring researchers to make otherwise implicit commitments explicit. (Guest & Martin, 2021)

For a typical study, researchers define competing mechanisms, simulate their predictions, collect behavior, fit parameters, check whether parameters and model identities can be recovered, and evaluate predictions beyond the fitting data. Wilson and Collins provide a practical guide to careful use of behavioral models, including recovery checks. These checks connect the behavior of the implementation to the interpretation of its fitted parameters. (Wilson & Collins, 2019)

## Neighboring Approaches

| Approach | Central question | Relationship to the current release |
|---|---|---|
| Psychometrics | What does a score measure, and are comparisons meaningful? | The additive measurement examples isolate which comparisons survive common and differential offsets. |
| Computational cognitive science | Which processes generate behavior? | The learning module tracks which deterministic hypotheses remain compatible with specified evidence. |
| Computational psychiatry | Can mechanistic models and predictive data analysis improve understanding of psychiatric phenomena? | A future application linking formal properties to a specified mechanism and clinical evidence. |
| Computational social science | How do interaction rules, networks, institutions, and data explain social patterns? | Solidarity and collective-action modules separate network structure, capability, and participation. |
| Formal methods | Does a precisely specified system possess a stated property? | This is the project's most direct present contribution. |

Table: Neighboring Research Approaches and Their Connection to the Library

Computational psychiatry includes both data-driven prediction and theory-driven modeling of interpretable processes. Huys, Maia, and Frank describe their relationship and the challenges of translating between levels. This provides a research setting in which formal properties can be connected to mechanistic questions and assessed against clinical evidence. (Huys et al., 2016)

## Is This Widespread Across Disciplines?

**Mathematical and computational approaches have established traditions across biology, psychology, sociology, anthropology, and comparative cultural research. Proof assistants such as Lean contribute a specialized form of assurance within that landscape.** The following evidence map shows what each approach makes possible. It documents examples rather than estimating disciplinary adoption rates.

| Field | Established kinds of modeling | Direct precedent found | Scientific opportunity illustrated |
|---|---|---|---|
| Biology | Dynamical systems, stochastic processes, population and biochemical models | Heath and colleagues used PRISM to analyze a model of FGF signaling. (Heath et al., 2008) | Analyze temporal and probabilistic properties of a specified pathway |
| Psychology | Mathematical cognition, psychometrics, learning and decision models | Finkel, Fougea, and Le Roux formalized a stress theory using automata. (Finkel et al., 2025) | Translate a verbal process theory into explicit states and transitions |
| Sociology and related social theory | Networks, agent-based models, games, and institutional rules | Axelrod modeled cultural influence; Holliday and colleagues formalized voting properties in Lean. (Axelrod, 1997; Holliday et al., 2021) | Connect local rules to collective patterns and verify properties of decision procedures |
| Anthropology | Formal kinship, cultural transmission, archaeological and social simulation | Read, Fischer, and Leaf described computational algebraic analysis of kinship terminology. (Read et al., 2013) | Study the internal structure of culturally interpreted symbolic relations |
| Ethnology / comparative cultural research | Comparison of cultural patterns, coding and sampling frameworks, sometimes formal and computational models | HRAF's methods materials address comparative sampling and dependence between societies. (Human Relations Area Files, n.d.) | Design comparisons with explicit sampling and dependence assumptions |

Table: Formal Approaches Across Biological and Social Disciplines

Ethnology often refers to comparative study across cultures, while ethnography typically involves situated description and interpretation. Usage varies across national academic traditions. Formal comparison and situated interpretation can contribute to a shared investigation.

The biology example is especially informative: probabilistic model checking examines formally specified system behavior, sometimes using exact or approximate numerical techniques. Its guarantees differ from a general theorem proved in Lean. The two methods offer complementary forms of assurance whose scope follows their stated mathematical guarantees. (Heath et al., 2008)

Kinship algebra makes the prospect of formalizing social concepts especially tangible. Relations can be composed and their internal rules investigated. Ethnographic interpretation establishes which local categories the relations represent; the algebra then makes their implications available for systematic analysis. (Read et al., 2013)

## Why Isn't Everything Written in Lean?

Several obstacles concern the scientific task itself; others concern implementation and incentives. The following is a synthesis and assessment, not a measured causal ranking of adoption barriers.

**Constructs are contestable.** The meanings of intelligence, trust, distress, solidarity, or fairness can change with theoretical commitments and practical aims. Formalization exposes that choice but cannot make it disappear. Competing formalizations may be useful because they reveal exactly where interpretations diverge.

**The observation process is part of the problem.** A score is shaped by an instrument, context, interpretation, and measurement error. Proving a relationship among latent variables does not prove that questionnaire responses instantiate it. The measurement module makes this issue visible even with simple integer arithmetic.

**Identification can fail before estimation begins.** Different mechanisms may produce the same observations. More participants reduce some sampling uncertainty; they do not automatically repair structural ambiguity. The identifiability and causality modules show exact versions of this problem. Network-specific research gives richer examples involving homophily and social influence. (Shalizi & Thomas, 2011)

**Systems change.** People respond to institutions, labels, incentives, and one another. A model useful in one time or community may fail elsewhere. Heterogeneity may be scientifically substantive rather than noise to average away.

**The cost must match the research risk.** Formal proof requires precise definitions, mathematical libraries, tool expertise, maintenance, and review. Sometimes a simulation, a standard analytic argument, or a better experiment resolves the key uncertainty more efficiently. Lean is especially valuable when a reusable result, subtle inference, or consequential algorithm needs strong assurance.

**Qualitative evidence does different work.** Interviews, ethnography, archival interpretation, and participatory inquiry can identify categories and mechanisms that a model has omitted. They can improve formalization by revealing that the specified question was wrong. Precision is useful when it preserves the distinctions the research needs.

**Empirical and normative questions remain.** A proof that a policy meets a chosen fairness criterion does not establish that this criterion should govern a particular institution. A proof of logical consistency does not resolve whose interests, histories, or values should shape the rules.

## How to Formalize a Psychological or Social Claim

The following sequence makes the work concrete.

1. **Choose a bounded question.** For example: “Can two different explanations of confidence generate the same reported confidence score?” This is more actionable than “Formalize metacognition.”
2. **Specify the interpretation.** State what each variable represents and how it could be observed. Separate confidence level, discrimination of correct from incorrect responses, and task performance. These distinctions matter in established metacognition measurement. (Fleming & Lau, 2014)
3. **Specify the domain.** Are variables integers, real numbers, finite states, probabilities, or time series? Does the model describe one person, a population, or an institution?
4. **Separate definitions from assumptions.** “An accepted allocation covers each modeled cost” can be a definition. “People participate whenever costs are covered” is an empirical behavioral assumption if applied to real people.
5. **Construct competing models.** An informative proof often compares alternatives rather than only deriving properties of a favored model.
6. **Write the claim and its quantifiers.** “There exists a cooperative heterogeneous pair” differs greatly from “all heterogeneous groups cooperate.”
7. **Search for a counterexample.** Vary omitted factors, boundary values, and the observation design. A counterexample can reveal a false universal claim or an overly weak specification.
8. **Prove the claim in Lean.** Encode the objects, assumptions, and conclusion; construct a proof; and check its dependencies and reproducible build.
9. **Review the translation back to prose.** Read every definition. Ask whether the formal claim actually matches the psychological or social sentence.
10. **Test the empirical bridge.** Simulate realistic noise, examine parameter/model recovery, fit data if appropriate, test held-out predictions, and investigate setting-specific failures.

### A Complete Miniature Example from the Verified Source

The measurement module defines `response latent intercept = latent + intercept`. One actual theorem is:

```lean
theorem common_intercept_preserves_difference (a b intercept : Int) :
    response a intercept - response b intercept = a - b := by
  simp only [response]
  omega
```

In plain language, subtracting two scores removes an offset that is identical for both. If the latent values are 7 and 4, and both scores add 3, the observed difference is `10 − 7 = 3`, exactly the latent difference `7 − 4 = 3`.

`Int` specifies integers. `response` supplies the model. The line after the colon is the claim. `simp only [response]` exposes the definition, and `omega` supplies an arithmetic proof that Lean checks. The successful proof covers all integer inputs to that statement.

The scientific question begins where the proof ends: **do the two observations actually share this additive offset?** If different groups use a scale differently, the theorem's common-offset condition may fail. The nearby counterexample and bounded-bias theorem address precisely that issue. (Sodelin, 2026)

### From a Therapy Narrative to a Research Model

For a future cognitive behavioral therapy (CBT) research project, a model could represent expectations, observations, avoidance choices, and belief updates. A proof could establish that an update stays within bounds, that a task leaves two mechanisms tied, or that a new observation can separate them. The next investigation would connect those mechanisms to measured behavior and intervention outcomes. This sequence turns a broad clinical narrative into a series of answerable research questions.

A psychopathology model could similarly represent interactions among processes or symptoms. Its parameters would acquire substantive interpretations through measurement and model comparison. The value of formalization would be the clearer link between a proposed mechanism, its mathematical behavior, and the evidence needed to assess it.


# The Complete Atlas of 67 Theorems

This atlas expands the shorter tables in *How We Formalized Questions About Society*. Each entry gives the actual declaration name, its mathematical content, the proof idea, and the scientific question it makes clearer. The source for all 67 entries is the pinned project release (Sodelin, 2026); the earlier guide provides the narrative baseline (Formalizing Soft Sciences Project, 2026). The numbering is a reading order used in this edition; Lean identifies results by their namespace and name.

The atlas can be read in two directions. The network section follows the original question of how cooperation extends beyond direct acquaintance. Readers interested in psychological methodology can begin with measurement (17–25), identifiability (26–34), and causality (35–40), then connect those results to learning and aggregation.

Numerical examples are synthetic constructions chosen to make the mathematical relationships transparent. Proof-method descriptions are explanations of the inspected source, not additional proofs created for this edition.

## Solidarity — 16 Declarations

[Pinned source: Solidarity.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/Solidarity.lean)

The network uses natural-number labels: 0, 1, 2, and onward. Two labels are adjacent when they differ by one. `Reach` means there is a finite chain of these links. Membership is a predicate, trust is a separate relation, and the final six results concern a two-person donation game. The module deliberately keeps these meanings separate. Its network is undirected and has no travel cost. Its labels and trust relation are independent of the payoff mechanism, allowing logical relationships between those concepts to be examined directly.

### 01. `adj_symm` — a Direct Link Goes Both Ways

**Claim:** if A is adjacent to B, B is adjacent to A. **Why:** the definition allows either number to be one greater than the other; exchanging the two alternatives proves symmetry. **Use:** this establishes that the example is an undirected network. It is a supporting lemma for later path proofs.

### 02. `reach_trans` — Two Routes Can Be Joined

**Claim:** if A can reach B and B can reach C, A can reach C. The proof follows the second route step by step and extends the first route. **Example:** a referral chain from one service to another can be concatenated with a further chain as a graph-theoretic possibility.

### 03. `reach_symm` — a Route Can Be Reversed

**Claim:** any finite path can be followed in the opposite direction. The proof uses symmetric adjacency and route concatenation. **Use:** it turns routes from the starting vertex into routes back to it, enabling the general connectivity proof.

### 04. `zero_reaches` — Every Numbered Position Is Reachable from Zero

**Claim:** for any natural number `n`, vertex 0 reaches vertex `n`. The proof is induction: 0 reaches itself, and a route to `n` extends one step to `n + 1`. **Intuition:** a finite trip can reach any particular point along an indefinitely extended chain.

### 05. `path_connected` — Any Two Vertices Are Connected

**Claim:** every A reaches every B. The proof goes from A back to 0 and from 0 to B. **Use:** this is the main connectivity result for the example. It shows that a network's global extent need not equal the number of people directly known by one member.

### 06. `at_most_two_neighbors` — Local Contact Is Tightly Bounded

**Claim:** if B is adjacent to A, B must be `A + 1` or `A − 1`. The formal result gives an explicit two-candidate bound on adjacent labels. At vertex 0 there is only one actual adjacent vertex. **Use:** paired with global reach, this separates local and global structure.

### 07. `unbounded_reachable` — Bounded Local Contact Permits Unbounded Reach

**Claim:** for any proposed numerical bound, some larger numbered vertex remains reachable from 0. Choose the next number and apply result 04. Together with result 06, it gives a counterexample to the claim that bounded direct contacts necessarily bound an entire connected population.

### 08. `membership_nesting` — Inclusion Is Transitive

**Claim:** if every A-member belongs to B and every B-member belongs to C, every A-member belongs to C. The proof composes the two inclusion assumptions. **Example:** if a study's recruitment strata genuinely nest inside its sampling frame, the resulting inclusion follows.

### 09. `overlapping_memberships` — Groups Can Overlap Without Being Identical

**Claim:** there exist groups with a shared member and an exclusive member on each side, all within one population. The witnesses are A = {0,1}, B = {0,2}, with the common population containing every natural number. **Use:** this permits multiple intersecting memberships. It is a logical basis for representing someone as a researcher, musician, and community member.

### 10. `connected_without_trust` — a Connection Does Not Entail Trust

**Claim:** a connected network can coexist with a trust relation in which person 0 does not trust person 1. The proof chooses a relation that is false everywhere; the stated conclusion only requires that particular missing trust relation. **Use:** it blocks the inference from network connectivity alone to trust.

### 11. `cooperation_stable_iff` — the Exact Incentive Threshold

**Claim:** mutual contribution resists a unilateral payoff-improving deviation exactly when contribution cost is no larger than the defection sanction. If the other person contributes, contributing pays `benefit − cost`; defecting pays `benefit − sanction`. The benefit cancels. **Example:** benefit 3, cost 1, sanction 2 gives payoffs 2 versus 1.

### 12. `no_sanction_failure` — Removing the Sanction Changes This Game's Incentive

**Claim:** when contribution has strictly positive cost and sanction is zero, mutual contribution fails the defined stability test. Result 11 would require a positive cost to be no greater than zero, a contradiction. **Use:** it isolates which term sustains the equilibrium in this payoff specification.

### 13. `heterogeneous_cooperation_exists` — Different Labels Can Coexist with Stable Cooperation

**Claim:** two players can receive different Boolean labels while mutual contribution is stable at benefit 3, cost 1, sanction 2. The proof assigns different labels and invokes the threshold theorem. **Use:** it defeats an unrestricted claim that identical labels are logically necessary for cooperation.

### 14. `homogeneous_cooperation_can_fail` — Identical Labels Do Not Guarantee Cooperation

**Claim:** two players can share a label while mutual contribution is unstable at benefit 3, cost 1, sanction 0. The proof gives both the same label and applies result 12. **Use:** similarity and incentives are separate ingredients in this vocabulary.

### 15. `symbols_alone_insufficient` — a Shared Marker Changes Nothing If It Changes No Mechanism

**Claim:** two players can share marker 7 and still face the unstable game with positive cost and no sanction. **Use:** this makes a research question visible: through which causal route would a symbol matter—expectations, preferences, coordination, or enforcement?

### 16. `mutual_gain` — Both Can Do Better Under Mutual Contribution

**Claim:** if `cost < benefit + sanction`, the payoff under mutual contribution exceeds the payoff under mutual defection. These are `benefit − cost` and `−sanction`, respectively. Algebra gives the stated inequality. **Use:** it separates a comparison of outcomes from an incentive to reach or maintain an outcome.

**Research implications.** Two people can share a social marker without trusting one another; trust can exist without a profitable action; a profitable joint outcome can exist without individual incentives to maintain it. Those distinctions are the reusable achievement. A richer theory of identity can now specify how labels affect expectations, payoffs, or the network itself.

## Measurement — 9 Declarations

[Pinned source: Measurement.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Measurement.lean)

The entire module uses `response = latent + intercept`, with integer values, loading one, and no random error. One psychological interpretation concerns the distinction between an underlying judgment process and response-scale use. That interpretation suggests measurements through which the model can be developed.

### 17. `common_intercept_preserves_order` — a Shared Offset Preserves Ranking

**Claim:** with the same intercept, A's response is no larger than B's exactly when A's latent value is no larger than B's. The proof cancels the shared addition. **Example:** adding 20 to both 40 and 60 keeps their order. **Use:** it identifies one sufficient measurement condition for ranking comparisons.

### 18. `common_intercept_preserves_difference` — a Shared Offset Preserves the Gap

**Claim:** subtracting the two responses gives exactly the latent difference when their intercepts match. **Example:** latent scores 7 and 4 become 10 and 7 after adding 3; the gap remains 3. **Use:** change or group comparisons can be robust to a common additive offset.

### 19. `shift_invariance` — the Origin Can Move Without Changing an Observation

**Claim:** adding any shift to a latent score and subtracting the same shift from the intercept preserves the response. **Example:** latent 4 plus intercept 3 and latent 6 plus intercept 1 both produce 7. **Use:** a single observed sum cannot fix the absolute origin of both components.

### 20. `population_shift_invariance` — More People Do Not Automatically Fix the Origin

**Claim:** shifting every person's latent value by the same amount and compensating in the shared intercept preserves the entire response function. The proof applies result 19 to every person and then uses equality of functions. **Use:** increasing sample size alone cannot remove this structural ambiguity.

### 21. `known_intercept_identifies` — a Fixed Intercept Removes One Ambiguity

**Claim:** two latent values with the same specified intercept must be equal if their responses are equal. Cancellation proves it. **Use:** once the intercept is fixed, the response mapping is injective in the latent value.

### 22. `anchor_identifies_intercept` — a Fixed Latent Anchor Can Calibrate an Offset

**Claim:** if two intercepts produce the same response for the same latent anchor, the intercepts are equal. The anchor cancels. **Use:** an independently grounded reference can distinguish offsets in this model.

### 23. `group_intercepts_can_reverse_order` — Measurement Differences Can Reverse a Comparison

**Claim:** although latent 0 is below latent 1, response 0 with intercept 2 exceeds response 1 with intercept 0. Lean checks the concrete arithmetic. **Use:** apparent ordering of scores need not equal ordering of the latent values. In a judgments-of-learning (JOL) study, a difference in scale use is one possible rival explanation worth assessing.

### 24. `bounded_bias_interval` — Turn a Bias Assumption into a Sensitivity Interval

**Claim:** if the intercept difference is between `−delta` and `delta`, the latent difference lies between `observed difference − delta` and `observed difference + delta`. **Example:** observed gap 5 and bias bound 2 imply a latent gap from 3 to 7. **Use:** state how large differential bias must be to change an interpretation.

### 25. `difference_exceeding_bias_identifies_order` — a Sufficiently Large Gap Fixes the Sign

**Claim:** if differential bias has an upper bound `delta` and the observed A-minus-B gap exceeds it, A's latent value exceeds B's. Only the relevant one-sided bias bound is needed. **Example:** a gap of 5 with an upper bias bound of 2 leaves a positive latent difference.

**Research implications.** An ANOVA or ANCOVA can estimate a response difference under its statistical assumptions. This module asks a prior interpretive question: what does that response difference say about the underlying construct? Neither analysis replaces the other.

## Identifiability — 9 Declarations

[Pinned source: Identifiability.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Identifiability.lean)

A candidate predicts an exact output for each possible probe. A design chooses the allowed probes. Larger probe sets preserve exact identifying information; finite noisy estimation introduces a further question of precision. `Equivalent` means two candidates agree on every allowed probe. `Identified` means such agreement forces the candidates to be equal. This exact notion of structural information provides the foundation on which a finite-data recovery analysis can be built.

### 26. `equivalent_refl` — a Candidate Agrees with Itself

**Claim:** any candidate is observationally equivalent to itself under any design. Its prediction equals itself at each permitted probe. **Use:** this is the reflexivity component of treating observational indistinguishability as an equivalence relation. Together with the next two lemmas, it supplies the equivalence structure used to reason about whole classes of explanations.

### 27. `equivalent_symm` — Indistinguishability Goes Both Ways

**Claim:** if A and B make equal predictions on the design, B and A do too. The proof reverses each equality. **Use:** the model does not privilege one explanation merely because its name appears first.

### 28. `equivalent_trans` — Chains of Exact Agreement Remain Equivalent

**Claim:** if A agrees with B and B agrees with C on all allowed probes, A agrees with C. The proof composes equalities. **Use:** whole families of candidates can be grouped by what the design can distinguish.

### 29. `restrict_design` — Discarding Probes Cannot Distinguish Previously Identical Predictions

**Claim:** candidates equivalent on a larger probe set remain equivalent on any included smaller set. Every smaller-set probe already belongs to the larger set. **Use:** dropping an informative task cannot create structural distinctions that were absent before.

### 30. `more_probes_preserve_identification` — Adding Exact Probes Retains Existing Identification

**Claim:** if a smaller design already identifies every candidate in the class, a larger design containing it also does. Agreement on the larger design implies agreement on the smaller one, which already forces equality. **Use:** a useful probe need not be discarded when adding another.

### 31. `postprocess_preserves_equivalence` — Recoding Identical Outputs Cannot Create Information

**Claim:** applying the same function to identical outputs leaves them identical. **Example:** if two mechanisms both produce 1, converting that score to a category, embedding, or deterministic summary still gives the same transformed result. **Use:** better downstream computation cannot recover a distinction absent from the input.

### 32. `baseline_ambiguous` — a Sum Admits Distinct Explanations

**Claim:** when the only probe observes the sum, components `(1,0)` and `(0,1)` both produce 1. **Interpretive example:** a response influenced by familiarity and another social cue could look identical under different combinations. The actual components are just integers. **Use:** one constructive witness can expose an ambiguous design.

### 33. `baseline_not_identified` — No Exact Recovery of Both Components from This Design

**Claim:** the sum-only design does not identify arbitrary integer pairs. If it did, the two distinct pairs from result 32 would have to be equal, implying `1 = 0`. **Use:** the problem is not merely a small sample or a weak estimator; the observation map loses a distinction.

### 34. `both_probes_identify` — a Discriminating Second Observation Resolves the Example

**Claim:** observing both the first component and the total identifies the ordered pair. Equality of first-component outputs fixes the first component; equality of totals then fixes the second. **Example:** total 7 and first component 3 determine second component 4. **Use:** design a measurement to separate explanations before collecting a large dataset.

**Research implications.** A warmth/competence and judgments-of-learning study can ask which rival psychological explanations predict the same observed pattern, then select a task or manipulation that separates them. The model turns an intuitive mechanism question into a design question.

## Causality — 6 Declarations

[Pinned source: Causality.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Causality.lean)

There is a binary background `U`, treatment `T`, and outcome `Y`. Observed assignment makes `T = U`. In one model, `Y = T`; in the other, `Y = U`. The observational object is an exact mapping, and an effect numerator adds treatment contrasts across both background values. Probability distributions and division are not implemented.

### 35. `observational_equivalence` — the Two Causal Stories Produce the Same Observed Mapping

**Claim:** both models return `(U,U)` for the observed treatment–outcome pair. The proof establishes function equality by checking an arbitrary background value. **Use:** even perfect observation of this assignment pattern cannot distinguish the two mechanisms.

### 36. `intervention_disagreement` — Forcing Treatment Separates the Stories

**Claim:** set treatment to true while background is false: the treatment-driven model returns true, whereas the background-driven model returns false. Lean checks this Boolean inequality directly. **Use:** an intervention can probe combinations that the observational assignment never produces.

### 37. `treatment_effect_numerator` — the Treatment-driven Model Has Numerator Two

**Claim:** the sum of outcomes under treatment across both backgrounds minus the corresponding untreated sum is 2. Both background-specific treatment contrasts equal 1. **Interpretation:** if the two backgrounds are equally weighted, the average effect would be 1.

### 38. `common_cause_numerator` — the Background-driven Model Has Numerator Zero

**Claim:** the same effect numerator is 0 when the outcome copies background and ignores treatment. Holding background fixed, changing treatment changes nothing. **Use:** results 37 and 38 supply the distinct correct answers needed for the impossibility proof.

### 39. `no_universal_observational_estimator` — Equal Inputs Cannot Yield Two Different Correct Effects

**Claim:** no function taking only the specified observational mapping can return the correct effect numerator for every binary model. Results 35, 37, and 38 force a contradiction: the estimator receives the same input but would need to return both 2 and 0. **Use:** it identifies an information limit shared by all estimators in the defined class.

### 40. `all_responses_identify` — a Complete Exact Response Table Fixes This Model

**Claim:** if two models agree at every treatment/background combination, their outcome functions—and therefore their model structures—are equal. Function equality supplies the proof. **Use:** it identifies sufficient information at the far end of the spectrum from the incomplete observational design.

**Research implications.** A model of why a therapy works needs more than reproducing a before-and-after association. The formal question is which assumptions and observations distinguish a treatment mechanism from alternative causes. Intervention-outcome evidence can then evaluate the treatment claim while the formal analysis clarifies what mechanism has been identified.

## Learning — 9 Declarations

[Pinned source: Learning.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Learning.lean)

`Fits` means a deterministic hypothesis agrees with every input–label pair in a finite evidence list. The module formalizes consistency constraints on candidate explanations. Probabilistic labels, memory, and graded confidence provide natural extensions beyond this deterministic starting point.

### 41. `fits_empty` — No Observations Exclude No Hypotheses

**Claim:** every hypothesis fits an empty evidence list. There is no listed example on which it can disagree. **Use:** this exposes the difference between consistency and evidential support: with no constraints, even a bad hypothesis fits.

### 42. `fits_cons_iff` — One New Example Adds One Exact Constraint

**Claim:** a hypothesis fits a new labeled example followed by the old evidence exactly when it matches the new label and fits the old list. The proof separates membership in the new head from membership in the old tail. **Use:** this is the logical structure of sequential elimination.

### 43. `fits_append_iff` — Fitting Combined Evidence Means Fitting Both Parts

**Claim:** a hypothesis fits two concatenated lists exactly when it fits each list separately. The proof divides observations according to which list contains them. **Use:** it supports modular assembly of evidence constraints.

### 44. `more_evidence_narrows_models` — Extra Exact Constraints Cannot Add Fitting Candidates

**Claim:** a hypothesis fitting a larger list also fits any included smaller list. Equivalently, the candidate set compatible with the larger list is contained in the earlier set. **Use:** gathering a discriminating observation can shrink the space of explanations.

### 45. `truth_survives_correct_label` — Correct Evidence Preserves a Fitting Truth Function

**Claim:** if the true function fits the existing list, adding its own label for a new input preserves the fit. Result 42 reduces the task to an obvious self-equality and the earlier fit. **Use:** it explains why noiseless elimination can retain the target.

### 46. `distinguishing_query_eliminates_rival` — Ask Where the Explanations Disagree

**Claim:** if a rival predicts a different label from the truth at an input, adding the truth's label there makes the rival fail exact fit. **Use:** this is the core logic behind a discriminating test. A follow-up task should target predictions that differ, not merely collect more of the same ambiguous response.

### 47. `conflicting_labels_impossible` — a Deterministic Rule Cannot Give Two Unequal Answers to One Input

**Claim:** if the evidence assigns distinct labels to the same input, no deterministic hypothesis can fit the entire list. Otherwise its one output would equal two unequal labels. **Use:** contradiction can reveal missing context or an unsuitable model class.

### 48. `incorrect_label_excludes_truth` — Strict Elimination Is Fragile to Error

**Claim:** adding a label unequal to the truth's output makes the truth function fail exact fit. **Use:** this is a reason to treat perfect-label assumptions carefully, including in AI training data and psychological coding.

### 49. `duplicate_evidence_same_models` — Copying a List Creates No New Exact Constraint

**Claim:** fitting a list twice is equivalent to fitting it once. Result 43 reduces the claim to the fact that requiring a condition twice adds nothing. **Use:** duplicated records should not be confused with newly informative observations.

**Research implications.** it formalizes what evidence excludes, rather than what a mind experiences while learning. A psychologically richer model would add noise, graded confidence, forgetting, strategy changes, and tests of whether those additions explain behavior.

## Collective Action — 10 Declarations

[Pinned source: CollectiveAction.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/CollectiveAction.lean)

`Feasible` means every required task has a capable group member. `Accepts` means each member's modeled reward covers their modeled cost, relative to a zero outside option. `Ready` requires both. These definitions isolate capability coverage and individual participation. Capacity, scheduling, bargaining, and normative criteria can be introduced as separate layers, creating an explicit mathematical route from interdependence to richer institutional models.

### 50. `adding_members_preserves_feasibility` — Existing Task Coverage Survives Adding People

**Claim:** a larger group containing a feasible smaller group is feasible. Every earlier capable witness remains available. **Example:** if a team already contains someone for each required role, adding another person does not remove those capabilities in this model.

### 51. `restricting_members_preserves_acceptance` — Removing Members Preserves Remaining Inequalities

**Claim:** if every member of a larger group has reward at least cost, every member of a subgroup does too. **Use:** acceptance is checked person by person under the same functions.

### 52. `union_accepts_iff` — Acceptance Over a Union Decomposes

**Claim:** the union of two groups satisfies the participation inequalities exactly when each group satisfies them. The proof follows whether each member comes from the first group or the second. **Use:** it shows how a property defined pointwise can compose.

### 53. `indispensable_member_withdrawal` — Excluding the Only Possible Provider Leaves a Gap

**Claim:** if any group member capable of a specified task must be one particular person, a group excluding that person cannot cover every task. The proof asks who could perform that task and obtains a contradiction. **Use:** it describes a bottleneck or single point of dependency.

### 54. `complementary_pair_feasible` — Two Specialists Can Cover Two Roles Together

**Claim:** in a two-role world, each person can perform exactly the role with their own Boolean label, so the full pair covers both tasks. For each task, choose its matching person. **Use:** it supplies a constructive example of productive complementarity.

### 55. `no_specialist_alone_feasible` — Neither Role Covers the Whole System

**Claim:** either specialist alone leaves the other task uncovered. The proof considers which specialist remains and selects the opposite role. **Use:** combined with result 54, it demonstrates a precise kind of interdependence.

### 56. `aggregate_surplus_not_participation` — a Good Total Can Conceal a Losing Participant

**Claim:** costs 1 and 1 with rewards 0 and 3 yield total reward 3 greater than total cost 2, yet `Ready` fails because one person receives less than their cost. **Use:** a proposal described as beneficial overall can still fail an individual participation condition.

### 57. `repaired_allocation_ready` — Changing the Split Can Satisfy Both Constraints

**Claim:** allocate rewards 1 and 2 to the same feasible specialist pair with costs 1 each. Both inequalities now hold, so `Ready` holds. **Use:** it separates generating a surplus from arranging a distribution that meets modeled participation constraints.

### 58. `two_person_budget_iff` — Total Affordability Characterizes Existence of an Acceptable Split

**Claim:** an integer share exists covering A's cost and leaving enough for B exactly when the budget covers their combined costs. If affordable, giving A exactly A's cost constructs a valid split. **Use:** this is a complete necessary-and-sufficient condition for the stated allocation problem.

### 59. `acceptable_share_interval` — Characterize Every Acceptable First Share

**Claim:** a particular share satisfies both participation inequalities exactly when it lies between A's cost and `budget − B's cost`. Rearranging B's inequality gives the upper bound. **Example:** costs 2 and 3 with budget 8 allow A's integer share from 2 through 5. **Use:** several allocations may satisfy participation.

**Research implications.** In care coordination, “the service exists,” “someone can perform it,” “the person can access it,” and “the arrangement works for everyone involved” are different questions. The current capability and payoff conditions supply a starting structure. Adding scheduling, transportation, eligibility, and workload would make the representation responsive to more operational questions.

## Aggregation — 8 Declarations

[Pinned source: Aggregation.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Aggregation.lean)

`Higher` compares natural-number counts by cross multiplication. To interpret it as a rate comparison, denominators must be positive. The concrete example verifies that requirement. The illustration below uses fictional “successes” and does not represent treatment outcomes.

| Context | A | B | Higher rate |
|---|---:|---:|---|
| 1 | 9/10 = 90% | 80/100 = 80% | A |
| 2 | 20/100 = 20% | 1/10 = 10% | A |
| Pooled | 29/110 ≈ 26.36% | 81/110 ≈ 73.64% | B |

Table: Synthetic Rates Used in the Aggregation Counterexample

### 60. `reversal_cells_valid` — the Example Contains Legitimate Counts

**Claim:** each success count is no larger than its denominator, and the denominators 10 and 100 are positive. Lean checks these arithmetic facts. **Use:** the reversal is not an artifact of dividing by zero or having more successes than trials. This is a supporting validation lemma.

### 61. `first_stratum_advantage` — A Is Ahead in the First Context

**Claim:** A's 9 out of 10 exceeds B's 80 out of 100. Cross multiplication compares 900 against 800. **Use:** this establishes one premise of the combined reversal.

### 62. `second_stratum_advantage` — A Is Ahead in the Second Context Too

**Claim:** A's 20 out of 100 exceeds B's 1 out of 10. The comparison is 200 against 100. **Use:** A's advantage is present in both modeled contexts, not only one.

### 63. `pooled_reversal` — Pooling Puts B Ahead

**Claim:** B's total 81/110 exceeds A's 29/110. A contributes most of its observations from the low-rate context; B contributes most from the high-rate context. **Use:** an aggregate comparison can reverse within-context comparisons.

### 64. `simpson_reversal` — the Three Comparisons Coexist

**Claim:** A's advantage in each context and B's pooled advantage all hold together. The proof packages results 61–63 as a conjunction. **Use:** this is the complete counterexample, making the apparent contradiction inspectable.

### 65. `equal_weight_addition_preserves_order` — Consistent Unit Weighting Preserves Two Inequalities

**Claim:** if `a ≤ b` and `c ≤ d`, then `a + c ≤ b + d` for integers. Arithmetic proves it. **Use:** it contrasts ordinary addition under common unit weights with comparisons whose composition differs.

### 66. `aggregate_cannot_identify_components` — the Sum-only Ambiguity Is Reused

**Claim:** observing only the sum does not identify both components of the specified two-component model. The proof directly invokes result 33. **Use:** a result about experimental design also describes information lost through aggregation.

### 67. `recoding_cannot_restore_components` — Relabeling a Summary Cannot Recover the Lost Distinction

**Claim:** any shared recoding of the sum still makes `(1,0)` and `(0,1)` observationally equivalent under the baseline probe. The proof combines the ambiguous pair with postprocessing preservation. **Use:** a more sophisticated representation of the same summary does not supply missing information by itself.

**Research implications.** When evaluating a program, a pooled outcome can change because the cases served changed. Defining the target comparison gives the pooled and context-specific statistics their scientific meaning. The same care applies when comparing model performance across easy and difficult benchmark families.

## What the Count Means After Reading the Atlas

The atlas forms seven connected bodies of reasoning. Some results establish a reusable property; some are arithmetic witnesses; some combine or restate earlier results. Their scientific value depends on how they constrain an explanation or improve a decision. `Audit.lean` names the results for dependency checking; it adds no extra social-science theorem to the count.


# Worked Investigations

A short theorem can hide a long scientific argument. Its proof may occupy three lines, while its interpretation requires decisions about measurement, causal structure, and the intended population. The following investigations open those decisions. The additional algebraic and statistical illustrations are explanatory derivations; they are not new Lean declarations in the 67-theorem release.

## Measurement as a Problem of Coordinates

Suppose a psychological response is represented by an underlying value `a` plus an offset `i`. The observable is `a + i`. A researcher sees 12. Which part belongs to the construct and which part to the scale? The answer is not contained in the sum. Both `(a,i) = (8,4)` and `(a,i) = (10,2)` produce the same observation.

This is more than an example of inadequate sample size. Result 19 identifies a transformation that preserves every relevant observation: replace `(a,i)` by `(a+s,i−s)`. Result 20 extends the transformation across the entire population. Even an enormous collection of perfectly measured responses cannot distinguish parameterizations linked by this symmetry if no additional constraint is supplied.

The natural response is to anchor the scale. One may fix an intercept, choose a reference latent value, or introduce another observation with different dependence on the components. Each choice buys identification by adding structure. The scientific responsibility is to say where that structure comes from. A convenient normalization can define coordinates without establishing a substantive psychological zero. A validated anchor can provide stronger empirical justification. These roles should not be confused.

The distinction between absolute levels and differences is especially revealing. If every observation shares the same unknown offset, differences remain exact even though absolute latent values are not identified. Thus a model can leave one question unanswered while resolving another. “The model is unidentified” is often too coarse a diagnosis. The better question is: which quantity is identified, under which design?

Now allow different offsets. Write the observed difference as `d`, the latent difference as `g`, and the offset difference as `b`. The model says `d = g + b`, hence `g = d − b`. If `−delta ≤ b ≤ delta`, subtraction yields `d − delta ≤ g ≤ d + delta`. This is the entire mathematical engine of result 24.

Take `d = 5`. A bound of 2 gives the interval [3,7], a bound of 5 gives [0,10], and a bound of 6 gives [−1,11]. Nothing about the proof changes. What changes is whether the bound excludes zero. The decisive empirical work lies in justifying the admissible bias, not in obtaining more decimal places from the subtraction.

An asymmetric bound can be more appropriate. If `L ≤ b ≤ U`, the same algebra gives `d − U ≤ g ≤ d − L`. This more general expression is an explanatory extension, not an additional verified theorem in the release. It illustrates how formalization can suggest a next result while also identifying the evidence the result would require.

Random error adds another layer. If the observation includes an error term, a deterministic bias interval alone no longer describes uncertainty in an estimated group difference. A statistical procedure would need to account for sampling and measurement error as well as uncertainty about systematic bias. Combining these uncertainties is a modeling task; placing a confidence label on a deterministic bound would not perform it.

The reward for making these distinctions is practical. Instead of arguing vaguely about whether an instrument is “biased,” researchers can ask what kinds of bias matter for the target contrast, which ones cancel, which ones reverse it, and how strongly each is constrained by evidence.

## Identifiability as Geometry of Observations

The two-component example observes `a + b`. In the plane of possible pairs, every pair with the same sum belongs to the same observational class. The points `(1,0)` and `(0,1)` are simply two convenient witnesses. The deeper issue is that the observation is constant along an entire direction of variation.

The second probe observes `a`. Now a candidate must match both `a` and `a + b`. Once the first coordinate agrees, matching the total forces the second to agree. Result 34 checks that argument for all integer pairs, not just the example pair.

In elementary linear algebra, the observation mapping can be written using rows `[1,1]` and `[1,0]`. The first row alone compresses two coordinates into one. Adding a second independent row can restore unique recovery in this particular system. This matrix interpretation is explanatory; the repository does not implement a general rank or determinant theorem.

That perspective suggests an experimental-design question with immediate psychological meaning: does a new task contribute an independent constraint, or does it reproduce the same mixture under another name? A second questionnaire that measures exactly the same sum offers repetition, not structural separation. A task that responds differently to the candidate mechanisms can be much more informative.

The formal success can still be practically fragile. Imagine that the second measurement is `a + (1 + epsilon)b` rather than `a`. If `epsilon` is nonzero, two exact linear observations can distinguish the components over real numbers. But the difference between the observations is only `epsilon b`. Recovering `b` requires division by `epsilon`. When `epsilon` is tiny, small observation errors become large parameter errors. Structural identification and reliable estimation are therefore separate achievements.

This illustration is analytically elementary, but it captures a recurring reason for model-recovery checks. A task may contain the needed distinction in principle while expressing it too weakly for the available data. An optimizer's apparent success does not answer that question by itself. Recovery simulations ask whether known generating parameters or model identities can be recovered under the actual design and plausible noise.

The example also clarifies why a proof should record the candidate class. If only pairs with `b = 0` are permitted, the sum alone identifies `a`. If arbitrary pairs are allowed, it does not. Restricting a model class is sometimes scientifically justified, sometimes merely convenient. The proof records what the restriction permits; evidence and theory must justify imposing it.

## Causality as a Missing Part of the Response Table

The causal module becomes transparent when all four treatment/background combinations are displayed.

| Background U | Treatment T | Outcome if Y follows T | Outcome if Y follows U | Naturally observed under T = U? |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | Yes |
| 0 | 1 | 1 | 0 | No |
| 1 | 0 | 0 | 1 | No |
| 1 | 1 | 1 | 1 | Yes |

Table: Complete Response Table for Two Binary Causal Models

On the two observed rows, the models agree perfectly. On the two unobserved rows, they disagree. The problem is not that the models produce almost identical predictions that a larger sample might separate. They produce identical observations under the specified assignment.

Assume an estimator receives that observational mapping and returns an integer effect numerator. Because the mapping is identical in both models, the estimator must return the same integer. But the correct numerator is 2 in one model and 0 in the other. A universally correct estimator would therefore require `2 = 0`. The contradiction establishes result 39.

Notice the quantifiers. The theorem does not say that no estimator can ever be correct for one of these models. An estimator that always returns 2 is correct for the treatment-driven model. It fails on the background-driven model. The theorem rules out a guarantee of correctness across the whole allowed class when the input contains only the stated observational object.

This difference reveals the strength of the result. A method can return the right answer in a particular world without having information that distinguishes that world from another admissible one. Confidence generated by the method cannot manufacture the missing distinction.

Changing the design can help. Setting treatment independently of background can expose combinations that natural assignment omits, provided the intervention has the intended meaning. Additional assumptions can also help by ruling out candidate worlds. The model must state those assumptions explicitly. A proof about the restricted class then becomes informative, but its empirical scope is only as credible as the restriction.

The repository's last causal theorem takes the strongest possible information route: two deterministic response tables that agree everywhere define the same model. Its strength lies in stating precisely what complete information would determine. Research design then asks which observations and assumptions can recover the needed contrasts from realistically available data.

For social networks, the stakes are similar even though the real mathematics is richer. Similar behavior among connected people may reflect influence, selection of similar companions, shared conditions, or several mechanisms together. Shalizi and Thomas (2011) establish a substantive precedent for these identification difficulties. The binary example here should be understood as an instructional counterpart, not a Lean reproduction of their full results.

## Cooperation Has Several Thresholds

The donation game has a small enough payoff structure to expose its entire incentive argument. Consider one player while the other contributes. Contribution yields `benefit − cost`; defection yields `benefit − sanction`. Contribution resists an improving deviation precisely when `cost ≤ sanction`.

This condition is striking partly because benefit disappears. Holding the other player's action fixed makes benefit the same in both options, so it cancels. The cancellation is informative about the model's strategic comparison. It does not establish that perceived benefit is psychologically irrelevant in a richer decision process.

The condition for preferring mutual contribution to mutual defection is different: `cost < benefit + sanction`. A setting can satisfy this outcome comparison while still failing the unilateral incentive test. That is the logical shape of a collective-action problem: a mutually better outcome need not be individually stable under the specified rules.

The collective-action module adds another distinction. A team can have the capabilities needed to cover every task while allocating its rewards in a way that fails someone's participation condition. With costs 1 and 1 and rewards 0 and 3, the total looks promising and one person still loses relative to the model's zero outside option. Changing the split to 1 and 2 satisfies both inequalities.

Four questions must therefore remain separate: Can the task be performed? Does each participant receive enough under the defined criterion? Is the proposed behavior stable against relevant deviations? Is the arrangement legitimate or fair? The current release supplies precise versions of the first three across different modules. Connecting them and adding an explicit normative criterion would produce a richer institutional model.

Its coverage notion isolates the availability of a skill. “For every task, some member can perform it” does not enforce that the same member has time to perform every task for which that person is the witness. A care organization with one professional capable of ten simultaneous appointments satisfies a simple coverage predicate while failing a scheduling requirement. That gap identifies a useful extension: capacity-constrained assignment.

The withdrawal theorem reveals a second precision issue. Its premise says that anyone in the group capable of a selected task must be the designated agent. That premise is also true when no one can perform the task. The theorem still correctly concludes that excluding the agent leaves the task uncovered. To describe a functioning organization becoming nonfunctional, one must separately establish initial feasibility. Adding that premise upgrades an exclusion result into a theorem about the loss of an initially feasible arrangement.

The relationship to classical sociology is therefore interpretive and selective. Differentiated roles can motivate a formal study of interdependence. The particular capability predicates, payoff inequalities, and integer transfers remain the modeler's choices. Historical scholarship must determine whether they faithfully reconstruct a selected argument; a theorem prover cannot do that textual work by itself.

## Aggregation Changes the Question Unless the Target Is Fixed

The synthetic rate example places most A observations in the difficult context and most B observations in the easy one. Within each context, A's rate is ten percentage points higher. The pooled values reverse because the mixtures differ.

This is not an arithmetic paradox. A pooled rate weights each context by its share of that group's observations. A's weights are 10/110 and 100/110; B's are 100/110 and 10/110. Different weighting schemes can produce different comparisons without any inconsistency.

If both groups were standardized to equal context weights, their illustrative rates would be `(0.90 + 0.20)/2 = 0.55` for A and `(0.80 + 0.10)/2 = 0.45` for B. This calculation describes a new comparison, not the original pooled outcome. Whether it is the scientifically appropriate comparison depends on the target population and causal question.

A confounder, a mediator, and a collider can demand different treatment in a causal analysis. A rule saying “always stratify when there is a reversal” is therefore not justified by the counterexample. The proof teaches that the comparison depends on composition; it does not select a universal adjustment policy.

This point applies to AI benchmarks as well. Suppose one system is evaluated mainly on easy proofs and another mainly on difficult ones. Their pooled pass rates may conceal their relative performance within matched problem families. A good evaluation defines the test distribution, reports stratified results where relevant, and resists treating one pooled percentage as an explanation.

## Repetition, Evidence, and the Difference Between a Copy and a New Trial

The learning module says that duplicating a list changes no exact-consistency constraints. A deterministic rule agreeing with every entry once agrees with them twice. That result is correct and narrower than the tempting slogan that repetition supplies no information.

For independent Bernoulli observations under a probability model, repeated outcomes can change a likelihood. With `s` successes and `f` failures, the likelihood is proportional to `p^s(1−p)^f`. Additional independent trials alter the exponents. Copying existing records and pretending they are independent trials also alters the computed expression, but without adding independent evidence. The statistical model would then be misapplied.

This contrast gives result 49 a useful role in reasoning about data provenance. The word “duplicate” may refer to a copied record, a repeated task, or a newly observed event with the same value. Those are different data-generating circumstances. The Lean theorem handles list-based exact fit. A probability model supplies the additional structure needed to study repeated sampling.

Likewise, conflicting labels need not establish irrationality or measurement fraud. A task description that omits context can map two genuinely different situations to the same formal input. A time index, social relationship, instruction, or internal state may be missing. Formal contradiction can be a clue that the scientific representation needs more detail.

## A Metacognitive Puzzle That Points Beyond the Current Library

Imagine a predictor that assigns confidence 0.50 on every trial and is correct on exactly half its trials. At the only confidence value it uses, the observed correctness rate matches the stated confidence. Yet the confidence report provides no way to distinguish correct from incorrect trials. Calibration and discrimination are different properties.

This is an explanatory example, not a new theorem in the release. It demonstrates why a future formalization of metacognition should define its target carefully. A property of average confidence is not automatically a property of metacognitive sensitivity, and a sensitivity measure is not automatically an account of the process generating confidence. Fleming and Lau (2014) provide methodological background on these distinctions and measurement issues.

The experiment-design question becomes sharper: which observations distinguish a shift in confidence level from a change in how confidence tracks correctness? Which model parameters are identifiable when task performance changes? Could two mechanisms yield the same confidence distribution but different responses to an intervention? These are plausible research targets that connect formal methods to substantive psychological measurement.

The existing library supplies tools for recognizing the structure of these problems. A next development would add probability distributions, an explicit confidence model, a likelihood, and recovery analysis. That is a concrete path from a methodological foundation to a substantive psychological investigation.


# Anatomy of the Arguments

The atlas shows what the library contains. Examining the internal architecture of several proofs reveals why a collection of modest lemmas can become a useful scientific instrument. The central move is to preserve an argument while changing its setting. A path proof assembles local steps into global reach. An identification proof carries information from observations back to candidate explanations. An impossibility proof constructs a pair that defeats every method with the same restricted input.

The following propositions restate selected results from the inspected source in conventional mathematical notation (Sodelin, 2026). Their proofs explain the existing development. Set notation is used as a reading aid for the predicates in Lean, and the integer domains are retained where they determine the statement. The equations also make the quantifiers visible: some claims describe every allowed case, while others establish one decisive witness.

## Paths: How a Local Rule Produces Global Reach

Let the vertices be the natural numbers. Define adjacency by saying that one vertex is the successor of the other. Reachability is generated by two constructors: a vertex reaches itself, and a route can be extended by one adjacent step. This inductive definition is itself an explanation of what counts as a route.

**Route-composition lemma.** If A reaches B and B reaches C, then A reaches C. This is result 02, `reach_trans`.

*Proof.* Hold the route from A to B fixed and induct on the construction of the route from B to C. In the base case, the second route stays at B, so the first route is already the desired route. In the step case, the second route first reaches an intermediate vertex and then takes one adjacent step. The induction hypothesis joins the first route to that intermediate route; the final step extends the joined route to C. Every route generated by the definition has one of these forms, so the proof covers all finite routes. □

Symmetric adjacency then supports reversed routes. Induction on the destination shows that zero reaches every natural-number vertex: the route to zero is immediate, and the route to the successor extends the previous route. Combining reversal with composition yields connectivity between any two vertices. This is the dependency chain behind results 01–05.

**Local-to-global counterexample.** At most two candidate labels can be adjacent to any vertex, yet vertices with arbitrarily large labels are reachable from zero. For any bound N, choose the destination N + 1. The connectivity argument supplies a finite route to it. Results 06 and 07 therefore separate a bound on local contacts from a bound on the extent of the reachable network.

The proof makes one source of confusion easy to diagnose. A bounded number of direct acquaintances is a local property. The number of people reachable through chains is a global property. A model of how trust, information, or resources actually travel would add conditions on transmission along those chains. Having established the network distinction, the next model can study those mechanisms without repeatedly rebuilding the underlying argument.

## Measurement: An Identified Contrast Inside an Unidentified Representation

Let a and b be latent integer values, with a shared integer intercept i. The response function adds the intercept. Result 18 yields

$$
(a+i)-(b+i)=a-b.
$$

*Proof.* Expand subtraction and cancel the shared intercept. The Lean proof unfolds the response definition and uses integer arithmetic automation to construct a proof of the equality. □

The consequential point is the target of inference. A response alone leaves a latent value and its intercept interchangeable under compensating shifts. The difference of two responses, however, is exactly determined when the shift is common. An identifiable contrast can live inside a representation whose absolute coordinates remain ambiguous.

Allow intercepts to differ. Write d for the observed A-minus-B difference, g for the latent difference, and q for the intercept difference. Then

$$
d=g+q,\qquad -\delta\leq q\leq\delta.
$$

**Bias-bound proposition.** The stated assumptions imply

$$
d-\delta\leq g\leq d+\delta.
$$

*Proof.* From q ≤ δ and g = d − q, subtraction gives g ≥ d − δ. From q ≥ −δ, subtraction gives g ≤ d + δ. These are the two conjuncts of result 24. If d > δ, the lower inequality yields g > 0; result 25 establishes that sign conclusion using the relevant upper bound on q. □

The assumptions on q already imply that δ is nonnegative whenever they can be satisfied. A theorem prover can establish a conditional statement even for parameter values with impossible premises, so a meaningful application also supplies an admissible instance. In the worked example, d = 5 and δ = 2 make the domain concrete and the positive sign unavoidable.

This is a useful form of scientific leverage: a disputed measurement assumption becomes an explicit quantity whose magnitude can be studied. Researchers can ask whether the largest plausible differential offset is smaller than the observed contrast. The formalization identifies precisely how that empirical assessment controls the conclusion.

## Identification: The Design Determines the Equivalence Classes

Let Θ be a candidate space, X a probe space, and Y an output space. A prediction function maps a candidate and probe to an output. A design D selects probes. Two candidates are equivalent on D when their predictions agree on every selected probe:

$$
\theta\sim_D\phi
\quad\Longleftrightarrow\quad
\forall x\in D,\ f(\theta,x)=f(\phi,x).
$$

The design identifies the candidate space when equivalence forces equality. Reflexivity, symmetry, and transitivity follow from the corresponding properties of equality, providing results 26–28. These lemmas justify treating observationally indistinguishable candidates as classes.

**Design-extension proposition.** Suppose a design S identifies the candidate space and every probe in S also belongs to a design L. Then L identifies that space.

*Proof.* Choose arbitrary candidates that agree on L. They agree on every probe in S because S is included in L. Identification by S then forces the candidates to be equal. Since the candidates were arbitrary, L identifies the whole space. This is result 30, using result 29. □

Notice the direction of the argument. More probes impose more equality requirements on a candidate pair; fewer pairs remain equivalent. This is the same logical pattern that will appear in learning from additional exact evidence. A shared proof pattern can connect research problems that initially sound unrelated.

For the concrete integer-pair model, the first design observes only a + b. The pairs (1,0) and (0,1) have equal outputs and unequal coordinates. Their existence refutes identification. The enriched design observes both a and a + b. Suppose two candidates agree on those outputs. Agreement on the component fixes a; equality of totals then fixes b by cancellation. This proves result 34 for all candidate pairs.

The decisive scientific question becomes whether a proposed task adds a new constraint on the mechanisms under study. If it does, formalization can demonstrate the resulting change in distinguishability. The experiment gains a reason for its design that is stronger than the hope that another measure will help.

## An Impossibility Proof With an Entire Class of Estimators in View

Write O(M) for the observational object generated by a model M, and Δ(M) for its target effect numerator. Suppose two allowed models have the same observation but different targets:

$$
O(M_1)=O(M_2),\qquad \Delta(M_1)\ne\Delta(M_2).
$$

**Information-limit argument.** An estimator that receives only O(M) cannot return the correct target for every allowed model.

*Proof.* Assume an estimator E is correct for every model in the class. Correctness at the two selected models gives E(O(M₁)) = Δ(M₁) and E(O(M₂)) = Δ(M₂). Equality of observations makes the left sides equal. The right sides would therefore be equal, contradicting the assumed target difference. □

Result 39 instantiates this pattern in a precisely specified binary model. One outcome follows treatment; the other follows background. Natural assignment makes treatment equal background, producing identical observational functions. Their effect numerators are 2 and 0, supplying the contradiction.

The strength of this argument comes from its quantifier over estimators. It is not a report that a selected regression, neural network, or optimization routine failed. Every function with the specified input faces the same conflict. An improved computational method can use existing information more effectively, while identification requires the input or model class to contain the distinction the target needs.

This also explains the constructive use of impossibility. The proof points to the missing resource. An intervention can reveal an unobserved combination; an additional measurement can distinguish candidate mechanisms; a scientifically justified assumption can narrow the class. Each proposal changes a clearly identified part of the problem.

## Learning: Why a New Label Can Remove a Rival

Let h be a deterministic hypothesis and E a finite list of input–label pairs. The predicate Fits requires h(x) = y for every pair (x,y) in E. Appending two evidence lists corresponds to satisfying both sets of constraints:

$$
\mathrm{Fits}(h,E_1\mathbin{+\!+}E_2)
\quad\Longleftrightarrow\quad
\mathrm{Fits}(h,E_1)\land\mathrm{Fits}(h,E_2).
$$

*Proof.* A pair in either component list belongs to the appended list, giving the forward direction. A pair in the appended list belongs to at least one component, so the relevant fit assumption gives the reverse direction. This is result 43. □

Adding a correctly labeled query at x preserves a truth function that already fits the old evidence. If a rival predicts a different label at x, fitting the new evidence would require that rival to equal the truth label there, a contradiction. Results 45 and 46 therefore connect the choice of a query to the survival or elimination of hypotheses.

Duplicating the entire list yields the same fit condition twice. The conjunction of a proposition with itself is equivalent to that proposition, establishing result 49. This derivation gives a compact algebra of exact evidence: combining lists combines constraints, repeated constraints are redundant, and a discriminating constraint removes a rival. A stochastic observation model would add a different account of how repeated measurements update support.

## Participation: The Entire Set of Acceptable Allocations

Let cA and cB be integer costs, B an integer budget, and s the share allocated to A. The modeled participation conditions are

$$
c_A\leq s,\qquad c_B\leq B-s.
$$

**Allocation proposition.** There is some integer share satisfying both conditions exactly when cA + cB ≤ B.

*Proof.* For necessity, add the two participation inequalities: the shares sum to B, so the costs cannot exceed B. For sufficiency, choose s = cA. A's inequality holds at equality, and B − cA ≥ cB follows from the total-budget assumption. This proves both directions of result 58 and constructs a valid allocation. □

Result 59 characterizes all acceptable first shares:

$$
c_A\leq s\leq B-c_B.
$$

This interval makes an institutional design question visible. With costs 2 and 3 and budget 8, four integer allocations meet the participation conditions: first shares 2, 3, 4, and 5. Participation alone leaves a choice among them. A bargaining rule, equality criterion, priority principle, or contribution-based rule can select within that set once its normative commitments are specified.

The proof has therefore done two jobs. It establishes whether an allocation exists and describes the available design space. Scientific or normative work can now address selection within that space with the arithmetic already secured.

## The Role of the Checker in These Arguments

Lean represents each theorem as a term of the claimed proposition's type. Tactics help construct that term; the kernel checks it. In this development, `rfl` handles definitional equalities, `funext` reduces function equality to pointwise equality, `constructor` separates conjunctions or implications in an equivalence, and induction follows the structure of a natural number or route. The `omega` tactic handles the relevant integer and natural-number linear arithmetic. These are different proof-construction methods serving one checkable logical interface (Lean Project, n.d.).

That division of labor is valuable for collaboration. A psychologist can examine what the variables and comparisons mean. A mathematician can inspect the proposition and the generality of its argument. A formal-methods researcher can review definitions, dependencies, and verification. An AI system can assist in proposing and checking steps. The artifact gives each participant a stable object on which to work.

The intellectual reward appears when these levels meet. A short cancellation proof reveals an identified contrast. An elementary witness reveals an information limit. A two-sided inequality reveals an allocation space. Precision becomes scientifically exciting when it changes the question a researcher knows how to ask.


# Verified Social-Science Models and AI

The prospect is compelling: a language model could produce an explanation whose deductive core is independently checkable. When the explanation fails, the failure could identify a missing premise, an invalid step, or an underdetermined question. These are concrete capabilities that a research program can develop and measure.

## Four Different Routes from a Library to a Model

| Route | What happens | What must be evaluated |
|---|---|---|
| Context or retrieval | Relevant definitions and results are supplied when answering a question | Does the model select the right theorem and preserve its assumptions? |
| Tool-assisted reasoning | The model proposes statements or proofs and receives checker feedback | Does checking reduce errors while the formal statement still matches the intended question? |
| Supervised training | Model parameters are updated using curated examples | Does learning generalize beyond copied statements and familiar proof patterns? |
| Reinforcement learning with verification | A training process uses formal feedback as part of its reward | Does the reward encourage the intended reasoning without weakening the task or exploiting the evaluator? |

Table: Routes From a Verified Library to an AI System

Context and retrieval make the material useful immediately by changing the information available to an answer. Supervised and reinforcement training require a separate pipeline that updates model parameters. Publicly releasing a corpus makes that reuse possible; actual inclusion in a provider's training data depends on that provider's choices.

There is direct precedent for the training route in formal mathematics. Xin et al. (2024) report training with a large synthetic Lean proof corpus. Ren et al. (2025) describe a later prover using subgoal decomposition and reinforcement learning. These reports establish that formal proof data can be part of a productive training pipeline for theorem proving. The next question is transfer: which scientific and social reasoning skills improve when the training material pairs formal structure with substantive interpretation?

## What the Present Corpus Could Teach

The most promising targets are disciplined distinctions: reachability versus trust, observed score versus latent value, observational fit versus causal identification, total surplus versus individual participation, and exact consistency versus probabilistic evidence. A model that reliably preserves these distinctions would make fewer specific reasoning errors.

Pairing Lean with an interpretation gives a learner both the deductive structure and its intended scientific meaning. In result 13, the labels are arbitrary and causally inert. If a training example says only “heterogeneous cooperation exists,” a learner may acquire the slogan and miss the reason it holds. A better example pairs the statement with its definitions, a plain-language interpretation, and an explanation of which mechanism the model isolates and how that mechanism could be extended.

One promising unit of training data would contain the research question, formal objects, theorem statement, checked proof, interpretation, boundary conditions, a nearby false claim, and a counterexample to that false claim. It would also record source provenance and review status. This is a proposed design for a dataset; no such training run was performed here.

For instance, the true statement is that common additive offsets preserve differences. A nearby false statement is that all group-specific offsets preserve differences. The counterexample makes the missing assumption visible. A second nearby claim—“therefore this instrument is unbiased”—does not follow from either theorem. Teaching the model to identify that change in claim type may matter more for scientific communication than teaching it to reproduce the arithmetic proof.

## The Reward Must Be Attached to the Right Statement

A checker accepts a proof of the statement it receives. If a system silently weakens the conclusion or strengthens the premises until the task becomes trivial, successful checking no longer measures success on the original question. The statement must therefore be fixed or independently reviewed before the proof is scored.

Similarly, inconsistent premises allow arbitrary conclusions in classical logic. A proof that follows from inconsistent assumptions is a derivation, but it does not provide a useful model of a possible case. Vacuous universal statements can also be correct for an empty domain while being misleadingly described as claims about a populated society. Verification quality therefore includes premise and interpretation review, not only a compiler success flag.

The official Lean documentation distinguishes a valid proof from the meaning of its statement and describes stronger checking procedures for higher-risk settings. This report inspected standard source and CI evidence; it did not run those stronger external checks. (Lean Project, n.d.)

## How to Test Transfer Without Rewarding Memorization

A credible study should compare the same base model under carefully matched conditions: no supplied corpus, prose-only explanations, formal code only, paired prose and formal material, and paired material with access to a checker. These are proposed experimental arms. They would separate the value of the information, its presentation, and verification feedback.

Training and evaluation should be split by underlying model family or theorem dependency group, not merely by randomly distributing individual declarations. Result 66 directly reuses result 33, and result 64 packages earlier comparisons. Placing one in training and the other in testing could inflate apparent generalization. Splitting paraphrases of the same example across the boundary would create a similar problem.

Useful test tasks include translating a verbal claim into a formal statement; locating missing assumptions; detecting that a question is underdetermined; finding a counterexample to an overgeneralization; explaining why a proof does not establish a clinical claim; and distinguishing a normative premise from an empirical observation. Some tasks have checker-verifiable answers. Others require independent, blinded domain review of semantic fidelity.

The evaluation should separately report proof success, correct statement selection, assumption preservation, unsupported empirical claims, uncertainty calibration, and performance on new domains. A higher proof pass rate alongside more unjustified social conclusions would not be a successful outcome for this project.

The proposed primary scientific-communication endpoint is the rate of unsupported conclusions on held-out scenarios, accompanied by accuracy and abstention measures. A useful improvement would reduce unsupported claims without achieving that reduction merely by refusing every question. Its practical threshold should be specified before data collection with the intended users and the consequences of errors in view.

No effect size is available for this proposed intervention. A future analysis might report paired accuracy differences or changes in error rates with uncertainty intervals. Because questions share templates and model families, uncertainty should respect that clustering. Treating every generated paraphrase as an independent observation would create misleading precision.

## Ethics Requires a Second Kind of Discipline

Formal ethical reasoning can specify obligations, permissions, prohibited actions, priorities, and exceptions. Benzmüller et al. (2020) describe a framework using higher-order logic and automated reasoning to investigate normative theories. This establishes a route for extending the project into explicit normative theories.

A useful distinction separates logical coherence, empirical consequences, and normative justification. A policy can be internally coherent under a set of values while relying on false empirical beliefs. It can generate an intended consequence while being unacceptable under another defensible value commitment. A theorem can expose those dependencies without settling them.

For example, `Accepts` in the collective-action module means reward covers modeled cost. Renaming that predicate “consent” would not add voluntariness, adequate information, freedom from coercion, or the ability to withdraw. Similarly, an allocation that satisfies two participation inequalities need not satisfy an independently defined equality or priority principle. The gap is conceptual, not a missing arithmetic tactic.

This is where a paired corpus could be particularly useful. It could require a model to say which ethical premises are assumed, which consequences have been proved, and which empirical facts would still need to be established. The goal would be auditable reasoning about values and consequences: a model that can state an obligation, preserve its exceptions, identify a conflict, and explain how a conclusion changes when a premise changes. Those capabilities would be meaningful targets for an evaluation of ethical reasoning.



# Research Program

## Deconstructive Analysis — Tracing a Broad Claim Downward

Consider the assertion, “A verified psychological model gives an AI a correct understanding of people.” It contains several transitions. The natural-language theory must be represented faithfully; the formal proof must establish the intended property; the model must capture relevant processes; the observations must measure those processes; the trained system must use the model correctly; and its behavior must generalize to new settings.

The 67-theorem audit primarily strengthens the deductive transition. The literature supplies precedents for the surrounding activities. It does not collapse the chain into one guarantee.

This diagnosis is useful because each transition has a distinct failure test. Compare the formal statement with the prose to test semantic fidelity. Inspect proofs and dependencies to test formal correctness. Compare models and data to test empirical adequacy. Review instruments to test measurement validity. Evaluate held-out behavior to test transfer. No single score can substitute for this structure.

The same method applies to a narrower statement: “Shared identity supports cooperation.” Does identity alter expected behavior, preferences, contact opportunities, or enforcement? Does cooperation mean contribution, persistence, or mutual obligation? Does the conclusion concern a possible equilibrium, a likely outcome, or a morally justified institution? The present model answers one incentive question after most of those choices have already been made.

## Reconstructive Analysis — Building Upward from a Useful Result

A productive extension could start from a measurement problem in metacognition. Define the observations and candidate mechanisms, establish which parameters or contrasts are identifiable, add a realistic observation model, and investigate recovery under the proposed design. Only then ask whether the model fits new data and improves on alternatives.

A second route starts from team capability. Replace the current coverage predicate with a finite assignment model including capacity and scheduling. State participation or access conditions separately. Prove an informative feasibility or failure result, then examine whether the formal variables correspond to real operational constraints. This would extend the current sociology-inspired work toward an application while connecting the scheduling result to the institution's observed constraints.

A third route starts from AI scientific explanation. Build examples in which a theorem is valid but its tempting broader interpretation is not. Train or prompt a model on paired correct and incorrect interpretations, then assess new model families with blinded review and checker feedback. The target is a reduction in a specified reasoning error, giving the broader ambition of improved understanding an observable test.

These paths all follow the same discipline: select a bounded question, preserve provenance, identify the decisive assumption, and choose an evaluation that could reveal failure. The excitement lies in making an elusive question tractable enough to challenge.

## Middle-out Synthesis — the Most Useful Place to Work

A model family tied to a measurement, experiment, or institutional problem provides a productive scale for this research. The family is broad enough to compare meaningful alternatives and precise enough to connect a proof to an actual decision.

The present library is well positioned to support that scale because several modules connect naturally. Identifiability describes what observations distinguish. Measurement specifies how observations arise. Causality distinguishes observational equivalence from intervention consequences. Learning tracks compatibility with evidence. Aggregation describes information and comparisons lost in summaries. Collective action connects capabilities to participation constraints.

Those links organize a research program around a clear criterion: an extension should make a previously ambiguous scientific decision more explicit and testable. A theorem that changes an experiment is a particularly tangible form of progress.



# Metacognitive Review of the Evidence Process

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

# Metacognitive Reflection on Inference Robustness

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



# Conclusion


The project demonstrates that selected methodological distinctions can be encoded as small, reproducible Lean developments. Its strongest present contribution is a clear chain from definitions to conditional consequences. It also supplies instructive counterexamples to claims that are easy to overstate in ordinary language.

The next advance should connect that chain to a consequential research decision: a measurement that separates mechanisms, an assumption whose failure changes an inference, or a model property whose verification protects an empirical analysis. Progress can be measured by the new research decisions the formalization makes possible.

For AI, verified libraries can support retrieval, tool-assisted reasoning, and carefully designed training studies. Existing theorem-proving research makes that prospect credible. The specific claim that formalized psychology or ethics improves broad social reasoning remains a research hypothesis. It deserves a test designed to detect both gains and overconfidence.



# References

Axelrod, R. (1997). The dissemination of culture: A model with local convergence and global polarization. *Journal of Conflict Resolution, 41*(2), 203–226. https://doi.org/10.1177/0022002797041002001

Benzmüller, C., Parent, X., & van der Torre, L. (2020). *Designing normative theories for ethical and legal reasoning: LogiKEy framework, methodology, and tool support* (Version 6) [Preprint]. arXiv. https://arxiv.org/abs/1903.10187v6

Finkel, A., Fougea, G., & Le Roux, S. (2025). *An automata-based method to formalize psychological theories: The case study of Lazarus and Folkman's stress theory* [Preprint]. arXiv. https://arxiv.org/abs/2501.05185

Fleming, S. M., & Lau, H. C. (2014). How to measure metacognition. *Frontiers in Human Neuroscience, 8*, Article 443. https://doi.org/10.3389/fnhum.2014.00443

Formalizing Soft Sciences Project. (2026). *How we formalized questions about society: A reader's guide to 67 Lean proofs, their theory, and their limits* [Unpublished project reader's guide].

Guest, O., & Martin, A. E. (2021). How computational modeling can force theory building in psychological science. *Perspectives on Psychological Science, 16*(4), 789–802. https://doi.org/10.1177/1745691620970585

Heath, J., Kwiatkowska, M., Norman, G., Parker, D., & Tymchyshyn, O. (2008). Probabilistic model checking of complex biological pathways. *Theoretical Computer Science, 391*(3), 239–257. https://doi.org/10.1016/j.tcs.2007.11.013

Holliday, W. H., Norman, C., & Pacuit, E. (2021). *Voting theory in the Lean theorem prover* [Postprint]. arXiv. https://arxiv.org/abs/2110.08453

Human Relations Area Files. (n.d.). *Sampling for cross-cultural anthropological research*. HRAF advanced cross-cultural research course. https://hraf.yale.edu/advanced-ccc/8.%20Sampling%20for%20Cross-Cultural%20Anthropological%20Research/sampling.html

Huys, Q. J. M., Maia, T. V., & Frank, M. J. (2016). Computational psychiatry as a bridge from neuroscience to clinical applications. *Nature Neuroscience, 19*, 404–413. https://doi.org/10.1038/nn.4238

Lean Project. (n.d.). *Validating a Lean proof*. The Lean language reference. Retrieved September 28, 2026, from https://lean-lang.org/doc/reference/latest/ValidatingProofs/

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., . . . Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, Article n71. https://doi.org/10.1136/bmj.n71

Read, D., Fischer, M., & Leaf, M. (2013). What are kinship terminologies, and why do we care? A computational approach to analyzing symbolic domains. *Social Science Computer Review, 31*(1), 16–44. https://doi.org/10.1177/0894439312455914

Ren, Z. Z., Shao, Z., Song, J., Xin, H., Wang, H., Zhao, W., Zhang, L., Fu, Z., Zhu, Q., Yang, D., Wu, Z. F., Gou, Z., Ma, S., Tang, H., Liu, Y., Gao, W., Guo, D., & Ruan, C. (2025). *DeepSeek-Prover-V2: Advancing formal mathematical reasoning via reinforcement learning for subgoal decomposition* [Preprint]. arXiv. https://arxiv.org/abs/2504.21801

Shalizi, C. R., & Thomas, A. C. (2011). Homophily and contagion are generically confounded in observational social network studies. *Sociological Methods & Research, 40*, 211–239. https://doi.org/10.1177/0049124111404820

Shea, B. J., Reeves, B. C., Wells, G., Thuku, M., Hamel, C., Moran, J., Moher, D., Tugwell, P., Welch, V., Kristjansson, E., & Henry, D. A. (2017). AMSTAR 2: A critical appraisal tool for systematic reviews that include randomised or non-randomised studies of healthcare interventions, or both. *BMJ, 358*, Article j4008. https://doi.org/10.1136/bmj.j4008

Society for Mathematical Psychology. (n.d.). *Society for Mathematical Psychology*. Retrieved September 28, 2026, from https://mathpsych.org/

Sodelin. (2026). *Formalizing Soft Sciences* (Commit 780f1b83aef15a9cf455566bab9df2a47d738074) [Computer software]. GitHub. https://github.com/Sodelin/Formalizing-Soft-Sciences/tree/780f1b83aef15a9cf455566bab9df2a47d738074

Sterne, J. A. C., Savović, J., Page, M. J., Elbers, R. G., Blencowe, N. S., Boutron, I., Cates, C. J., Cheng, H.-Y., Corbett, M. S., Eldridge, S. M., Emberson, J. R., Hernán, M. A., Hopewell, S., Hróbjartsson, A., Junqueira, D. R., Jüni, P., Kirkham, J. J., Lasserson, T., Li, T., . . . Higgins, J. P. T. (2019). RoB 2: A revised tool for assessing risk of bias in randomised trials. *BMJ, 366*, Article l4898. https://doi.org/10.1136/bmj.l4898

Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife, 8*, Article e49547. https://doi.org/10.7554/eLife.49547

Xin, H., Guo, D., Shao, Z., Ren, Z., Zhu, Q., Liu, B., Ruan, C., Li, W., & Liang, X. (2024). *DeepSeek-Prover: Advancing theorem proving in LLMs through large-scale synthetic data* [Preprint]. arXiv. https://arxiv.org/abs/2405.14333


# Appendix A

## Verification and Source Map

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

# Appendix B

## Relationship to the Earlier Book

This monograph expands *How We Formalized Questions About Society: A Reader's Guide to 67 Lean Proofs, Their Theory, and Their Limits* (Formalizing Soft Sciences Project, 2026). It preserves the earlier distinction between reach, membership, trust, and incentives; the six foundation modules; the theorem identities; and the connection from proof to research question.

The expanded presentation adds a cross-disciplinary account of mathematical and computational modeling, longer worked arguments, a formal AI-evaluation proposal, and integrated discussion of normative reasoning. It also reconciles the earlier book's chronology: its early chapter describes the 16-theorem stage, while later chapters describe the 67-theorem release. Proposed task-complementarity examples in that early discussion subsequently appear as checked results in the collective-action module.

The earlier book records a separate, larger mathematics-of-psychology corpus whose location had not been recovered. That corpus remains outside this 67-theorem audit. This edition neither counts it nor replaces it. Its future integration would require its source, toolchain, provenance, and a reproduced verification record.

# Appendix C

## Formal Objects at a Glance

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

Table: Formal Objects and Their Roles in the Source

The exact source definitions govern interpretation. The notation in this table is a reading aid, with parameter names expanded for clarity.

# Appendix D

## A Research Program With Concrete Milestones

**Milestone 1: a validated semantic map.** Have a mathematical reviewer and a domain researcher inspect a small set of paired informal and formal statements. Resolve disagreements about variable meaning before adding extensive proofs.

**Milestone 2: a richer measurement model.** Select one target contrast, state its measurement equation, and distinguish exact identification from finite-data recovery. Develop a sensitivity analysis whose assumptions can be informed by data or substantive knowledge.

**Milestone 3: a design-changing result.** Identify a rival explanation that the initial task cannot separate. Add an observation or intervention with a clearly stated discriminating role. Evaluate its practical recovery properties before collecting a large confirmatory sample.

**Milestone 4: a reusable model artifact.** Package the statement, definitions, proof, interpretation, and verification receipt with an immutable version. Record source licensing and authorship so the artifact can be reused responsibly.

**Milestone 5: a controlled AI evaluation.** Compare representation and checker-access conditions, split by model families, and evaluate both formal correctness and scientific interpretation. Publish failures and successful cases with the same provenance discipline.

These milestones make progress visible through capabilities acquired: a better specification, an identified contrast, an improved design, a reproducible artifact, and a tested reasoning benefit.

# Appendix E

## Glossary


**Axiom.** A proposition accepted without proof within a formal system. Standard logical axioms are distinct from substantive assumptions encoded through model definitions or theorem premises.

**Construct validity.** The justification for interpreting an observation or score as representing the intended concept.

**Counterexample.** A case satisfying a claim's premises while violating its conclusion; one suffices to refute the corresponding universal assertion.

**Empirical adequacy.** How well a model serves its intended explanatory or predictive purpose in the world.

**Equilibrium.** A strategy configuration meeting a specified stability condition. The exact deviation class and preference assumptions matter.

**Formalization.** Translation of a question, structure, or argument into precise mathematical or logical objects.

**Identifiability.** Uniqueness of a target quantity given the permitted observation object and model class. Structural identifiability differs from reliable estimation with finite data.

**Invariant.** A property preserved by a specified transformation or process.

**Kernel.** The small core of a proof assistant responsible for checking proof terms against formal statements.

**Lemma.** A proved result used to support other results. The term concerns its role, not necessarily its difficulty.

**Model checking.** Algorithmic examination of whether a formally described system satisfies specified properties, with guarantees that depend on the method, state space, and any approximations.

**Normative premise.** An assumption about what should be valued, permitted, or required.

**Observational equivalence.** Agreement of candidate models on the observations permitted by a design.

**Parameter recovery.** Testing whether an estimation procedure can recover known generating parameters under a specified design and data-generating model.

**Proof assistant.** Software for constructing and checking formal proofs, often interactively.

**Semantic fidelity.** Agreement between the intended informal meaning and the actual formal statement and definitions.

**Sensitivity analysis.** Investigation of how a conclusion changes when assumptions or inputs vary.

**Theorem.** A proposition accompanied by a proof in the formal system. Its empirical relevance depends on interpretation and applicability.

**Validation.** Assessment of whether a representation is adequate for its intended real-world use.

**Verification.** Assessment that a specified mathematical or computational object possesses its claimed formal property.

# Appendix F

## Reference Management and Research Notes


The reading pack includes `references.ris` and `references.bib`. Import either file into a Zotero collection named “Formalizing Minds and Societies.” Use the other as an interchange backup rather than importing both into the same collection without deduplication.

Suggested tags distinguish the sources' roles: `formal-methods`, `mathematical-psychology`, `measurement`, `identifiability`, `computational-anthropology`, `social-choice`, `ai-training`, and `normative-reasoning`. An additional access tag, such as `access/abstract` or `access/selected-full-text`, preserves how deeply a source was inspected for this report.

The file `source-relations.csv` records conceptual relationships proposed by this synthesis. For example, model-identification literature motivates the probe-design chapter, and AI theorem-proving studies provide precedent for a training method. These links are interpretive relationships in this reading map, not claims that one original author cited another.

For Obsidian, place the Markdown folder in a vault and open `README.md`. Keep theorem notes linked to the inventory's pinned source URLs. A useful note template records the informal question, formal statement, model assumptions, proof role, empirical bridge, and next extension. A Better Notes workflow can attach those notes to the relevant Zotero item while retaining the source URL and citekey.

The files support independent import and reuse in a reference manager or Markdown knowledge base.


# Appendix G

## Executive Summary

**A well-chosen formal model can show which observation separates competing explanations, which measurement bias changes a conclusion, and which participant loses under an apparently beneficial arrangement. The project makes those insights inspectable through 67 checked Lean declarations.**

The integrated release links seven areas of scientific reasoning: solidarity (16 declarations), measurement (9), identifiability (9), causality (6), learning (9), collective action (10), and aggregation (8). Its contribution is the connected artifact: definitions, proofs, concrete counterexamples, explanations, and a commit-linked verification record. Supporting lemmas and combined results make the argument reusable.

The models are minimal mathematical representations of social systems and research procedures. They isolate a relationship so it can be understood exactly and extended deliberately. The strongest examples achieve substantial generality within their definitions: a bias interval holds for every admissible integer input; two probes identify every pair in the candidate space; an information-limit theorem applies to every estimator receiving the specified observational object.

| Finding | Evidence and next use |
|---|---|
| All 67 declarations are present and named in the dependency audit. | Direct inspection of the pinned source and successful CI record; a separately reproduced build would add verification independence. |
| Formal approaches span the named biological and social disciplines. | Primary examples establish methodological traditions and concrete precedents. |
| Proofs make research assumptions and consequences inspectable. | The worked examples show how the formal structure guides a measurement, design, or interpretation question. |
| Verified data and checker feedback can support AI theorem proving. | Primary training reports establish a technical precedent for the proposed paired corpus. |
| Transfer to scientific interpretation is an experimentally testable opportunity. | Compare representations and checker access on held-out model families, with formal and semantic evaluation. |

Table: Evidence and Research Uses at a Glance

Five results offer especially clear entry points: the bounded measurement-bias interval; identification through a second probe; identical observations with different intervention effects; collective surplus with failed participation; and reversal of rates under pooling. Each makes a consequential distinction visible.

The immediate research program is to select one measurement or design problem, enrich its model, pair the proof with recovery analysis, obtain domain review, and test the resulting reasoning artifact in human or AI use. Context and retrieval provide an immediate route to using the material; parameter-updating training is a separate development route.

The source was inspected at commit `780f1b83aef15a9cf455566bab9df2a47d738074`. GitHub Actions run [36392008029](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36392008029) reports a successful Lean 4.19.0 build and audit for that commit. This edition adds interpretation and synthesis based on that recorded verification.

# Appendix H

## Source Access and Evidence Roles

The following register records the material inspected for this synthesis. The source identifiers connect the manuscript to the accompanying metadata files.

**R10: Axelrod, 1997.** Publisher abstract and metadata. Used for the agent-based cultural-modeling precedent; simulations not reproduced.

**R13: Benzmüller et al., 2020.** Primary arXiv abstract and revision metadata. Uses the inspected 2020 version; the original preprint appeared in 2019. No implementation audit.

**R07: Finkel et al., 2025.** Primary preprint abstract and metadata. Used to establish a formalization precedent; no reconstruction of the full method.

**R12: Fleming & Lau, 2014.** Publisher full-text sections on sensitivity, bias, and measurement limitations. Used for construct distinctions; no new meta-d-prime fitting performed.

**R18: Formalizing Soft Sciences Project, 2026.** Complete baseline book recovered from the project's supplied document archive; prose and source appendix inspected. The expanded monograph preserves its theorem identities and develops the exposition.

**R04: Guest & Martin, 2021.** Publisher abstract and metadata; bibliographic details checked against PubMed and author institutional record. Full article not reviewed.

**R08: Heath et al., 2008.** Author-hosted PDF abstract, introduction, and selected reduction-method sections; journal metadata checked against institutional record. No numerical reproduction.

**R09: Holliday et al., 2021.** Primary postprint abstract and metadata. The underlying published conference paper is identified by the authors; cited here via its inspected postprint. No independent rebuild.

**R17: Human Relations Area Files, n.d..** Official methods-page descriptions. Embedded lectures and slides were not fully reviewed; used as a methods gateway.

**R06: Huys et al., 2016.** Abstract and selected full-text sections in PMC concerning data-driven and theory-driven approaches. Clinical effect estimates were not extracted for the synthesis.

**R02: Lean Project, n.d..** Official manual sections on kernel acceptance, axiom printing, statement meaning, and stronger verification methods. Current manual; project runtime is separately pinned to 4.19.0.

**R20: Page et al., 2021.** Primary publisher abstract and bibliographic metadata, with PubMed author-list cross-check. Used for the stated purpose of the appraisal/reporting instrument.

**R11: Read et al., 2013.** Publisher abstract and bibliographic metadata; 2013 issue year confirmed, first online 2012. Full text restricted.

**R15: Ren et al., 2025.** Primary preprint abstract and metadata, including revised author list. Used for method precedent; no independent model evaluation.

**R16: Shalizi & Thomas, 2011.** Primary arXiv abstract and journal metadata. The full paper's mathematics was not independently audited.

**R19: Shea et al., 2017.** Primary publisher abstract and bibliographic metadata, with PubMed author-list cross-check. Used for the stated purpose of the appraisal/reporting instrument.

**R03: Society for Mathematical Psychology, n.d..** Official society description and journal/conference links.

**R01: Sodelin, 2026.** Full source of seven theorem modules, complete audit, workflow, verification receipt, bibliography, and main-commit workflow status.

**R21: Sterne et al., 2019.** Primary publisher abstract and bibliographic metadata, with PubMed author-list cross-check. Used for the stated purpose of the appraisal/reporting instrument.

**R05: Wilson & Collins, 2019.** Abstract, search-indexed captions and metadata. Direct publisher, PMC, and institutional full-text routes returned challenges; no full-text audit or reproduction.

**R14: Xin et al., 2024.** Primary preprint abstract and metadata. Used to establish a verified-data training precedent; benchmark claims not independently reproduced.

