# Foundations I: a research report on verified models for the social sciences

Version 0.2 · 28 September 2026 UTC · A working research report prepared for Nolan Downard. The formal development was produced with AI assistance and checked by Lean. Independent scholarly review remains outstanding.

## 0 Executive brief

The project now has a foundation beyond solidarity and small groups: **measurement, identification, causal reasoning, learning, collective action, and aggregation**. Six new modules contain 51 theorem declarations. Together with the original 16, the repository contains 67 checked declarations. Supporting lemmas, illustrative counterexamples, and main results are included in that count; it is not a count of scientific discoveries.

Three particularly useful results are these. First, a difference between scores can reliably indicate an underlying ordering in a simple additive model if it exceeds an assumed bound on differential measurement bias. Second, identical observational information can be compatible with different causal effects, so an estimator cannot recover both effects without additional information or restrictions. Third, a coalition can have complementary capabilities and positive aggregate surplus while a member remains unwilling to participate under the chosen allocation.

These are established kinds of mathematical reasoning, now expressed in a small checked library with explicit assumptions. No field-level open problem has been solved. The immediate achievement is to make several research questions precise, answer their restricted versions, and identify the extra mathematics and evidence needed for broader answers.

The next highest-value step is a measurement-and-design development: replace exact integer scores with a justified statistical model, distinguish structural identification from estimation uncertainty, and test whether proposed observations separate psychological mechanisms. The larger earlier mathematics-of-psychology corpus must be recovered before choosing overlapping material to reimplement.

## 1 Scope and research question

The guiding question is: **Which inferences in social research can be made explicit enough to check, and which depend on information the model does not contain?** Solidarity is one application. The same question applies to a psychological scale, an experiment on learning, a comparison of institutions, or a cross-cultural association.

This is a foundations project in the practical sense of reusable definitions and verified implications. It does not propose a complete axiomatization of psychology or a reduction of culture to mathematics. Meanings, historical interpretation, construct validity, and the choice of outcomes require substantive inquiry.

Three distinct tasks govern the work: formalize a precise model, prove consequences inside it, and assess whether its assumptions represent the setting of interest. Only the first two are completed for the new elementary examples.

## 2 Method and evidence

This is a targeted methodological literature map paired with an executable formal development. It is not a systematic review, a meta-analysis, or a preregistered empirical study. Searches followed conceptual links from theory construction, computational-model recovery, and measurement invariance to social-network identification and cross-cultural dependence. Primary papers, author repositories, official teaching materials, and Lean documentation were preferred.

The [source register](sources/source-register.csv) records access depth and claim-bearing locations. Some sources were available as selected full-text passages; others only as abstracts, figure captions, or publisher summaries. Paywalls, challenges, and extraction failures are recorded in the [search log](sources/search-log.md). PsycINFO and subscription databases were not searched. The literature map cannot establish priority or exhaustiveness.

Formal work uses Lean 4.19.0 and its bundled standard library. The original source is preserved. A successful remote build and an audit of all 67 declarations establish the reported check status; this environment's local Lean launcher did not run successfully. See the [verification receipt](verification.md).

## 3 Why formalize these foundations?

Borsboom and colleagues distinguish the construction of a formal theoretical model from assessing its adequacy and wider scientific value [F01]. This project adds machine checking to a narrow part of that process: the step from explicit assumptions to consequences. It does not automate theory selection.

An informal argument can conceal a missing assumption. For example, comparing observed scores tacitly assumes something about how the instruments behave across groups. Inferring influence from resemblance tacitly assumes something about common causes. Inferring cooperation from collective benefit tacitly assumes something about allocation and individual incentives. Writing those arguments as theorem statements makes the missing premise visible.

The mathematical areas here are logic and functions, elementary algebra and inequalities, discrete modeling, causal identification, elementary learning theory, and a small part of cooperative economic reasoning. The original network module uses graph-like reachability, and its donation game is game theory. Using integers for scores and tokens does not make the project a contribution to number theory. Combinatorics will matter more when finite populations, networks, and experiment designs are developed.

