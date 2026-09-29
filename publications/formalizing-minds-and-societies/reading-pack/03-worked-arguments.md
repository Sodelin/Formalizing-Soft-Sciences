## 4.8 Worked investigations in what a proof can reveal

A short theorem can hide a long scientific argument. Its proof may occupy three lines, while its interpretation requires decisions about measurement, causal structure, and the intended population. The following investigations open those decisions. The additional algebraic and statistical illustrations are explanatory derivations; they are not new Lean declarations in the 67-theorem release.

### Measurement as a problem of coordinates

Suppose a psychological response is represented by an underlying value `a` plus an offset `i`. The observable is `a + i`. A researcher sees 12. Which part belongs to the construct and which part to the scale? The answer is not contained in the sum. Both `(a,i) = (8,4)` and `(a,i) = (10,2)` produce the same observation.

This is more than an example of inadequate sample size. Result 19 identifies a transformation that preserves every relevant observation: replace `(a,i)` by `(a+s,i−s)`. Result 20 extends the transformation across the entire population. Even an enormous collection of perfectly measured responses cannot distinguish parameterizations linked by this symmetry if no additional constraint is supplied.

The natural response is to anchor the scale. One may fix an intercept, choose a reference latent value, or introduce another observation with different dependence on the components. Each choice buys identification by adding structure. The scientific responsibility is to say where that structure comes from. A convenient normalization can define coordinates without establishing a substantive psychological zero. A validated anchor can provide stronger empirical justification. These roles should not be confused.

The distinction between absolute levels and differences is especially revealing. If every observation shares the same unknown offset, differences remain exact even though absolute latent values are not identified. Thus a model can leave one question unanswered while resolving another. “The model is unidentified” is often too coarse a diagnosis. The better question is: which quantity is identified, under which design?

Now allow different offsets. Write the observed difference as `d`, the latent difference as `g`, and the offset difference as `b`. The model says `d = g + b`, hence `g = d − b`. If `−delta ≤ b ≤ delta`, subtraction yields `d − delta ≤ g ≤ d + delta`. This is the entire mathematical engine of result 24.

Take `d = 5`. A bound of 2 gives the interval [3,7], a bound of 5 gives [0,10], and a bound of 6 gives [−1,11]. Nothing about the proof changes. What changes is whether the bound excludes zero. The decisive empirical work lies in justifying the admissible bias, not in obtaining more decimal places from the subtraction.

An asymmetric bound can be more appropriate. If `L ≤ b ≤ U`, the same algebra gives `d − U ≤ g ≤ d − L`. This more general expression is an explanatory extension, not an additional verified theorem in the release. It illustrates how formalization can suggest a next result while also identifying the evidence the result would require.

Random error adds another layer. If the observation includes an error term, a deterministic bias interval alone no longer describes uncertainty in an estimated group difference. A statistical procedure would need to account for sampling and measurement error as well as uncertainty about systematic bias. Combining these uncertainties is a modeling task; placing a confidence label on a deterministic bound would not perform it.

The reward for making these distinctions is practical. Instead of arguing vaguely about whether an instrument is “biased,” researchers can ask what kinds of bias matter for the target contrast, which ones cancel, which ones reverse it, and how strongly each is constrained by evidence.

### Identifiability as geometry of observations

The two-component example observes `a + b`. In the plane of possible pairs, every pair with the same sum belongs to the same observational class. The points `(1,0)` and `(0,1)` are simply two convenient witnesses. The deeper issue is that the observation is constant along an entire direction of variation.

The second probe observes `a`. Now a candidate must match both `a` and `a + b`. Once the first coordinate agrees, matching the total forces the second to agree. Result 34 checks that argument for all integer pairs, not just the example pair.

In elementary linear algebra, the observation mapping can be written using rows `[1,1]` and `[1,0]`. The first row alone compresses two coordinates into one. Adding a second independent row can restore unique recovery in this particular system. This matrix interpretation is explanatory; the repository does not implement a general rank or determinant theorem.

That perspective suggests an experimental-design question with immediate psychological meaning: does a new task contribute an independent constraint, or does it reproduce the same mixture under another name? A second questionnaire that measures exactly the same sum offers repetition, not structural separation. A task that responds differently to the candidate mechanisms can be much more informative.

