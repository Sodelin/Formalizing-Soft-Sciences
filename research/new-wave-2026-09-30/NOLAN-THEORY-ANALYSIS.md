# Nolan's theory of missed scope and generative generalization

29 September 2026 Pacific / 30 September UTC. Original hypothesis: Nolan Downard. This report reconstructs his proposal and develops a mathematical interpretation. The definitions and mechanisms proposed here are analytical constructions, not an established theory of model internals. The earlier NANUQ dossier and New Wave protocol are supporting artifacts; neither constituted this analysis.

## What was missing from the earlier response

Nolan asked why an assistant repeatedly finds satisfactory deliverables while missing a more complete system interpretation and a more transferable structure. He did not merely ask for a checklist requiring stronger theorems. His proposal concerns the production of the search space itself: which possibilities become visible enough to pursue, and whether the assistant must wait for the user to name an absent axis.

The earlier response extracted a useful instruction but then treated its workflow implementation as though it completed the conceptual analysis. That skipped the proposed causal account, the difference between two scope failures, the meaning of a shadow, and the possibility that an auditor inherits exactly the same narrow search. Time spent does not establish analytical completeness. These missing questions are the reason for this report.

## My reconstruction of your theory

The theory has several separable claims. They should not be accepted or rejected as one bundle.

| Nolan's claim, reconstructed | My interpretation | Status |
|---|---|---|
| Finding a solution differs from finding the best useful solution | The readily expressible task can be satisfied while the user's larger outcome remains underexplored | Logical distinction; plausible diagnosis of this interaction |
| Decomposition can encode the wrong goal | Breaking a narrow representation into excellent subtasks preserves its omissions | Can be demonstrated formally; occurrence/frequency is empirical |
| Generic checking can reproduce the problem | An evaluator supplied the same representation may certify local success without generating omitted alternatives | Conditional mechanism, not a claim that every auditor does this |
| A task is a system, not merely a requested object | Internal mechanisms, dependencies and failure paths matter to the outcome | Requires a declared outcome and system boundary |
| That system also participates in larger systems | Value and transfer depend on consumers, environments and shared structure | Requires explicit connections rather than unlimited scope expansion |
| Generality is revealed by the system's shadow | Observable invariants can expose a structure that applies across apparently different tasks | Productive metaphor; mathematical meanings must be specified |
| Specific user questions reveal unnamed search dimensions | Naming level, bound or transfer can change the candidate problems considered | Supported as an interpretation of the reported interaction; full prompt trace absent |
| A recurrent outside question may compensate for the omission | An intervention should generate competing representations/targets, not just assess the current answer | Proposed remedy; effectiveness needs measurement |

My strongest interpretation is: **the assistant's failure can occur before proof or implementation, when it constructs the space of plausible answers.** Good execution within that space does not repair the fact that the important answer was never represented.

The reward-language explanation adds a further claim: that training or completion incentives systematically favor such spaces. This is possible, but these interactions do not isolate that cause. Narrow instructions, familiar methods, context limits, resource allocation, learned response patterns and misestimated user intent can produce similar observable behavior. We should distinguish the observed scope failure from an explanation of its internal origin.

## Two failures that should not be collapsed

An internal-scope failure occurs when the answer omits mechanisms needed for the intended outcome. A screening-room website could satisfy every page specification while failing the actual experience because scheduling, permissions, accessibility or an external dependency was never included. The point is not that all websites must have these features; it is that the user's intended outcome determines which are necessary. Adding more pages cannot fix a missing decisive dependency.

An external-scope failure occurs when the solved mechanism is unnecessarily confined to its original application, or when its interaction with a larger system is ignored. A theorem stated for one level might actually depend on a bounded local configuration independent of level. Its original application is then a special case of a broader structure. Alternatively, a useful module may fail in its receiving environment because a required interface is absent.

These failures differ. Internal completeness does not imply transferable generality. Transferability does not imply the original system is complete. A rigorous fragment can transfer widely while omitting the learning mechanism needed to make a clinical claim. Conversely, an application can work fully for its intended use without admitting a useful theorem about all related applications.

The desired search should examine both: what must be present for this outcome, and what the actual mechanism permits beyond this instance.

