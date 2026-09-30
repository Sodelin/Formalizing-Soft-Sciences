# New Wave: source-connected research with strongest-useful-target review

Adopted 30 September 2026. This protocol governs new discovery tasks and reviews of existing contributions. It supplements the [source-first open-problem gate](research/publication-audit-2026-09-29/OPEN-PROBLEM-GATE.md); it does not make previously rejected candidates eligible or replace an active bounded task packet.

The required chain is **external problem → strongest useful target → checked contribution → specific new capability → subsequent research or submission**. A polished proof, a larger theorem count, or successful repository publication cannot substitute for a missing link.

## 1. Register one question before work

Use the [task contract](research/new-wave-2026-09-30/task-contract.template.json). Keep one compact claim ledger, linking existing evidence rather than generating parallel paperwork.

Record the primary source, exact locator, accurate problem statement, closest subsequent work, search date and unresolved obstacle. Distinguish an explicitly posed open problem, an author-stated model limitation, and our own proposed question. A model limitation can motivate an investigation, but must not be relabeled a recognized open mathematical problem. Current unresolved status requires checking; an old future-work paragraph is insufficient.

Map the source's objects, assumptions and requested conclusion to the proposed formal model. List changes and omitted mechanisms. Reject a significance claim if the model omits the mechanism needed to support it. For example, conditional approach/avoid observations do not answer how a CBT agent selects a policy or learns from exposure.

Admission requires both a source connection and a precise research target. If either is missing, the next task is a bounded source/model investigation, with an explicit deliverable and stopping point. Do not begin an easier proof and retroactively invent its relevance.

## 2. Specify the strongest useful target

Before proving the baseline, register the ambitious statement, domain, assumptions, quantifiers and output. Explain which stronger conclusion would materially resolve the source obstacle. Evaluate these axes where relevant:

| Axis | Concrete challenge |
|---|---|
| Scope | Can a fixed level become all levels, or a finite example become a specified general class? |
| Assumptions | Which consequential assumptions can be removed or weakened without losing source fidelity? |
| Bounds | Can an upper bound become a sharp threshold, with a matching lower bound or counterexample? |
| Characterization | Can a sufficient condition become necessary and sufficient? |
| Robustness | Can an exact result tolerate explicitly quantified noise, approximation or model mismatch? |
| Mechanism and use | Does the stronger result enable an inference, decision or dependency that the baseline cannot? |

These axes form a partial order: generality, sharpness, computation and fidelity can conflict. Do not claim absolute maximality. Choose a strongest useful target within a declared domain and budget, and explain tradeoffs.

At least one consequential strengthening must receive a substantive attempt before a discovery task is declared complete. Evidence can be a derivation, proof artifact, counterexample search with stated coverage, or failed proof with an identified obstruction. A list of possible strengthenings is not an attempt. Failed search is not an impossibility proof; bounded enumeration is not global optimality.

Preserve the initial target and dated revisions. A narrower result may be valuable, but label it partial and state the remaining gap. Do not revise the target downward merely because an easy lemma succeeded.

## 3. Use agents for distinct checks

The user's preferred executor is Sol 6.1 at Max when the platform exposes it. Record the actual model and effort when observable; otherwise record unknown. A requested preference is not evidence of a model switch or a cost advantage. Budget total work across agents, not just the integrator's run.

An integrator owns the registered question and contribution chain. A source reviewer checks correspondence and prior work. A proof challenger independently reconstructs the claim and searches for vacuity, inconsistent assumptions, counterexamples and stronger useful alternatives. Give the challenger the primary question and artifact before supplying the author's verdict. Distinct agents can still share blind spots, so their agreement is not proof.

Assign bounded tasks with concrete return artifacts. Do not create an unlimited agent tree or use agent count as a quality metric. Verification may be delegated, but the integrator must inspect the evidence and report unresolved findings.

## 4. Make each subtask answer to the central target

Every proposed subtask must state what evidence or dependency its completion supplies for the registered target. Classify its output as central result, necessary support, exploratory finding, or optional refinement. Supporting formalization and reproduction are useful when their role is explicit. Optional refinements cannot justify declaring the central question answered.

At checkpoints compare the best established result with the initial ambitious statement, the remaining obstruction and actual resource use. Predeclare phase budgets for source validation, target attempts, verification and synthesis, with a repair reserve. Use project-specific limits; do not invent universal percentages.

Stop or redirect when the claim is false, vacuous, already established or disconnected from its source; a missing empirical assumption defeats its promised interpretation; the budget expires; or two successive checkpoints add only support/refinement without resolving a named blocker or improving the central result. At a stop, return the strongest established statement, attempted stronger statement, evidence about the blocker and smallest meaningful next investigation. A budget stop proves no maximality.

This addresses the observed tendency toward incremental completion as a testable workflow hypothesis. It does not establish that an inference-time assistant feels reward, receives dopamine or updates its training objective through conversation. Track target drift, consequential strengthening attempts and gap closure rather than attributing internal motivation.

## 5. Verify the claim actually being advertised

Record the exact commit, toolchain/dependency revisions, commands, logs, theorem locations and proof-trust boundary. Distinguish a fresh complete build from a prior hosted run, source inspection, sampled transcription checks and exhaustive bounded computation. Never report a Lean build without executing it or clearly identifying the hosted evidence being cited.

Check nonemptiness and nonvacuity, consequential assumption removal, boundary cases and small counterexamples. Review whether the mathematical statement corresponds to the scientific interpretation. A theorem can be perfectly proved and still formalize the wrong question.

For empirical or biological claims, specify measurements, intervention semantics, identifiability assumptions, parameter estimation and validation data where needed. A proof of consequences of assumed dynamics does not establish those dynamics in organisms or patients.

## 6. Attach the contribution to its consumer

Before publication preparation, write the exact baseline-to-result delta and the significance delta separately. State what becomes possible that was unavailable before. Identify a concrete downstream theorem/module, executable transformation, testable prediction or research task and its required interface. A narrative link to biology or psychology is insufficient.

Attach this record to the same research packet and later submission/update. For VibeMathed or another venue, include the source question, statement, assumptions, source map, strengthening frontier, verification evidence, novelty limits and downstream use. Repository publication, submission, review, acceptance and adoption are distinct states; record only those supported by evidence. An external open problem improves relevance but does not guarantee recognition.

The [retrospective](research/new-wave-2026-09-30/RETROSPECTIVE.md) supplies the initial cross-project critique. The [CBT starter assessment](research/new-wave-2026-09-30/STARTER-ASSESSMENT.md) demonstrates a candidate that must remain on hold. Existing NANUQ continuation packets retain their stated bounds and stopping rules; apply this review within them rather than launching an unrelated maximal search.

## Completion record

Return one ledger containing: source/status; original and final targets; attempted strengthenings and boundary evidence; strongest established result and remaining gap; exact verification status; baseline/significance delta; downstream consumer; and publication state. Central-task completion requires the admitted question to be answered or its stated milestone to be reached. Partial results and informative failures remain explicitly partial. The protocol itself succeeds only if it improves meaningful target selection and outcomes, not the volume of documentation.