## 4 Identifiability: can observations distinguish explanations?

Let a candidate mechanism predict an output for each available probe. Two candidates are observationally equivalent under a design when they produce the same output at every probe that design permits. The design identifies the candidate when equivalent candidates must be equal.

The module proves that adding probes preserves any identification already achieved. It also proves that applying the same transformation to identical outputs cannot create a distinction. This provides a common interface for measurement and aggregation: one concerns the observations a design supplies, the other the distinctions its summaries discard.

In the worked example, two unknown integer components are `a` and `b`. The baseline probe reports `a + b`; a second probe reports `a`. Baseline data cannot distinguish `(1, 0)` from `(0, 1)`. With both exact probes, the first component and then the second are identified. This answers a specific design question, not the general problem of experimental design.

For psychology, the components might provisionally represent two mechanisms contributing to a response. That interpretation is a proposal, not a validated measurement equation. Wilson and Collins discuss parameter and model recovery as practical checks in computational behavioral modeling [F02]. Our result addresses exact structural distinguishability; it supplies no finite-sample recovery guarantee or evidence that these two mechanisms describe people.

## 5 Measurement: what does a score comparison mean?

The illustrative measurement equation is `observed = latent + intercept`. A common intercept preserves order and differences. But increasing every latent value by an amount and decreasing the intercept by the same amount changes no observations. An arbitrary origin is therefore not recoverable from these observations alone. Knowing an intercept identifies a person's latent score; knowing an anchor's latent value identifies the intercept in this restricted equation.

For two observations, let the observed difference be `d` and the intercept difference lie between `−δ` and `δ`. The theorem establishes that the latent difference lies in the interval `[d − δ, d + δ]`. If the observed difference exceeds the upper bound on differential bias, its sign identifies the latent ordering. The interval is a **sensitivity bound**, not a statistical confidence interval. The theorem assumes the bound; it neither estimates nor validates it.

For example, an observed difference of 5 with a justified differential-bias bound of 2 constrains the latent difference to 3 through 7 in these score units. If the bound is 6, the corresponding interval crosses zero, so the ordering is unresolved by this argument. An explicit counterexample shows that unequal intercepts can reverse an ordering.

Measurement-invariance research concerns whether comparisons retain their intended interpretation across groups or occasions [F03]. Our one-indicator, unit-loading, error-free integer model is much narrower than factor analysis or item-response theory. It does not establish invariance for any existing instrument, equate constructs across cultures, or justify comparing populations merely because a common numeric label is available.

## 6 Causality: why more of the same observations may not settle a mechanism

The causal example has a binary background variable `U`, treatment `T`, and outcome `Y`. Observational assignment sets `T = U`. Model A sets `Y = T`; Model B sets `Y = U`. In both, the observed treatment and outcome are `(U, U)` for either possible background value.

An intervention that sets treatment to true while background is false separates the models: A yields true and B yields false. The code sums the treatment contrasts over both background values. This numerator is 2 in A and 0 in B; under a uniform background distribution the average effects would be 1 and 0. Probability and division are not implemented in this module.

The impossibility theorem quantifies over every estimator that takes only the observational function as input. Such an estimator receives equal inputs in these two cases, so it must give the same answer, although the correct numerators differ. Consequently no such estimator is correct for every model in the specified class. This is a counterexample to unrestricted observational identification, not a claim that all causal inference from observational data is impossible.

Social resemblance poses related identification problems. Shalizi and Thomas analyze latent homophily and contagion [F04]. McFowland and Shalizi give positive consistency results under particular latent-network and linear-outcome assumptions [F05]. These are complementary warnings about assumptions, not mutually exclusive verdicts. The new binary theorem is not a formalization of either full paper and does not solve peer-effect identification in realistic networks.

## 7 Learning: exact consistency and its limits