The formal success can still be practically fragile. Imagine that the second measurement is `a + (1 + epsilon)b` rather than `a`. If `epsilon` is nonzero, two exact linear observations can distinguish the components over real numbers. But the difference between the observations is only `epsilon b`. Recovering `b` requires division by `epsilon`. When `epsilon` is tiny, small observation errors become large parameter errors. Structural identification and reliable estimation are therefore separate achievements.

This illustration is analytically elementary, but it captures a recurring reason for model-recovery checks. A task may contain the needed distinction in principle while expressing it too weakly for the available data. An optimizer's apparent success does not answer that question by itself. Recovery simulations ask whether known generating parameters or model identities can be recovered under the actual design and plausible noise.

The example also clarifies why a proof should record the candidate class. If only pairs with `b = 0` are permitted, the sum alone identifies `a`. If arbitrary pairs are allowed, it does not. Restricting a model class is sometimes scientifically justified, sometimes merely convenient. The proof records what the restriction permits; evidence and theory must justify imposing it.

### Causality as a missing part of the response table

The causal module becomes transparent when all four treatment/background combinations are displayed.

| Background U | Treatment T | Outcome if Y follows T | Outcome if Y follows U | Naturally observed under T = U? |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | Yes |
| 0 | 1 | 1 | 0 | No |
| 1 | 0 | 0 | 1 | No |
| 1 | 1 | 1 | 1 | Yes |

On the two observed rows, the models agree perfectly. On the two unobserved rows, they disagree. The problem is not that the models produce almost identical predictions that a larger sample might separate. They produce identical observations under the specified assignment.

Assume an estimator receives that observational mapping and returns an integer effect numerator. Because the mapping is identical in both models, the estimator must return the same integer. But the correct numerator is 2 in one model and 0 in the other. A universally correct estimator would therefore require `2 = 0`. The contradiction establishes result 39.

Notice the quantifiers. The theorem does not say that no estimator can ever be correct for one of these models. An estimator that always returns 2 is correct for the treatment-driven model. It fails on the background-driven model. The theorem rules out a guarantee of correctness across the whole allowed class when the input contains only the stated observational object.

This difference reveals the strength of the result. A method can return the right answer in a particular world without having information that distinguishes that world from another admissible one. Confidence generated by the method cannot manufacture the missing distinction.

Changing the design can help. Setting treatment independently of background can expose combinations that natural assignment omits, provided the intervention has the intended meaning. Additional assumptions can also help by ruling out candidate worlds. The model must state those assumptions explicitly. A proof about the restricted class then becomes informative, but its empirical scope is only as credible as the restriction.

The repository's last causal theorem takes the strongest possible information route: two deterministic response tables that agree everywhere define the same model. Its strength lies in stating precisely what complete information would determine. Research design then asks which observations and assumptions can recover the needed contrasts from realistically available data.

For social networks, the stakes are similar even though the real mathematics is richer. Similar behavior among connected people may reflect influence, selection of similar companions, shared conditions, or several mechanisms together. Shalizi and Thomas (2011) establish a substantive precedent for these identification difficulties. The binary example here should be understood as an instructional counterpart, not a Lean reproduction of their full results.

### Cooperation has several thresholds

The donation game has a small enough payoff structure to expose its entire incentive argument. Consider one player while the other contributes. Contribution yields `benefit − cost`; defection yields `benefit − sanction`. Contribution resists an improving deviation precisely when `cost ≤ sanction`.

This condition is striking partly because benefit disappears. Holding the other player's action fixed makes benefit the same in both options, so it cancels. The cancellation is informative about the model's strategic comparison. It does not establish that perceived benefit is psychologically irrelevant in a richer decision process.

The condition for preferring mutual contribution to mutual defection is different: `cost < benefit + sanction`. A setting can satisfy this outcome comparison while still failing the unilateral incentive test. That is the logical shape of a collective-action problem: a mutually better outcome need not be individually stable under the specified rules.

The collective-action module adds another distinction. A team can have the capabilities needed to cover every task while allocating its rewards in a way that fails someone's participation condition. With costs 1 and 1 and rewards 0 and 3, the total looks promising and one person still loses relative to the model's zero outside option. Changing the split to 1 and 2 satisfies both inequalities.

Four questions must therefore remain separate: Can the task be performed? Does each participant receive enough under the defined criterion? Is the proposed behavior stable against relevant deviations? Is the arrangement legitimate or fair? The current release supplies precise versions of the first three across different modules. Connecting them and adding an explicit normative criterion would produce a richer institutional model.

