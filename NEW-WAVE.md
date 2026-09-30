# New Wave: discover the right target, then execute it

Revision 2, 29 September 2026 Pacific / 30 September UTC. This revision corrects the first version's completion-centered framing. Checking work against a registered question does not establish that the question was worth choosing or sufficiently broad. There are two goals: discover the strongest useful structure and target, then execute and verify an answer. This supplements the [source-first open-problem gate](research/publication-audit-2026-09-29/OPEN-PROBLEM-GATE.md) and preserves active bounded task packets.

For research, the intended chain is **target discovery ↔ external problem → checked contribution → specific new capability → subsequent research or submission**. Subsequent use is a claim to substantiate when made, not a requirement for already having an adopter. Read the [NANUQ experiment dossier](https://github.com/Sodelin/Work-on-Samuel-Alexander-Research-/blob/main/research/new-wave/NANUQ-EXPERIMENT-DOSSIER.md) for the motivating evidence.

The [analysis of Nolan's theory](research/new-wave-2026-09-30/NOLAN-THEORY-ANALYSIS.md) explains the original hypothesis, the proposed formal model, its limits, and the dependency-driven generative intervention. This workflow is an application of that hypothesis, not a validated theory of model internals.

## 0. Challenge the target, separately from checking execution

This universal instruction applies to research, software and other tasks. Use it before substantial implementation, after the first working result/design, and before closing:

> Step outside the current task decomposition. What outcome is actually wanted? What mechanism produces it? Which restrictions does that mechanism truly use? What missing subsystem or external dependency could defeat the outcome? What explicit structure-preserving transfer could make the result more useful? Choose the most consequential plausible alternative and perform the cheapest test that distinguishes it from the current target.

Return a short answer with the outcome, decisive mechanism, one consequential alternative and actual test or named blocker. Do not generate a long checklist. A challenger can conclude that the registered question itself should change; the execution ledger cannot dismiss that merely because it is outside the current scope.

Within a system, trace mechanisms, dependencies and failure paths needed for the user's outcome. Across systems, name the source/target objects, map and preserved invariant. The user's illumination and shadow metaphor is useful for separating these views. Similarity alone cannot establish transfer: projections can discard decisive information, and multiple hidden systems can produce the same observations.

Ask specifically: **Where does this argument use the named restriction?** If nowhere, formulate the unrestricted statement and test it. NANUQ's coefficient depends on at most six labels independently of network level; that locality reveals the all-level target. Complete illumination or a perfect answer is not generally certifiable. Report coverage and unknown boundaries.

Also trigger the challenge when a named restriction disappears, a tiny change produces a large scope gain, or two checkpoints add only refinements without resolving a named blocker. Resume execution after each bounded challenge; do not interrupt every lemma. Give an independent challenger the outcome/source/artifact before the author's verdict. Rotate restriction, omitted-mechanism and transfer questions. Optional randomness must be logged and evaluated, not assumed helpful.

Budget target discovery separately from execution and verification. Before broadly formalizing a paper, ask which exact inference needs each dependency and whether a smaller interface suffices. Compare a small set of candidate questions by relevance, source correspondence, available leverage and resource cost, then register a provisional target. Preserve dated replacements when evidence favors a better question.

A Lean theorem can establish consequences of a declared workflow predicate or preservation map. It cannot force an assistant to obey the instruction, certify that a record reflects actual behavior, or prove global optimality without a specified complete search space. The task contract is a record, not an enforced runtime controller. Evaluate this intervention through the paired trials in the dossier; paperwork volume is not success.

## 1. Register a provisional research question after discovery

Use the [task contract](research/new-wave-2026-09-30/task-contract.template.json). Keep one compact claim ledger, linking existing evidence rather than generating parallel paperwork.

Record the primary source, exact locator, accurate problem statement, closest subsequent work, search date and unresolved obstacle. Distinguish an explicitly posed open problem, an author-stated model limitation, and our own proposed question. A model limitation can motivate an investigation, but must not be relabeled a recognized open mathematical problem. Current unresolved status requires checking; an old future-work paragraph is insufficient.

Map the source's objects, assumptions and requested conclusion to the proposed formal model. List changes and omitted mechanisms. Reject a significance claim if the model omits the mechanism needed to support it. For example, conditional approach/avoid observations do not answer how a CBT agent selects a policy or learns from exposure.

Admission requires both a source connection and a precise research target. If either is missing, the next task is a bounded source/model investigation, with an explicit deliverable and stopping point. Do not begin an easier proof and retroactively invent its relevance.

## 2. Specify the strongest useful target

Before proving the baseline, register the ambitious statement, domain, assumptions, quantifiers and output. Explain which stronger conclusion would materially resolve the source obstacle.

Before choosing a fixed level or case, inspect whether the proposed argument uses that restriction at all. If it does not, formulate the general statement first. For a surprisingly easy later generalization, record which prior machinery did the work, why the original statement was narrower, and what the stronger result changes scientifically. Ease is a diagnostic of possible target-selection failure, not proof of novelty or failure. In the NANUQ retrospective, distinguish the reported rapid strengthening from the independently verified final claims; elapsed time and the full sequence of earlier attempts are not established by the current audit.

Evaluate these axes where relevant:

| Axis | Concrete challenge |
|---|---|
| Scope | Can a fixed level become all levels, or a finite example become a specified general class? |
| Assumptions | Which consequential assumptions can be removed or weakened without losing source fidelity? |
| Bounds | Can an upper bound become a sharp threshold, with a matching lower bound or counterexample? |
| Characterization | Can a sufficient condition become necessary and sufficient? |
| Robustness | Can an exact result tolerate explicitly quantified noise, approximation or model mismatch? |
| Mechanism and use | Does the stronger result enable an inference, decision or dependency that the baseline cannot? |

These axes form a partial order: generality, sharpness, computation and fidelity can conflict. Do not claim absolute maximality. Choose a strongest useful target within a declared domain and budget, and explain tradeoffs.

Every task requires a substantive target challenge. Attempt a consequential strengthening when a plausible one survives preliminary inspection; an already sharp target or irrelevant axis does not require a manufactured extension. Evidence can be a derivation, proof artifact, counterexample search with stated coverage, or failed proof with an identified obstruction. A list of possible strengthenings is not an attempt. Failed search is not an impossibility proof; bounded enumeration is not global optimality.

Preserve the initial target and dated revisions. A narrower result may be valuable, but label it partial and state the remaining gap. Do not revise the target downward merely because an easy lemma succeeded.

## 3. Use agents for distinct checks

The user's preferred executor is Sol 6.1 when available; effort is task-specific, with Medium the latest stated session preference. Record the actual model and effort when observable; otherwise record unknown. A requested preference is not evidence of a model switch or a cost advantage. Budget total work across agents, not just the integrator's run.

An integrator owns the registered question and contribution chain. A source reviewer checks correspondence and prior work. A proof challenger independently reconstructs the claim and searches for vacuity, inconsistent assumptions, counterexamples and stronger useful alternatives. Give the challenger the primary question and artifact before supplying the author's verdict. Distinct agents can still share blind spots, so their agreement is not proof.

Assign bounded tasks with concrete return artifacts. Do not create an unlimited agent tree or use agent count as a quality metric. Verification may be delegated, but the integrator must inspect the evidence and report unresolved findings.

## 4. Make each subtask answer to the central target

Execution subtasks must state what evidence or dependency they supply for the current target. Target-discovery subtasks can instead show that a different target better serves the user's outcome. Classify outputs as central result, necessary support, exploratory finding, or optional refinement. Supporting formalization and reproduction are useful when their role is explicit. Optional refinements cannot justify declaring the central question answered.

At checkpoints compare the best established result with the initial ambitious statement, the remaining obstruction and actual resource use. Predeclare phase budgets for source validation, target attempts, verification and synthesis, with a repair reserve. Use project-specific limits; do not invent universal percentages.

Stop or redirect when the claim is false, vacuous, already established or disconnected from its source; a missing empirical assumption defeats its promised interpretation; the budget expires; or two successive checkpoints add only support/refinement without resolving a named blocker or improving the central result. At a stop, return the strongest established statement, attempted stronger statement, evidence about the blocker and smallest meaningful next investigation. A budget stop proves no maximality.

This addresses the observed tendency toward incremental completion as a testable workflow hypothesis. It does not establish that an inference-time assistant feels reward, receives dopamine or updates its training objective through conversation. Track target drift, consequential strengthening attempts and gap closure rather than attributing internal motivation.

## 5. Verify the claim actually being advertised

Record the exact commit, toolchain/dependency revisions, commands, logs, theorem locations and proof-trust boundary. Distinguish a fresh complete build from a prior hosted run, source inspection, sampled transcription checks and exhaustive bounded computation. Never report a Lean build without executing it or clearly identifying the hosted evidence being cited.

Check nonemptiness and nonvacuity, consequential assumption removal, boundary cases and small counterexamples. Review whether the mathematical statement corresponds to the scientific interpretation. A theorem can be perfectly proved and still formalize the wrong question.

For empirical or biological claims, specify measurements, intervention semantics, identifiability assumptions, parameter estimation and validation data where needed. A proof of consequences of assumed dynamics does not establish those dynamics in organisms or patients.

## 6. Attach the contribution to its consumer

Before publication preparation, write the exact baseline-to-result delta and the significance delta separately. State what becomes possible that was unavailable before. For any downstream-use claim, identify a theorem/module, executable transformation, testable prediction or research task and its required interface, and distinguish proposed use from verified consumption. A contribution does not require guaranteed adoption. A narrative link to biology or psychology is insufficient evidence of transfer.

Attach this record to the same research packet and later submission/update. For VibeMathed or another venue, include the source question, statement, assumptions, source map, strengthening frontier, verification evidence, novelty limits and downstream use. Repository publication, submission, review, acceptance and adoption are distinct states; record only those supported by evidence. An external open problem improves relevance but does not guarantee recognition.

The [retrospective](research/new-wave-2026-09-30/RETROSPECTIVE.md) supplies the initial cross-project critique. The [CBT starter assessment](research/new-wave-2026-09-30/STARTER-ASSESSMENT.md) demonstrates a candidate that must remain on hold. Existing NANUQ continuation packets retain their stated bounds and stopping rules; apply this review within them rather than launching an unrelated maximal search.

## Completion record

Return one ledger containing: source/status; target-challenge outcome; original and final targets; tested alternatives and boundary evidence; strongest established result and remaining gap; exact verification status; baseline/significance delta; any downstream-use evidence; and publication state. Completion requires both a justified target and an answer or reached milestone. Partial results and informative failures remain explicitly partial. Reading GitHub supplies context, not updates to model weights. Requested model/effort settings do not establish which is empirically best; record actual settings when observable. The protocol itself succeeds only if it improves meaningful target selection and outcomes, not the volume of documentation.