## A formal model of the first failure

Let U be the user's intended outcome, E the available evidence, and r a representation of the task. The representation includes objects, mechanisms, boundaries, assumptions and possible operations. Let C(r,E) be the candidate targets or answers generated under that representation. An execution procedure returns an answer a from this set.

A local acceptance predicate L(r,a) says that a satisfies the represented task. An outcome predicate G(U,a,E) says that a achieves the intended outcome under the declared evidence and assumptions. These predicates are deliberately different.

It is possible that L(r,a) holds while G(U,a,E) fails. For example, a specification asks for two working pages, while the user outcome also requires a functional booking integration. Both pages can be correct without the integration. This is a witness to the logical distinction, not a universal judgment about software assistants.

A decomposition into subtargets t1,...,tn can prove every local obligation and still leave G unproved. To infer G, we need an independently justified coverage implication:

    (all required subtargets are achieved) -> intended outcome is achieved.

The important issue is how the required subtargets were discovered. Defining G to mean exactly the completed checklist would make the implication trivially true and erase the problem. U must remain anchored to the real intended outcome and environment.

This formalization shows why perfect verification of selected subtasks is insufficient. It does not show that decomposition itself is inefficient: when the coverage implication is justified, decomposition can be excellent. The hypothesis concerns premature decomposition of an inadequate representation.

## A formal model of unseen better targets

Let T be a specified universe of possible targets. For target t, distinguish validity, outcome relevance, strength, transfer and resource cost. A preference relation on targets captures the user's priorities. In many research settings it is a partial order rather than one universal score: a larger domain can require less faithful assumptions, and a sharper bound can be less useful than a computable method.

The represented candidate set C(r,E) can be a strict subset of T. We can verify that a returned target is best among C(r,E) while a superior target lies outside it. This is the formal core of the missing-map claim.

Suppose a procedure only returns elements of C(r,E). If t* is outside that set, the procedure cannot return t*, regardless of the number of comparisons it performs inside the set. If generation is stochastic, the same statement applies when t* has zero generation probability under the fixed procedure. Positive but tiny probability gives a different problem: discovery may be possible yet implausible within budget.

This is a conditional theorem about a defined procedure. Actual language models do not have a conveniently exposed fixed candidate set; their implicit representations can change during generation. We cannot identify their true support from one transcript. The formal model explains a possible failure mechanism without claiming to measure model internals.

Your objection to generic checking is strongest here: evaluating members of C is different from changing C. An auditor that generates new representations can help. An auditor restricted to testing the current answer cannot fix an excluded target. What matters is its action, not whether it is named an auditor or assigned to a different model.

## What the shadow could mean mathematically

One useful interpretation is an observation map O:S->Y from hidden systems to observed behavior. A shadow is O(s). A property f:S->Z is exactly recoverable from the shadow if some decoder d:Y->Z satisfies f=d composed with O on the admitted systems.

This occurs precisely when f is constant on each fibre of O: whenever two systems have the same observation, they have the same f. The necessity follows immediately from applying d to equal observations. For sufficiency, choose the shared f-value on each realized observation; an everywhere-defined decoder additionally needs a value on unrealized observations or a suitable codomain assumption. This detail matters when translating the statement into Lean.

Consequently, shadows can support some invariants without determining their sources. Two different mechanisms can have identical observed behavior. A perfect match of observations does not automatically reveal hidden topology, causal direction or psychological explanation. Statistical similarity is weaker still than exact equality.

A second useful interpretation is a structure-preserving map between different tasks. Let phi:S->S' map source systems to target systems, and h:Y->Y' map observations. A commuting relation

    O'(phi(s)) = h(O(s))

states exactly how an observation survives transfer. Even this relation only transfers what it says. To transfer a theorem, its assumptions and desired property must also survive or be replaced by explicitly justified conditions.

For psychology, this makes your idea productive: ask which conclusions are identifiable from the available behavioral shadows, which hidden mechanisms remain indistinguishable, and which new measurement or intervention separates them. Formal mathematics can characterize the distinctions. It cannot supply the missing empirical link just by declaring the maps.

Your metaphor therefore suggests observation, quotient and transfer structures. I do not yet see evidence that one topological construction captures all of it. A theorem about self-similarity would require a specified object, transformation and invariant; shared features alone are not self-similarity.

