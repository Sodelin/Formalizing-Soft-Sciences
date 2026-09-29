# 1. Abstract

A second measurement can separate explanations that a million repetitions of the first would leave tied. A proof can establish why, identify the needed information, and preserve the argument in a form that another researcher or computer can check. This monograph develops that scientific opportunity through a library of 67 Lean theorem declarations spanning network reach, measurement, identifiability, causality, learning, collective action, and aggregation. It expands the earlier project reader's guide into a sustained account of the definitions, lemmas, counterexamples, and research choices behind the development. The contribution is an integrated, inspectable research artifact and a program for connecting verified consequences to better questions, measurements, and experiments. The models are minimal mathematical representations that isolate relationships and support increasingly rich extensions. A complete source audit confirmed declaration coverage and a successful verification run at a fixed commit. A targeted literature map locates the work across psychology, biology, sociology, anthropology, normative reasoning, and AI theorem proving. Detailed worked arguments lead to a proposed evaluation of whether paired proofs and explanations improve scientific reasoning in AI systems. The resulting framework joins mathematical precision with an open-ended empirical program.

# 2. Introduction — the scientific opportunity

Two explanations fit every observation. More computation cannot choose between them because the distinction is absent from the information supplied. Then a researcher asks one different question, and the tie breaks. The crucial advance was a better observation. Formal reasoning can show exactly why it worked.

This is the promise of the development examined here. It creates an integrated library in which familiar scientific questions acquire precise mathematical form and checkable answers. The collection's seven modules can be inspected separately and understood together. Definitions, proofs, counterexamples, and source provenance give researchers common objects around which to disagree, revise, and build.

The work is new as a connected project artifact: this implementation, its explanatory map, and its verified path from assumptions to consequences. Its intellectual setting is an established tradition of mathematical and computational inquiry. That tradition supplies tools with which the present library can become a more capable research instrument.

The project connects a psychological question—how people think, judge, learn, and coordinate—to a mathematical question: **what follows from the explanation once we write it precisely?** The strength of that connection comes from making each stage explicit: the intended meaning, its mathematical representation, the consequence, and the observations that can test its use.

Consider the sentence, “Shared identity makes people cooperate.” It might mean that identity changes preferences, changes expectations of others, increases encounters, supplies a common signal, or makes sanctions more credible. Each interpretation suggests a different model. Formalization turns those interpretations into distinct mechanisms that can be compared.

The project currently supplies a vocabulary for asking sharper questions. Can an observation distinguish two mechanisms? Does a score difference survive measurement bias? Does a group have the skills required for a task? Does every necessary participant have an incentive to participate? Could a pooled statistic reverse the within-context comparisons? These are methodological foundations with applications to psychology and society.

Together, these minimal representations provide a basis for increasingly rich accounts of cognition and social organization. They isolate mechanisms, make their consequences exact, and identify the observations needed to connect them with research.

## 2.1 Three meanings of “formalization”

| Meaning | What the researcher produces | What it can establish |
|---|---|---|
| Mathematical specification | Equations, sets, relations, probability distributions, or explicit rules | An unambiguous model and deductions, assuming the mathematics is correct |
| Executable computational model | A program that generates predictions or simulates processes | Behavior of the implemented model under examined conditions |
| Machine-checked formal verification | A formal statement plus a proof accepted by a proof assistant, or a property checked by a model checker | That the specified property follows within the formal system and its trust boundary |

These activities complement one another. Mathematics specifies the relationships; execution reveals behavior under selected conditions; verification establishes formally stated properties. A research program can combine all three with empirical evaluation. The disciplinary examples below show the breadth of mathematical modeling and the more specialized role of proof assistants.

## 2.2 Verification and validation answer different questions

**Verification** asks whether the stated mathematical or computational object satisfies its specification. **Validation** asks whether that representation is adequate for its intended use in the world. Measurement validation is a further bridge: does the observation actually track the intended construct?

A model earns its role relative to a purpose. Predicting the next choice, explaining how learning occurs, and selecting an intervention place different demands on the same representation. Verification secures the deductive step, while validation investigates how that step serves the intended scientific use. Stating both tasks makes the research program stronger and easier to evaluate.

# 3. Method and provenance

## 3.1 What was inspected