The learning module defines a hypothesis as a function from inputs to labels. It fits a finite evidence list when it assigns every recorded input its recorded label. Adding evidence can only remove fitting hypotheses; a query at which two hypotheses disagree can eliminate a rival when the true label is supplied.

The proofs also expose the fragility of exact fitting. Two different labels at the same input make exact consistency impossible. A single incorrect label excludes the true hypothesis. Duplicating the same list adds no new exact-consistency constraint. That last statement does **not** say that repeated independent measurements are statistically useless: probability, noise, and evidence weight are absent here.

This is the logical core of a version-space perspective on learning, an established tradition [F08]. It is not the full candidate-elimination algorithm and includes no efficient representation of general and specific hypothesis boundaries. It does not prove how people learn cultural signs, update beliefs, or acquire concepts. Those applications would need an explicit account of noise, changing meanings, memory, sampling, and social context.

## 8 Collective action: complementarity, allocation, and participation

Here a group is feasible when each required task has a capable member. Two specialists with different capabilities can jointly cover tasks that neither can cover alone. If the only capable member for a needed task withdraws, the remaining group cannot cover every task. These statements are useful starting points for division of labor and organizational dependence.

Participation is a separate condition: each member's reward must meet their cost, relative to a zero outside option. A synthetic two-person economy has cost 1 for each person and rewards 0 and 3. Total reward exceeds total cost, but the first person's participation constraint fails. Changing the allocation to 1 and 2 satisfies both constraints and retains feasible task coverage.

More generally, with two costs and a fixed budget, an unrestricted integer allocation satisfying both constraints exists exactly when the budget covers the sum of the costs. The acceptable share for the first member runs from their cost to the budget minus the second member's cost. This is a complete answer within the model, not a new result in bargaining theory.

The comparison is inspired by the distinction between similarity and interdependence discussed in the original Durkheim reading [S14 in the earlier bibliography]. It formalizes one possible representation of complementary roles, not Durkheim's theory as a whole. It does not establish trust, democratic legitimacy, justice, equilibrium, enforcement, or the social effects of ethnic diversity. Capabilities are not ethnicity. A member may perform arbitrarily many tasks here, with no time constraint; extending to matching or scheduling changes feasibility.

## 9 Aggregation: what disappears when we pool?

The synthetic table gives an exact reversal. Every cell has a positive denominator and a success count no larger than its total.

| Context | A successes / total | B successes / total | Higher observed rate |
| --- | --- | --- | --- |
| Context 1 | 9 / 10 | 80 / 100 | A: 90% versus 80% |
| Context 2 | 20 / 100 | 1 / 10 | A: 20% versus 10% |
| Pooled | 29 / 110 | 81 / 110 | B: approximately 73.6% versus 26.4% |

Lean verifies the comparisons by integer cross-multiplication, avoiding rounding. The groups have different context compositions. The familiar reversal belongs to established work on aggregation and contingency tables [F09]; these particular counts are synthetic examples, not research data.

A second result reuses the identifiability module: observing a sum loses the distinction between two possible component assignments, and subsequent recoding cannot recover it. For a sociologist this motivates checking the unit of inference. An aggregate association does not automatically specify the individual mechanism behind it.

Cross-cultural non-independence is a different problem. Societies can share ancestry, diffusion pathways, or common causes. HRAF's methods materials present multiple approaches [F07], and a 2026 article cautions against treating all dependence with one automatic adjustment [F06]. Neither that dependence nor a valid sampling correction is represented in the present aggregation module. A checked pooled-count example is not a solution to Galton's problem.

## 10 What is old, what is new, and what remains open?

The algebraic identification arguments, consistency lemmas, allocation condition, and aggregation reversal are established mathematical ideas. This release contributes their explicit Lean implementation, shared interfaces, and interpretation for the project's research questions. A distinct source file is not evidence of mathematical novelty. No claim is made to the first Lean proof of these facts.