## The NANUQ example as a mechanism, not a slogan

The [experiment dossier](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/main/research/new-wave/NANUQ-EXPERIMENT-DOSSIER.md) records the proof boundaries. Here the key conceptual change is from network-level classification to dependence of the obstruction.

After opening hybrids into adjacent paired tips, a circular coefficient uses two anchors and at most four boundary labels. Keeping those labels and removing both copies of every unused hybrid label preserves the necessary quartet information. Network level is not part of that local dependence. A uniform finite certificate can then control every finite level, with the source hypotheses retained.

The question 'where is level used?' can expose a different proof architecture. It does more than request the next larger instance. The generalization required a representation and restriction argument; it is not justified merely by the observation that a variable is absent from one formula.

The five-taxon result illustrates a separate transformation: equality of normalized parameter-inequality catalogs can make a smaller test collection sufficient. It does not supply five-label compression of each original configuration. The multicopy result transfers preserved quartet sets and split support to a larger abstract class while losing some full tree-family and probability information.

Thus there are at least three distinct generalization operations: remove an irrelevant level bound through locality; reduce a test catalog through redundancy; and transfer through preservation of selected observables. The generic word generalize conceals these different mechanisms. A capable discovery procedure should identify the applicable operation without requiring the user to supply its name.

## My proposed generative mechanism

This part is my proposal derived from your theory, not something you already specified in full. It changes what candidates are generated before deciding whether the answer is satisfactory.

First, retain the user's outcome separately from the current target. Produce a small mechanism representation: what produces the result, what observations reveal it, what restrictions are stated, and which external connections affect its value. This is a provisional model, not a claim to fully illuminate the subject.

Second, apply operations that propose a different target or representation. Useful operations include removing a restriction not used in the argument; replacing instance classification with an invariant or bounded obstruction; substituting a smaller sufficient interface for a whole-paper implementation; introducing a missing causal mechanism; strengthening sufficiency to characterization; separating an observable from lost hidden information; and transporting a preserved invariant into another class.

Third, each operation must output a concrete alternative and a discriminating investigation. For NANUQ: 'replace the fixed-level target with all finite levels; determine whether restriction to the coefficient's labels preserves the representation and quartet sets.' That is generative. 'Check that we generalized' is not.

To discover an axis whose name the user has not supplied, temporarily replace application-specific objects with symbolic objects and reconstruct the properties used by each decisive step. An unused restriction suggests deletion. A used restriction suggests a different question: what weaker structural property would make this step work? Search for another class satisfying those recovered properties. This can reveal a generalization without first listing familiar labels such as level, size or noise. It is still fallible: proof dependencies can hide restrictions in definitions or imported results, and an implementation can omit real-world dependencies. Recovering dependencies is an evidence-producing investigation, not a mechanically reliable readout of every possible abstraction.

Fourth, pursue the cheapest meaningful investigation that could change target selection. It might be a derivation, structural lemma, small counterexample, source search or dependency trace. Its objective is to decide which question deserves execution, not merely to produce another finished item. The candidate can fail; rejecting an attractive but invalid transfer is useful discovery evidence.

Fifth, allocate further work among these alternatives and the existing target. Use explicit user priorities and uncertain estimates of significance, feasibility and cost. Early uncertainty should be visible rather than converted into a confident numerical utility. A policy that always selects the easiest certificate would recreate the original failure even with this machinery.

Finally, use milestone triggers or an external orchestrator to request this generation operation before substantial implementation, after the first working mechanism, and before closing. A prompt alone cannot guarantee the trigger actually fires. A runner can require that an alternative/test record exists before proceeding, but semantic quality still needs evidence. Runtime enforcement of record presence is different from a mathematical guarantee of good research.

This intervention is not outside every possible learned bias. It is a deliberate attempt to change the procedure's available actions: generating and testing new targets becomes explicit. Independent agents can supply genuinely different operations or evidence, but merely multiplying agents with the same narrow instructions is no guarantee.

## Can this find the optimal generalizable structure?