Its coverage notion isolates the availability of a skill. “For every task, some member can perform it” does not enforce that the same member has time to perform every task for which that person is the witness. A care organization with one professional capable of ten simultaneous appointments satisfies a simple coverage predicate while failing a scheduling requirement. That gap identifies a useful extension: capacity-constrained assignment.

The withdrawal theorem reveals a second precision issue. Its premise says that anyone in the group capable of a selected task must be the designated agent. That premise is also true when no one can perform the task. The theorem still correctly concludes that excluding the agent leaves the task uncovered. To describe a functioning organization becoming nonfunctional, one must separately establish initial feasibility. Adding that premise upgrades an exclusion result into a theorem about the loss of an initially feasible arrangement.

The relationship to classical sociology is therefore interpretive and selective. Differentiated roles can motivate a formal study of interdependence. The particular capability predicates, payoff inequalities, and integer transfers remain the modeler's choices. Historical scholarship must determine whether they faithfully reconstruct a selected argument; a theorem prover cannot do that textual work by itself.

### Aggregation changes the question unless the target is fixed

The synthetic rate example places most A observations in the difficult context and most B observations in the easy one. Within each context, A's rate is ten percentage points higher. The pooled values reverse because the mixtures differ.

This is not an arithmetic paradox. A pooled rate weights each context by its share of that group's observations. A's weights are 10/110 and 100/110; B's are 100/110 and 10/110. Different weighting schemes can produce different comparisons without any inconsistency.

If both groups were standardized to equal context weights, their illustrative rates would be `(0.90 + 0.20)/2 = 0.55` for A and `(0.80 + 0.10)/2 = 0.45` for B. This calculation describes a new comparison, not the original pooled outcome. Whether it is the scientifically appropriate comparison depends on the target population and causal question.

A confounder, a mediator, and a collider can demand different treatment in a causal analysis. A rule saying “always stratify when there is a reversal” is therefore not justified by the counterexample. The proof teaches that the comparison depends on composition; it does not select a universal adjustment policy.

This point applies to AI benchmarks as well. Suppose one system is evaluated mainly on easy proofs and another mainly on difficult ones. Their pooled pass rates may conceal their relative performance within matched problem families. A good evaluation defines the test distribution, reports stratified results where relevant, and resists treating one pooled percentage as an explanation.

### Repetition, evidence, and the difference between a copy and a new trial

The learning module says that duplicating a list changes no exact-consistency constraints. A deterministic rule agreeing with every entry once agrees with them twice. That result is correct and narrower than the tempting slogan that repetition supplies no information.

For independent Bernoulli observations under a probability model, repeated outcomes can change a likelihood. With `s` successes and `f` failures, the likelihood is proportional to `p^s(1−p)^f`. Additional independent trials alter the exponents. Copying existing records and pretending they are independent trials also alters the computed expression, but without adding independent evidence. The statistical model would then be misapplied.

This contrast gives result 49 a useful role in reasoning about data provenance. The word “duplicate” may refer to a copied record, a repeated task, or a newly observed event with the same value. Those are different data-generating circumstances. The Lean theorem handles list-based exact fit. A probability model supplies the additional structure needed to study repeated sampling.

Likewise, conflicting labels need not establish irrationality or measurement fraud. A task description that omits context can map two genuinely different situations to the same formal input. A time index, social relationship, instruction, or internal state may be missing. Formal contradiction can be a clue that the scientific representation needs more detail.

### A metacognitive puzzle that points beyond the current library

Imagine a predictor that assigns confidence 0.50 on every trial and is correct on exactly half its trials. At the only confidence value it uses, the observed correctness rate matches the stated confidence. Yet the confidence report provides no way to distinguish correct from incorrect trials. Calibration and discrimination are different properties.

This is an explanatory example, not a new theorem in the release. It demonstrates why a future formalization of metacognition should define its target carefully. A property of average confidence is not automatically a property of metacognitive sensitivity, and a sensitivity measure is not automatically an account of the process generating confidence. Fleming and Lau (2014) provide methodological background on these distinctions and measurement issues.

The experiment-design question becomes sharper: which observations distinguish a shift in confidence level from a change in how confidence tracks correctness? Which model parameters are identifiable when task performance changes? Could two mechanisms yield the same confidence distribution but different responses to an intervention? These are plausible research targets that connect formal methods to substantive psychological measurement.

The existing library supplies tools for recognizing the structure of these problems. A next development would add probability distributions, an explicit confidence model, a likelihood, and recovery analysis. That is a concrete path from a methodological foundation to a substantive psychological investigation.