Formalized social science has substantial predecessors. For example, Holliday, Norman, and Pacuit developed voting theory in Lean [F10]. The earlier [formalization review](../solidarity-at-scale/sources/formalization-prior-work.md) also records social-choice and game-theory projects. Upstream projects were not rebuilt as part of this expansion.

The [problem register](open-problems.md) identifies six bounded questions now resolved, seven proposed development tasks, and several broader methodological challenges. A source's historical future-work suggestion is a research lead until current literature establishes that it remains open. We do not label a problem open merely because this repository lacks a proof.

## 11 Process integrity

The implementation preserves `Solidarity.lean` and adds separate modules. Source hashes, the pinned toolchain, theorem inventory, complete axiom-printing audit, and successful CI run are recorded. Every new declaration has an explanation. The proof count is separated from substantive-result count, and the original psychology import remains explicitly pending.

The initial staging check found a Lean elaboration issue in three concrete rate comparisons. Unfolding their named predicate exposed the decidable arithmetic; the subsequent build and audit passed. There are no admitted goals or custom scientific assumptions declared as axioms. Reported logical dependencies are limited to Lean's standard `propext`, `Classical.choice`, and `Quot.sound`, with some proofs using none. No independent second-kernel verification or external human code review is claimed.

The evidence process has limitations: a targeted search, incomplete full-text access, no dual screening, and no independent extraction check. A systematic-review quality score would be inappropriate. These limitations constrain claims about literature coverage and novelty; they do not replace the separate check of the stated mathematical implications.

## 12 Inference robustness

The main threats are model misspecification and interpretation, not arithmetic rounding. The measurement result depends on unit loadings and the assumed bias bound. The causal impossibility depends on which information and model class are allowed. Exact-learning results depend on deterministic labels. Coalition feasibility omits congestion and participation omits bargaining dynamics. Aggregation results concern a deliberately selected example rather than typical prevalence.

Several counterexamples make these boundaries concrete: an intercept can reverse a score ordering; common causes can mimic a treatment effect observationally; a wrong label can eliminate truth; positive total surplus can coexist with nonparticipation. The repository therefore gives both positive implications and reasons a tempting broader inference fails.

No empirical effect-size synthesis, heterogeneity statistic, publication-bias estimate, or sensitivity meta-analysis was conducted. There is no dataset from which to calculate them. The proposed empirical bridge is to specify constructs and observations, test recovery under a realistic data-generating model, examine assumption violations, and evaluate predictions on held-out data. Those tasks remain to be done.

## 13 Next development and publication

Priority one is recovering and validating the prior psychology corpus. In parallel, the most coherent mathematical extension is to connect measurement ambiguity with experiment selection: which anchors or probes remove which equivalence classes, and how does a bounded perturbation change the answer? Any substantive novelty claim would then require a focused comparison with existing identification and design results.

Priority two adds probability and noisy observations, using a maintained mathematical library after checking toolchain compatibility. Priority three develops finite task assignment, outside options, and enforceable allocation. An anthropology track should specify cultural descent and diffusion separately before proposing a dependence correction. These are scoped development tasks, not promises to solve whole disciplines.

The immediate public deliverable is the repository's main branch with code, this report, theorem explanations, and provenance. The [publication plan](publication.md) stages external review, archival release, and a possible methods manuscript. No messages to scholars, journal submission, preprint submission, or archival DOI have been sent or created by this expansion.

## 14 References and reusable materials

See the [annotated references](sources/references.md) for F01–F11 and access limits, and the [BibTeX export](sources/references.bib) for citation-manager import. The [source relationship file](sources/source-relations.csv) records connections proposed in this synthesis; these are not automatically claims of direct citation between the original authors. The [Obsidian-compatible reading note](notes/foundations-map.md) uses ordinary Markdown and relative links. No live Zotero collection or private vault has been changed.

The [theorem guide](theorem-guide.md), [problem register](open-problems.md), and [verification receipt](verification.md) complete the bridge between the prose, the precise formal claims, and the check results.