The source of truth for the theorem explanations is [Formalizing Soft Sciences at commit 780f1b8](https://github.com/Sodelin/Formalizing-Soft-Sciences/tree/780f1b83aef15a9cf455566bab9df2a47d738074). The audit examined `Solidarity.lean`, all six foundation modules, `SocialScience/Audit.lean`, the CI workflow, the verification receipt, and the foundation bibliography. The complete earlier book, *How We Formalized Questions About Society*, was recovered as the baseline for this expanded edition. Its narrative, theorem guide, research register, and source appendix were examined alongside the pinned code.

The public proof files contain 67 `theorem` declarations. The audit names all 67. The current main-commit workflow reports success. Earlier documentation cites run 36391937036; that run also succeeded, but it belongs to commit a0663d5de45872ca4531067a886928f59ca48e61. This report uses the later main-commit receipt to avoid treating two commits as the same object.

The repository workflow rejects `sorry`, `admit`, custom `axiom` declarations, and `native_decide` in the project sources, runs the Lean build and axiom audit, and checks documentation/provenance. The recorded dependencies are standard Lean axioms or no axioms. Such logical axioms differ from substantive modeling assumptions: defining payoffs to ignore identity is a modeling choice even when no custom logical axiom is present. (Lean Project, n.d.; Sodelin, 2026)

## 3.2 Literature search

Searches were conducted on 28 September 2026. They combined targeted web queries with direct primary-source retrieval. Topics included the Society for Mathematical Psychology, computational model recovery, formalization of psychological theories, biological model checking, Lean voting theory, kinship algebra, deontic reasoning, and Lean-based AI training. The accompanying search log records the query groups, source selection, and material access failures.

Included evidence had to establish a directly relevant precedent, explain a methodological distinction, or support the AI-training discussion. Primary papers, author-hosted papers, research repositories, and official documentation were preferred. Promotional claims, unrelated search hits, and unverified priority claims were excluded from the synthesis. Some sources were available only as abstracts; their use is restricted accordingly in the bibliography.

The method is a source audit combined with a targeted narrative evidence map. The audited objects are definitions, theorem declarations, dependencies, and verification records. The literature component establishes selected precedents and informs a proposed research program. Search completeness and access depth are assessed in the process review and source register.

# 4. Findings

## 4.1 What mathematical psychology does

Mathematical psychology constructs precise accounts of psychological phenomena and investigates their consequences. The Society for Mathematical Psychology explicitly includes mathematical methods, formal logic, and simulation within its scope. Its journals and recurring conferences demonstrate an established research community. (Society for Mathematical Psychology, n.d.)

Examples of its questions include: how choice probabilities depend on preferences; how evidence accumulates before a decision; how learning changes with feedback; whether a measurement scale preserves comparisons; and how confidence relates to accuracy. Mathematics can reveal relationships that are hard to see in verbal descriptions, including parameter tradeoffs and cases where rival explanations make the same prediction.

Here is an illustrative learning equation:

`Q(next) = Q(now) + alpha × (outcome − Q(now))`

The variable `Q` represents an expectation, and `alpha` controls how much it moves toward the observed outcome. If `alpha = 0`, the expectation does not change. If `alpha = 1`, it becomes the latest outcome. Values between zero and one yield a weighted average. These exact consequences identify what the equation predicts and give empirical researchers properties to investigate.

A mathematical investigation could ask whether the expectation remains bounded or converges under particular input sequences. A psychological investigation would additionally ask whether this update rule explains actual behavior better than alternatives and whether the fitted parameter has the interpretation claimed.

## 4.2 What computational psychology does

Computational psychology emphasizes explicit information-processing mechanisms and executable models: rules that perceive, remember, infer, choose, and learn. It overlaps heavily with mathematical psychology. The difference is an emphasis, not a rigid border. Some models are compact equations; others are simulations, cognitive architectures, neural networks, or symbolic programs.

A useful distinction concerns **modeling a theory** versus **fitting a description of data**. A regression may describe how two variables co-vary without specifying the process producing the relationship. A generative cognitive model specifies a process that could produce responses, errors, or reaction times. Competing generative models can fit similar observations, making model comparison and design central to the investigation. Guest and Martin argue that computational implementation strengthens theory building by requiring researchers to make otherwise implicit commitments explicit. (Guest & Martin, 2021)

For a typical study, researchers define competing mechanisms, simulate their predictions, collect behavior, fit parameters, check whether parameters and model identities can be recovered, and evaluate predictions beyond the fitting data. Wilson and Collins provide a practical guide to careful use of behavioral models, including recovery checks. These checks connect the behavior of the implementation to the interpretation of its fitted parameters. (Wilson & Collins, 2019)

## 4.3 Neighboring approaches

| Approach | Central question | Relationship to the current release |
|---|---|---|
| Psychometrics | What does a score measure, and are comparisons meaningful? | The additive measurement examples isolate which comparisons survive common and differential offsets. |
| Computational cognitive science | Which processes generate behavior? | The learning module tracks which deterministic hypotheses remain compatible with specified evidence. |
| Computational psychiatry | Can mechanistic models and predictive data analysis improve understanding of psychiatric phenomena? | A future application linking formal properties to a specified mechanism and clinical evidence. |
| Computational social science | How do interaction rules, networks, institutions, and data explain social patterns? | Solidarity and collective-action modules separate network structure, capability, and participation. |
| Formal methods | Does a precisely specified system possess a stated property? | This is the project's most direct present contribution. |

Computational psychiatry includes both data-driven prediction and theory-driven modeling of interpretable processes. Huys, Maia, and Frank describe their relationship and the challenges of translating between levels. This provides a research setting in which formal properties can be connected to mechanistic questions and assessed against clinical evidence. (Huys et al., 2016)

## 4.4 Is this widespread across disciplines?

**Mathematical and computational approaches have established traditions across biology, psychology, sociology, anthropology, and comparative cultural research. Proof assistants such as Lean contribute a specialized form of assurance within that landscape.** The following evidence map shows what each approach makes possible. It documents examples rather than estimating disciplinary adoption rates.

| Field | Established kinds of modeling | Direct precedent found | Scientific opportunity illustrated |
|---|---|---|---|
| Biology | Dynamical systems, stochastic processes, population and biochemical models | Heath and colleagues used PRISM to analyze a model of FGF signaling. (Heath et al., 2008) | Analyze temporal and probabilistic properties of a specified pathway |
| Psychology | Mathematical cognition, psychometrics, learning and decision models | Finkel, Fougea, and Le Roux formalized a stress theory using automata. (Finkel et al., 2025) | Translate a verbal process theory into explicit states and transitions |
| Sociology and related social theory | Networks, agent-based models, games, and institutional rules | Axelrod modeled cultural influence; Holliday and colleagues formalized voting properties in Lean. (Axelrod, 1997; Holliday et al., 2021) | Connect local rules to collective patterns and verify properties of decision procedures |
| Anthropology | Formal kinship, cultural transmission, archaeological and social simulation | Read, Fischer, and Leaf described computational algebraic analysis of kinship terminology. (Read et al., 2013) | Study the internal structure of culturally interpreted symbolic relations |
| Ethnology / comparative cultural research | Comparison of cultural patterns, coding and sampling frameworks, sometimes formal and computational models | HRAF's methods materials address comparative sampling and dependence between societies. (Human Relations Area Files, n.d.) | Design comparisons with explicit sampling and dependence assumptions |

Ethnology often refers to comparative study across cultures, while ethnography typically involves situated description and interpretation. Usage varies across national academic traditions. Formal comparison and situated interpretation can contribute to a shared investigation.

The biology example is especially informative: probabilistic model checking examines formally specified system behavior, sometimes using exact or approximate numerical techniques. Its guarantees differ from a general theorem proved in Lean. The two methods offer complementary forms of assurance whose scope follows their stated mathematical guarantees. (Heath et al., 2008)

Kinship algebra makes the prospect of formalizing social concepts especially tangible. Relations can be composed and their internal rules investigated. Ethnographic interpretation establishes which local categories the relations represent; the algebra then makes their implications available for systematic analysis. (Read et al., 2013)

## 4.5 Why isn't everything written in Lean?

Several obstacles concern the scientific task itself; others concern implementation and incentives. The following is a synthesis and assessment, not a measured causal ranking of adoption barriers.

**Constructs are contestable.** The meanings of intelligence, trust, distress, solidarity, or fairness can change with theoretical commitments and practical aims. Formalization exposes that choice but cannot make it disappear. Competing formalizations may be useful because they reveal exactly where interpretations diverge.

**The observation process is part of the problem.** A score is shaped by an instrument, context, interpretation, and measurement error. Proving a relationship among latent variables does not prove that questionnaire responses instantiate it. The measurement module makes this issue visible even with simple integer arithmetic.

**Identification can fail before estimation begins.** Different mechanisms may produce the same observations. More participants reduce some sampling uncertainty; they do not automatically repair structural ambiguity. The identifiability and causality modules show exact versions of this problem. Network-specific research gives richer examples involving homophily and social influence. (Shalizi & Thomas, 2011)

**Systems change.** People respond to institutions, labels, incentives, and one another. A model useful in one time or community may fail elsewhere. Heterogeneity may be scientifically substantive rather than noise to average away.

**The cost must match the research risk.** Formal proof requires precise definitions, mathematical libraries, tool expertise, maintenance, and review. Sometimes a simulation, a standard analytic argument, or a better experiment resolves the key uncertainty more efficiently. Lean is especially valuable when a reusable result, subtle inference, or consequential algorithm needs strong assurance.

**Qualitative evidence does different work.** Interviews, ethnography, archival interpretation, and participatory inquiry can identify categories and mechanisms that a model has omitted. They can improve formalization by revealing that the specified question was wrong. Precision is useful when it preserves the distinctions the research needs.

**Empirical and normative questions remain.** A proof that a policy meets a chosen fairness criterion does not establish that this criterion should govern a particular institution. A proof of logical consistency does not resolve whose interests, histories, or values should shape the rules.

## 4.6 How to formalize a psychological or social claim

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

### A complete miniature example from the verified source

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

### From a therapy narrative to a research model

For a future cognitive behavioral therapy (CBT) research project, a model could represent expectations, observations, avoidance choices, and belief updates. A proof could establish that an update stays within bounds, that a task leaves two mechanisms tied, or that a new observation can separate them. The next investigation would connect those mechanisms to measured behavior and intervention outcomes. This sequence turns a broad clinical narrative into a series of answerable research questions.

A psychopathology model could similarly represent interactions among processes or symptoms. Its parameters would acquire substantive interpretations through measurement and model comparison. The value of formalization would be the clearer link between a proposed mechanism, its mathematical behavior, and the evidence needed to assess it.
