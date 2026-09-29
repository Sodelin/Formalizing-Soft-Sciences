# Source-first open-problem screening

**Decision: no existing social-science result is currently qualified for a discovery submission by this screening.** Preserve the 85-declaration corpus, but do not extend it for publication merely because an extension looks possible. First identify an externally stated unresolved problem and demonstrate that the proposed result would answer it, or supply a substantive part of its answer.

This is a project selection decision, not a claim that no reader could find the existing formalization useful. It supersedes the suggestion to seek model extensions before establishing an external target. The completed declaration audit and recovered books remain available.

## The required gate

1. Locate a named author's actual open question, conjecture or precise unresolved task in a primary source. A broad research theme does not suffice.
2. Check the target's current status and closest results before selecting it for new research. A historical question is not automatically still open.
3. Match the mathematical objects, assumptions, quantifiers and conclusion to an existing theorem or a proposed attack. Shared vocabulary does not establish correspondence.
4. Explain what the result would add beyond the source's known examples and established methods. A routine special case or a new formal proof of an established principle does not pass this project's discovery gate.

No new mathematical construction, extension or proof was attempted in this screening. Three concrete targets were examined and rejected as matches to the current corpus. Because none passed statement matching, no complete search for subsequent solutions or priority was undertaken for them. They are verified examples of authors posing problems, not certified research assignments.

## Actual stated targets and why the current results do not answer them

### SP1: Network power rankings versus balanced bargaining outcomes

**Source:** Dimitri Volchenkov, *Mathematical Sociology: Models, Structures, and Open Problems*, Mathematics 14(18), 3363 (2026), Section 3.4, concluding open-problem paragraph. [Publisher text](https://www.mdpi.com/2227-7390/14/18/3363), [DOI](https://doi.org/10.3390/math14183363).

The author asks which graph classes make specified structural power rankings agree with balanced bargaining payoff orderings, including distinct agreement quantifiers. The paragraph also asks: “What minimal counterexamples separate these cases, and what is the complexity of deciding agreement?”

**Existing proof examined:** `SocialScience.CollectiveAction.two_person_budget_iff`, together with the participation and solidarity results in the complete inventory.

That theorem characterizes when one unrestricted integer transfer covers two supplied costs. It has no exchange graph, power index, maximum-weight matching, outside-option condition or balanced-outcome set. It establishes neither ordering agreement nor a separating counterexample in the source's model. **Rejected as a match; no substantive partial answer established.**

Access boundary: the publisher's indexed Section 3.4 text was read, including the complete question and surrounding definitions. Direct publisher HTML/PDF retrieval failed. This is not a claim to have independently reviewed the full 76-page survey or its proofs.

### SP2: Sensitivity analysis with several forms of bias

**Source:** Carlos Cinelli, Avi Feller, Guido Imbens, Edward Kennedy, Sara Magliacane and Jose Zubizarreta, *Challenges in Statistics: A Dozen Challenges in Causality and Causal Inference*, arXiv:2508.17099v1 (23 August 2025), Section 3.6.3, especially “Other types of biases” and “Sharpness results.” [Primary full text](https://arxiv.org/html/2508.17099v1#S3.SS6.SSS3).

The challenge concerns sensitivity to selection, missingness, measurement error and interference, potentially together. The source states: “Performing sensitivity analysis to these types of biases, and perhaps handling all of them simultaneously, is an important open challenge.”

**Existing proofs examined:** `bounded_bias_interval`, `difference_exceeding_bias_identifies_order`, and the Boolean causal non-identification witnesses.

The measurement proofs assume numerical bounds on additive differential bias and propagate those bounds algebraically. They do not derive a causal identified set from observed data and a joint sensitivity model, or establish sharpness for the source's settings. The causal witnesses provide an established observation/effect collision, without that joint model. **Rejected as a match; no substantive partial answer established.**

Access boundary: selected full-text motivation, background and challenge passages in Sections 3.6 and 3.9 were read. Section 3.9 also credits existing causal-identification algorithms; a collection of checked elementary examples is not an automatic solution to its pipeline challenges.

### SP3: Distinguishing simple and complex contagion from data

**Source:** Aida Abiad and coauthors, *Hypergraphs and simplicial complexes in focus: a roadmap for future research in higher-order interactions*, Journal of Physics: Complexity 7, 022501 (2026), Section 6.1, final paragraph, PDF page 25. [Published PDF in Cambridge's repository](https://api.repository.cam.ac.uk/server/api/core/bitstreams/7ade7c44-7d22-4a7c-bfc7-29310947cdd7/content#page=25), [DOI](https://doi.org/10.1088/2632-072X/ae3c4e).

The source identifies the following task: “Distinguishing between simple and complex contagion from empirical data remains an open problem”.

**Existing proofs examined:** the natural-number path/connectedness results, generic probe-identification lemmas and Boolean causal witnesses.

The current corpus specifies neither the competing contagion laws nor a data-generating and observation model for this target. A generic observation collision or the fact that adding probes preserves injectivity does not construct a discriminator or establish an impossibility result for those contagion classes. **Rejected as a match; no substantive partial answer established.**

Access boundary: publication identity, Section 6.1 and the decisive problem passage were checked in the published 35-page PDF. The full roadmap's mathematical results were not independently audited.

## Scope and publication consequence

This bounded search found real externally posed tasks; the problem was not a shortage of interesting vocabulary. The current proofs fail the mathematical correspondence test for these tasks. Other targets may exist, but none has been established here. The decision is therefore **no qualifying match found**, not a universal impossibility claim about every possible use of the corpus.

The social package remains preserved on main. It has not been submitted as a separate VibeMathed discovery entry. Earlier curator messages shared it as a formalization dossier and explicitly did not claim open-problem closure. No additional discovery claim, researcher outreach or proof extension follows from this screening. Any future use in this project's discovery pipeline requires a source-first target that passes the gate above.

The [search ledger](open-problem-gate.json) records queries, source access and rejected mappings. The [complete theorem inventory](THEOREM-BY-THEOREM.md) supplies the exact existing statements against which these targets were compared.
