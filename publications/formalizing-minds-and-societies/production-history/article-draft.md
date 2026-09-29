# Abstract

A well-chosen formal model can identify the measurement that separates competing explanations, establish an information limit shared by every estimator in a defined class, or reveal why a collectively beneficial arrangement fails individual participation. This article presents an integrated library of 67 Lean theorem declarations that makes these possibilities concrete. Seven connected modules address network reach, measurement, identifiability, causality, learning, collective action, and aggregation. The contribution is a reusable research artifact linking precise definitions, machine-checked consequences, interpretable counterexamples, and a reproducible verification record. The models are minimal mathematical representations designed to isolate relationships and support increasingly rich extensions. A complete source audit matched all declarations to the dependency audit and confirmed a successful continuous-integration run at a fixed commit. A targeted literature map locates the work within mathematical psychology and established formal approaches across biology and social science. Five worked arguments show how the library can guide measurement, experiment design, and interpretation. A proposed AI evaluation tests whether paired proofs and explanations improve assumption preservation and reduce unsupported scientific conclusions. The project offers a concrete route from persuasive social explanations to inspectable reasoning, with empirical research determining the value of its downstream applications.

*Keywords:* mathematical psychology, formal verification, Lean, computational social science, identifiability, artificial intelligence

# From Social Explanations to Checkable Proofs

A research argument can be persuasive while leaving its most consequential premise unstated. A difference in scores becomes a difference in an underlying attribute. Similar behavior becomes evidence of social influence. A beneficial total becomes an arrangement that every participant should accept. Each transition may be defensible, but each requires an argument. Formalization makes those transitions available for inspection.

The power of this approach is that a small representation can support a large guarantee. An identification proof can settle uniqueness across an entire parameter class. An impossibility proof can establish a limit shared by every estimator receiving the specified information. A counterexample can decisively refute a universal implication. These results help determine what to measure, which explanations remain viable, and where a new experiment can add information.

The project examined here, *Formalizing Soft Sciences*, develops minimal mathematical representations of social systems and research procedures. Such settings isolate a relationship so that its consequences can be proved, compared, and extended. Their value lies in the distinctions they make usable: between a contact and a route, a score and a construct, an observation and an intervention, a collective surplus and an individually acceptable allocation. Richer models can preserve those distinctions while introducing noise, heterogeneity, time, and institutional detail.

This article evaluates what that development contributes to psychological and social research and how it could support AI reasoning. It treats formal verification as one component of scientific inquiry. The central proposal is to connect a checked implication to the research decision it informs, then make the empirical and interpretive bridge explicit.

## Mathematical and Computational Context

Mathematical psychology has an established tradition of describing psychological processes through precise structures, including equations, formal logic, and simulation (Society for Mathematical Psychology, n.d.). Computational psychology develops executable accounts of processes such as learning, memory, inference, and decision making. The fields overlap: equations can generate simulations, and simulations can embody theories that invite mathematical analysis.

Guest and Martin (2021) argue that computational modeling strengthens theory construction by making otherwise tacit commitments explicit. Formal verification adds a further question: does the stated consequence follow from the encoded model? The translation into that model remains open to scientific review. The Lean documentation distinguishes proof validity from the meaning of the theorem statement and explains how dependencies can be inspected (Lean Project, n.d.).

Relevant precedents extend across disciplines. Biological pathways have been studied with probabilistic model checking (Heath et al., 2008). Voting properties have been formalized in Lean (Holliday et al., 2021). Agent-based cultural models connect local interaction rules to collective patterns (Axelrod, 1997), and kinship terminology has been analyzed through computational algebraic structures (Read et al., 2013). Finkel et al. (2025) present an automata-based formalization of a psychological stress theory. These examples establish a substantive methodological neighborhood for the present work.

## Method

### Source Audit

All seven theorem-bearing modules were inspected at commit `780f1b83aef15a9cf455566bab9df2a47d738074` in the public repository (Sodelin, 2026). The audit also inspected the full declaration-audit file, verification receipt, and CI workflow. The source contains 67 named `theorem` declarations, with every declaration represented in the axiom audit. GitHub Actions run 36392008029 reported success for the inspected main-branch commit.

