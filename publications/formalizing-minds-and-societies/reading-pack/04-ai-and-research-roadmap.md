## 4.9 What verified social-science models could contribute to AI

The prospect is compelling: a language model could produce an explanation whose deductive core is independently checkable. When the explanation fails, the failure could identify a missing premise, an invalid step, or an underdetermined question. These are concrete capabilities that a research program can develop and measure.

### Four different routes from a library to a model

| Route | What happens | What must be evaluated |
|---|---|---|
| Context or retrieval | Relevant definitions and results are supplied when answering a question | Does the model select the right theorem and preserve its assumptions? |
| Tool-assisted reasoning | The model proposes statements or proofs and receives checker feedback | Does checking reduce errors while the formal statement still matches the intended question? |
| Supervised training | Model parameters are updated using curated examples | Does learning generalize beyond copied statements and familiar proof patterns? |
| Reinforcement learning with verification | A training process uses formal feedback as part of its reward | Does the reward encourage the intended reasoning without weakening the task or exploiting the evaluator? |

Context and retrieval make the material useful immediately by changing the information available to an answer. Supervised and reinforcement training require a separate pipeline that updates model parameters. Publicly releasing a corpus makes that reuse possible; actual inclusion in a provider's training data depends on that provider's choices.

There is direct precedent for the training route in formal mathematics. Xin et al. (2024) report training with a large synthetic Lean proof corpus. Ren et al. (2025) describe a later prover using subgoal decomposition and reinforcement learning. These reports establish that formal proof data can be part of a productive training pipeline for theorem proving. The next question is transfer: which scientific and social reasoning skills improve when the training material pairs formal structure with substantive interpretation?

### What the present corpus could teach

The most promising targets are disciplined distinctions: reachability versus trust, observed score versus latent value, observational fit versus causal identification, total surplus versus individual participation, and exact consistency versus probabilistic evidence. A model that reliably preserves these distinctions would make fewer specific reasoning errors.

Pairing Lean with an interpretation gives a learner both the deductive structure and its intended scientific meaning. In result 13, the labels are arbitrary and causally inert. If a training example says only “heterogeneous cooperation exists,” a learner may acquire the slogan and miss the reason it holds. A better example pairs the statement with its definitions, a plain-language interpretation, and an explanation of which mechanism the model isolates and how that mechanism could be extended.

One promising unit of training data would contain the research question, formal objects, theorem statement, checked proof, interpretation, boundary conditions, a nearby false claim, and a counterexample to that false claim. It would also record source provenance and review status. This is a proposed design for a dataset; no such training run was performed here.

For instance, the true statement is that common additive offsets preserve differences. A nearby false statement is that all group-specific offsets preserve differences. The counterexample makes the missing assumption visible. A second nearby claim—“therefore this instrument is unbiased”—does not follow from either theorem. Teaching the model to identify that change in claim type may matter more for scientific communication than teaching it to reproduce the arithmetic proof.

### The reward must be attached to the right statement

A checker accepts a proof of the statement it receives. If a system silently weakens the conclusion or strengthens the premises until the task becomes trivial, successful checking no longer measures success on the original question. The statement must therefore be fixed or independently reviewed before the proof is scored.

Similarly, inconsistent premises allow arbitrary conclusions in classical logic. A proof that follows from inconsistent assumptions is a derivation, but it does not provide a useful model of a possible case. Vacuous universal statements can also be correct for an empty domain while being misleadingly described as claims about a populated society. Verification quality therefore includes premise and interpretation review, not only a compiler success flag.

The official Lean documentation distinguishes a valid proof from the meaning of its statement and describes stronger checking procedures for higher-risk settings. This report inspected standard source and CI evidence; it did not run those stronger external checks. (Lean Project, n.d.)

### How to test transfer without rewarding memorization

A credible study should compare the same base model under carefully matched conditions: no supplied corpus, prose-only explanations, formal code only, paired prose and formal material, and paired material with access to a checker. These are proposed experimental arms. They would separate the value of the information, its presentation, and verification feedback.

Training and evaluation should be split by underlying model family or theorem dependency group, not merely by randomly distributing individual declarations. Result 66 directly reuses result 33, and result 64 packages earlier comparisons. Placing one in training and the other in testing could inflate apparent generalization. Splitting paraphrases of the same example across the boundary would create a similar problem.

Useful test tasks include translating a verbal claim into a formal statement; locating missing assumptions; detecting that a question is underdetermined; finding a counterexample to an overgeneralization; explaining why a proof does not establish a clinical claim; and distinguishing a normative premise from an empirical observation. Some tasks have checker-verifiable answers. Others require independent, blinded domain review of semantic fidelity.

The evaluation should separately report proof success, correct statement selection, assumption preservation, unsupported empirical claims, uncertainty calibration, and performance on new domains. A higher proof pass rate alongside more unjustified social conclusions would not be a successful outcome for this project.

The proposed primary scientific-communication endpoint is the rate of unsupported conclusions on held-out scenarios, accompanied by accuracy and abstention measures. A useful improvement would reduce unsupported claims without achieving that reduction merely by refusing every question. Its practical threshold should be specified before data collection with the intended users and the consequences of errors in view.