Sometimes, within a declared finite setting. Suppose we enumerate a finite target family, decide validity for every member, specify an agreed scoring function, and accurately evaluate every score. We can prove that selecting an argmax is optimal within that family. If the relation is a partial order, we can instead compute the nondominated candidates. Neither conclusion establishes that the family included the important omitted target.

For a bounded computational class, a complete generator and decidable predicates can support a stronger guarantee about that class. A proof that every possible obstruction reduces to a bounded witness can turn finite verification into an unbounded theorem. NANUQ's locality/restriction step exemplifies this latter pattern; it does not make all research discovery finite.

For unrestricted mathematical discovery or open-ended product design, the necessary assumptions are unavailable. We do not have a known complete space of meaningful targets, a universal measure of usefulness or a generally executable test of every possible claim. An instruction to search for the perfect answer cannot manufacture those objects.

The defensible ambition is therefore: **systematically expose consequential targets that the current representation omits, and establish optimality where a bounded domain or reduction permits it.** This is stronger than vague checking and weaker than a universal promise to find the best answer.

## What is worth formalizing in Lean

Four families would clarify the theory rather than just encode a checklist:

1. A counterexample to 'all local tasks passed implies intended outcome achieved' without a coverage implication.
2. A candidate-generation limitation: an output restricted to C cannot equal a target outside C; and finite optimality over C does not imply optimality over a larger T.
3. Observation/transfer lemmas: recoverability on fibres and conditions under which a map preserves a requested conclusion.
4. A general finite-obstruction reduction: if every failure in an unbounded class restricts to a failure in a finite checked class, absence of the latter excludes the former.

These would formalize useful logical distinctions. The first two are elementary and should not be advertised as discoveries or consume a large foundation project. The third may reuse existing repository work. The fourth becomes scientifically substantive when instantiated with a real representation and correspondence proof.

A formal workflow can also prove facts about an implemented runner: for example, a transition to execution requires an attached candidate proposal. That proves the runner's transition rule, not the proposal's relevance, completeness or originality. Proving a Lean proposition does not alter the language model's reward function or compel real-world adherence.

No Lean compilation or new formal theorem is claimed by this report. We should select a concrete application before building a large formal theory around these definitions; otherwise we would repeat the foundation-first failure you identified.

## How to evaluate the proposal without rewarding paperwork

Use held-out starting snapshots under matched total budgets. Compare ordinary task execution, execution plus correctness auditing, and execution plus the generative representation intervention. Where resources permit, add a specific-human-question condition. Hold model, effort, tool access and starting evidence fixed where possible; record variation otherwise.

Score the strongest correct result, coverage of the user's outcome, important restrictions removed with evidence, failed transfers correctly rejected, and useful downstream capability. Record total discovery/proof/verification/documentation cost when measurable. Do not score the number of proposed axes or completed checks as success.

Several runs and blinded judgments can reduce selection effects. Include tasks where generalization is easy, tasks where it requires new machinery, tasks already appropriately scoped and tasks where a broader claim is false. Known NANUQ answers make that case useful for illustration but contaminated as a discovery benchmark.

If the intervention improves target selection but adds enough overhead to erase the gain, that matters. If it mainly produces irrelevant broad claims, it fails. If ordinary auditing already generates equally good alternative representations, the contrast between checking and generation needs refining. A successful result would support the behavioral intervention; it would still not identify the internal reward mechanism.

## My assessment

The most useful part of your theory is its insistence that the search representation itself needs to be generated and challenged. It explains why a task can be beautifully completed yet remain much less significant than a nearby formulation, and why a user asking one precise question can unlock a disproportionately larger result.

The shadow idea supplies a promising language for preserved observations and cross-task structure, especially in psychology where hidden mechanisms may be observationally indistinguishable. Its strongest formal version must include information loss and identifiability, not assume that matching shadows reveal the entire system.

The causal story about reward is not established, and neither full illumination nor universal optimal generalization is currently a precise attainable guarantee. Those limits do not undermine the narrower, actionable theory. We can model target exclusion, prove preservation/reduction results, and evaluate a generative intervention without claiming access to internal motives.

This report provides the conceptual analysis that was previously missing. It is a candidate formal account and research proposal, not a completed empirical theory, a fully implemented autonomous controller or an exhaustive research corpus.