The workflow uses Lean 4.19.0, builds the libraries, checks the source for admitted goals and custom axioms, prints theorem dependencies, and validates documentation and provenance. The repository records standard Lean logical dependencies or none. This assessment inspected that evidence rather than performing a new local compilation. Appendix A provides a reproducible source locator and the relevant commands.

### Evidence Mapping

A targeted search conducted on September 28, 2026, sought primary research and official documentation on mathematical psychology, computational model recovery, formal social science, anthropology, ethical reasoning, and AI theorem proving. Sources were selected to establish precedents or support the methodological argument. Access depth varied from full source code and selected full-text sections to abstracts. The review was not preregistered and did not use duplicate screening or exhaustive database coverage. Its conclusions concern the identified examples and the inspected development, rather than the prevalence of formalization across entire disciplines.

## Results

### Contribution of the Integrated Library

The new artifact connects seven areas of reasoning within one checked development. Its shared definitions make relationships between modules explicit: an identification result becomes a result about information lost through aggregation, and a distinction between collective feasibility and participation becomes a question about institutional design. The accompanying explanations and commit-linked verification make the same object accessible to a domain researcher and a formal-methods reviewer. Established mathematics supplies much of the content; the contribution of this release is the integrated implementation, its interpretive map, and a concrete platform for further research.

### The Structure of the Development

Table 1 summarizes the theorem distribution. The count includes supporting lemmas, concrete witnesses, and results that reuse earlier statements. For example, one aggregation declaration directly invokes an identifiability result, while the combined Simpson statement packages three prior comparisons. The connected argument and reusable model property are the relevant units for assessing the library's scientific contribution.

| Module | Declarations | Scientific role |
|---|---:|---|
| Solidarity | 16 | Separates reach, membership, trust, and incentives |
| Measurement | 9 | Relates score comparisons to common or differential offsets |
| Identifiability | 9 | Determines which probes distinguish candidate explanations |
| Causality | 6 | Separates observational agreement from intervention effects |
| Learning | 9 | Characterizes exact consistency with labeled evidence |
| Collective action | 10 | Separates task coverage from participation constraints |
| Aggregation | 8 | Demonstrates reversal and information loss in summaries |
| Total | 67 | A connected foundation for model-based inquiry |

### Measurement Bounds Turn a Concern Into a Quantitative Question

The measurement model defines an integer response as latent value plus intercept. With a common intercept, response order and differences preserve latent order and differences. Allowing different intercepts introduces a precise sensitivity problem.

Let the observed difference be `d`, the latent difference `g`, and the intercept difference `b`. The model yields `d = g + b`. If `−delta ≤ b ≤ delta`, the verified result places `g` in `[d − delta, d + delta]`. An observed gap of 5 with a differential-bias bound of 2 therefore implies a latent gap between 3 and 7 in the specified units. A bound of 6 leaves the sign unresolved.

The proof converts a substantive bound into an exact conclusion. Establishing a defensible bound becomes the empirical task. This is a deterministic sensitivity interval; a sampling-based interval would additionally require an observation and estimation model. The distinction makes the next development concrete rather than diminishing the present result.

### Identification Can Be Changed by Design

The identifiability module defines observational equivalence as agreement of candidate predictions on every permitted probe. A design identifies candidates when such agreement forces their equality. The sum-only probe cannot distinguish integer pairs `(1,0)` and `(0,1)`. Adding a probe of the first component identifies the pair: equality of first components, together with equality of totals, determines the second component.

This result directs attention to the information supplied by a design. Adding observations of the same mixture can improve precision while leaving a structural ambiguity intact. A discriminating probe changes the observation map. Computational behavioral modeling further requires investigation of recovery under realistic finite-data conditions (Wilson & Collins, 2019). The current exact result is a clear starting point for that extension.

### Observational Equivalence Can Conceal Different Intervention Effects