No effect size is available for this proposed intervention. A future analysis might report paired accuracy differences or changes in error rates with uncertainty intervals. Because questions share templates and model families, uncertainty should respect that clustering. Treating every generated paraphrase as an independent observation would create misleading precision.

### Ethics requires a second kind of discipline

Formal ethical reasoning can specify obligations, permissions, prohibited actions, priorities, and exceptions. Benzmüller et al. (2020) describe a framework using higher-order logic and automated reasoning to investigate normative theories. This establishes a route for extending the project into explicit normative theories.

A useful distinction separates logical coherence, empirical consequences, and normative justification. A policy can be internally coherent under a set of values while relying on false empirical beliefs. It can generate an intended consequence while being unacceptable under another defensible value commitment. A theorem can expose those dependencies without settling them.

For example, `Accepts` in the collective-action module means reward covers modeled cost. Renaming that predicate “consent” would not add voluntariness, adequate information, freedom from coercion, or the ability to withdraw. Similarly, an allocation that satisfies two participation inequalities need not satisfy an independently defined equality or priority principle. The gap is conceptual, not a missing arithmetic tactic.

This is where a paired corpus could be particularly useful. It could require a model to say which ethical premises are assumed, which consequences have been proved, and which empirical facts would still need to be established. The goal would be auditable reasoning about values and consequences: a model that can state an obligation, preserve its exceptions, identify a conflict, and explain how a conclusion changes when a premise changes. Those capabilities would be meaningful targets for an evaluation of ethical reasoning.

# 5. Conclusion

The project demonstrates that selected methodological distinctions can be encoded as small, reproducible Lean developments. Its strongest present contribution is a clear chain from definitions to conditional consequences. It also supplies instructive counterexamples to claims that are easy to overstate in ordinary language.

The next advance should connect that chain to a consequential research decision: a measurement that separates mechanisms, an assumption whose failure changes an inference, or a model property whose verification protects an empirical analysis. Progress can be measured by the new research decisions the formalization makes possible.

For AI, verified libraries can support retrieval, tool-assisted reasoning, and carefully designed training studies. Existing theorem-proving research makes that prospect credible. The specific claim that formalized psychology or ethics improves broad social reasoning remains a research hypothesis. It deserves a test designed to detect both gains and overconfidence.

# 6. Deconstructive analysis — tracing a broad claim downward

Consider the assertion, “A verified psychological model gives an AI a correct understanding of people.” It contains several transitions. The natural-language theory must be represented faithfully; the formal proof must establish the intended property; the model must capture relevant processes; the observations must measure those processes; the trained system must use the model correctly; and its behavior must generalize to new settings.

The 67-theorem audit primarily strengthens the deductive transition. The literature supplies precedents for the surrounding activities. It does not collapse the chain into one guarantee.

This diagnosis is useful because each transition has a distinct failure test. Compare the formal statement with the prose to test semantic fidelity. Inspect proofs and dependencies to test formal correctness. Compare models and data to test empirical adequacy. Review instruments to test measurement validity. Evaluate held-out behavior to test transfer. No single score can substitute for this structure.

The same method applies to a narrower statement: “Shared identity supports cooperation.” Does identity alter expected behavior, preferences, contact opportunities, or enforcement? Does cooperation mean contribution, persistence, or mutual obligation? Does the conclusion concern a possible equilibrium, a likely outcome, or a morally justified institution? The present model answers one incentive question after most of those choices have already been made.

# 7. Reconstructive analysis — building upward from a useful result

A productive extension could start from a measurement problem in metacognition. Define the observations and candidate mechanisms, establish which parameters or contrasts are identifiable, add a realistic observation model, and investigate recovery under the proposed design. Only then ask whether the model fits new data and improves on alternatives.

A second route starts from team capability. Replace the current coverage predicate with a finite assignment model including capacity and scheduling. State participation or access conditions separately. Prove an informative feasibility or failure result, then examine whether the formal variables correspond to real operational constraints. This would extend the current sociology-inspired work toward an application while connecting the scheduling result to the institution's observed constraints.

A third route starts from AI scientific explanation. Build examples in which a theorem is valid but its tempting broader interpretation is not. Train or prompt a model on paired correct and incorrect interpretations, then assess new model families with blinded review and checker feedback. The target is a reduction in a specified reasoning error, giving the broader ambition of improved understanding an observable test.

These paths all follow the same discipline: select a bounded question, preserve provenance, identify the decisive assumption, and choose an evaluation that could reveal failure. The excitement lies in making an elusive question tractable enough to challenge.

# 8. Middle-out synthesis — the most useful place to work

A model family tied to a measurement, experiment, or institutional problem provides a productive scale for this research. The family is broad enough to compare meaningful alternatives and precise enough to connect a proof to an actual decision.

The present library is well positioned to support that scale because several modules connect naturally. Identifiability describes what observations distinguish. Measurement specifies how observations arise. Causality distinguishes observational equivalence from intervention consequences. Learning tracks compatibility with evidence. Aggregation describes information and comparisons lost in summaries. Collective action connects capabilities to participation constraints.

Those links organize a research program around a clear criterion: an extension should make a previously ambiguous scientific decision more explicit and testable. A theorem that changes an experiment is a particularly tangible form of progress.

# 9. Glossary

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