In the binary causal example, observational assignment sets treatment equal to background. One model makes outcome follow treatment; another makes it follow background. Both produce the same observed treatment–outcome mapping. Setting treatment to true while background is false separates their responses.

Their effect numerators are 2 and 0. Any estimator receiving only the shared observational mapping must return the same value for both, so no such estimator is correct throughout the allowed class. The proof identifies the information that is missing. Additional design features or model restrictions can change the identification question. The related difficulty of separating homophily and influence in social networks has a richer theoretical treatment in Shalizi and Thomas (2011).

### Collective Benefit and Individual Participation Are Distinct

The collective-action model first asks whether each required task has a capable member. It then asks whether every member's reward covers cost relative to a zero outside option. Two complementary specialists can meet the coverage requirement while a reward allocation fails participation.

With costs 1 and 1 and rewards 0 and 3, total reward exceeds total cost, but the first member's inequality fails. Reallocating rewards to 1 and 2 satisfies both participation conditions. More generally, an unrestricted integer budget can cover both costs through some split exactly when it covers their sum.

The example locates allocation inside the cooperation problem. Capacity constraints, bargaining, outside options, and normative criteria can be added as distinct extensions. This separation is particularly valuable because feasibility, stability, and legitimacy answer different institutional questions.

### A Reversal Makes the Comparison Visible

The aggregation module checks a synthetic table in which A's rates are 9/10 versus B's 80/100 in one context, and 20/100 versus 1/10 in another. A is higher within both contexts. Pooling gives A 29/110 and B 81/110, reversing the comparison.

Different context weights produce the reversal. The result prompts specification of the desired estimand and target population before interpreting a pooled rate. Whether adjustment is causally appropriate depends on the role of the conditioning variable. The example establishes the possibility and arithmetic of reversal; choosing the scientific comparison requires the broader design argument.

## Implications for AI Research

Verified proof data already have a role in AI theorem proving. Xin et al. (2024) report a synthetic Lean training corpus, and Ren et al. (2025) describe a system combining subgoal decomposition with reinforcement learning. These precedents support the feasibility of training on formal material. They leave open whether the present kind of social-science library improves scientific interpretation outside formal proof tasks.

A promising training unit would pair a research question with its definitions, theorem, proof, interpretation, and a nearby false generalization. For the measurement result, a model should both apply the common-offset theorem and recognize when the offset differs across groups. It should also distinguish a verified conditional statement from an empirical conclusion about a particular instrument.

Evaluation should compare retrieval, prose-only instruction, code-only instruction, paired representations, and checker-assisted reasoning. Splits should separate model families and dependency groups because declarations are not independent training examples. Outcomes should include semantic fidelity, assumption preservation, unsupported empirical claims, calibrated uncertainty, and proof success. Appendix B outlines this proposed evaluation.

Formal normative reasoning offers a related opportunity. Systems such as LogiKEy investigate ethical and legal theories using logic and automated reasoning (Benzmüller et al., 2020). A social-science proof library could help an AI distinguish an adopted value premise from an empirical assumption and a derived consequence. Those distinctions are measurable reasoning targets. Broad claims about moral understanding would require evidence beyond checker acceptance.

## Discussion

The development's immediate importance is architectural: it gives researchers a shared place to inspect definitions, deductions, counterexamples, and interpretations. A disagreement can become precise. One reader may contest an assumption about measurement; another may propose a different payoff model; a third may identify an empirical design that separates the alternatives. The proof artifact preserves the consequence while leaving those scientific choices available for revision.

This approach is most useful at the scale of a bounded research problem. A complete formalization of psychology is too broad to guide the next experiment. An isolated arithmetic lemma without an application is too small to establish its value. A model family linked to a measurement or design decision offers a workable middle scale.

The present corpus suggests two immediate directions. A metacognition project could connect confidence measurement to structural identification and recovery analysis, drawing on distinctions between confidence bias and sensitivity (Fleming & Lau, 2014). An institutional project could replace unrestricted task coverage with finite capacity and scheduling while retaining a separate participation model. Each extension would enrich an already explicit baseline.

### Process Integrity Assessment

The source inventory and commit-linked CI evidence are direct and auditable. The literature component is a targeted, single-reviewer synthesis with uneven full-text access. It supports a methods argument and an evidence map; it supplies neither an exhaustive novelty assessment nor a pooled estimate. Appendix C records the process assessment and improvements needed for a systematic review.

### Inference Robustness Assessment

The strongest conclusions are conditional mathematical statements and existence claims about established research approaches. The empirical value of the library and its transfer to AI scientific reasoning remain evaluable hypotheses. No meta-analysis was conducted, so heterogeneity statistics, publication-bias tests, and pooled effect sizes are inapplicable to the present results. Robustness work should first vary the models' assumptions and then test downstream behavior in a preregistered evaluation.

## Conclusion

Small formal models can expose large differences in meaning. A score difference, a causal effect, an individually acceptable allocation, and a pooled comparison each require their own conditions. The 67-theorem development makes selected conditions and consequences available for machine checking and human interpretation.

The next scientific contribution will come from using that precision: designing a more discriminating experiment, identifying a consequential assumption, or improving an AI's handling of a specific reasoning task. A verified result becomes especially valuable when it changes what researchers know to ask next.

# Appendix A

## Source and Verification Receipt

Repository: [Formalizing Soft Sciences](https://github.com/Sodelin/Formalizing-Soft-Sciences). Inspected commit: `780f1b83aef15a9cf455566bab9df2a47d738074`. Successful workflow: [36392008029](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36392008029). Toolchain: Lean 4.19.0.

The audited files are `Solidarity.lean` and the six modules `Measurement.lean`, `Identifiability.lean`, `Causality.lean`, `Learning.lean`, `CollectiveAction.lean`, and `Aggregation.lean` under `SocialScience/`. `SocialScience/Audit.lean` names every theorem for dependency inspection.

The following commands reproduce the repository's principal checks in an appropriately configured checkout:

```sh
lake build
lake env lean SocialScience/Audit.lean
python3 scripts/check_foundations.py
python3 projects/solidarity-at-scale/scripts/validate_project.py --check-only
```

The Python commands inspect provenance and documentation. Lean performs the proof checks. The two roles are separately represented in the workflow.

# Appendix B

## Proposed AI Evaluation

This is a proposed protocol, not a completed experiment. Use a fixed base model and held-out scientific scenarios grouped by underlying model family. Compare no added material, prose only, code only, paired prose and code, and paired material with checker access. Keep inference budgets and task prompts comparable.

Primary outcomes should measure semantic fidelity and unsupported empirical conclusions. Secondary outcomes can include theorem selection, proof completion, counterexample identification, appropriate recognition of underdetermination, and explanation quality. Use independent domain review for meaning-sensitive judgments and the checker for formal derivations. Report uncertainty with clustering by scenario family and disclose all exclusions.

Evidence for useful transfer would require improvement on new model families, preserved accuracy, and fewer unsupported conclusions. Gains restricted to familiar theorem names or arithmetic templates would support a narrower learning claim.

# Appendix C

## Review Quality and Source Access

A descriptive process checklist assigns 2/2 for source provenance, 1/2 for search reproducibility, 1/2 for explicit selection rules, 2/2 for theorem-extraction fidelity, 1/2 for critical appraisal, and 1/2 for independent reproducibility: 8/12 overall. This author-defined checklist is a descriptive self-assessment. AMSTAR 2 addresses the appraisal of systematic reviews of healthcare interventions (Shea et al., 2017). A systematic extension would preregister scope, search specialist databases, obtain complete texts, use independent screening/extraction, and reproduce the proof build separately.

The code audit used full source. The Lean reference and selected biological-modeling sections were directly inspected. Several psychological, anthropological, social-choice, and AI papers were used at abstract or selected-text depth. The accompanying source register gives per-source access information. The source register preserves the distinction between a reported precedent and an independently reproduced result.
