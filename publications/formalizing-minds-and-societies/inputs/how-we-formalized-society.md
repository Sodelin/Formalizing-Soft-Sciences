---
title: "How We Formalized Questions About Society"
subtitle: "A reader's guide to 67 Lean proofs, their theory, and their limits"
author: "Formalizing Soft Sciences · prepared for Nolan Downard with Codex"
date: "28 September 2026"
lang: en-US
rights: "Working educational edition; source rights remain with their respective authors"
---

# Begin here

Imagine two strangers cooperating on a task. Why did it work? Perhaps they trusted one another, shared a cultural signal, expected a reward, or knew that an institution would enforce an agreement. One observation—cooperation—does not tell us which explanation is right. Social science studies that gap between what we see and what caused it. This book shows how a small Lean project makes some of the reasoning in that gap unusually explicit.

You can read it without knowing Lean. The first chapters explain the ideas and examples. The theorem guides then name every checked result and say exactly what it means. The appendix contains the actual source. You can skip the code on a first reading.

**Status at this edition.** The [public repository](https://github.com/Sodelin/Formalizing-Soft-Sciences) has 16 declarations in the original solidarity model and 51 in six new foundation modules, for 67 checked declarations. Lean 4.19.0 built the source and audited their logical dependencies in [workflow run 36391937036](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36391937036). These are mathematical statements inside explicit simplified models. No field-level open problem, psychological law, or empirical effect was established. The larger earlier mathematics-of-psychology corpus mentioned in prior conversations has not been located or imported.

## A short map for reading together

1. **Theory first:** how a social explanation becomes a model, why evidence may fail to identify a mechanism, and what a Lean proof checks.
2. **The earlier solidarity model:** contacts and reach, overlapping memberships, trust, and a two-person incentive game.
3. **The new foundations:** measurements, distinguishing explanations, causes, learning, task-sharing, and misleading aggregates.
4. **What is new:** a connected, inspectable implementation and reader guide; the underlying mathematics is largely familiar. The source and verification record are reproducible; no mathematical priority is claimed.
5. **Technical reference:** every theorem, evidence notes, the open-problem register, and full Lean code.

# Part I Theory before formalization

## A claim has several layers

Suppose someone says, “A shared identity makes people cooperate.” First ask what identity means: a census category, a chosen affiliation, a felt relationship, or recognition of a symbol? Then ask what cooperation means: agreeing in a survey, contributing money, doing a task, or sustaining an institution over years? Finally ask whether the proposed relationship is a definition, a deduction from assumptions, or a claim about actual people.

A formal model is a deliberately small representation. It names objects and rules, then asks what must follow if those rules hold. A proof assistant checks the deduction. It cannot by itself tell us whether a questionnaire measures identity well, whether participants treat tokens as full motives, whether an ethnographic category preserves local meaning, or whether an intervention would be legitimate. Those require theoretical, historical, and empirical work.

The distinction is like a map. A perfectly drawn map of an imagined city can be internally consistent and still fail to describe Seattle. Lean checks internal consistency of the specified route; people must check the map's relationship to the world. Even a failed model helps if it reveals where a strong claim smuggled in an assumption.

## A running example: the two-explanation problem

Imagine a response score made from two possible sources: perceived familiarity and recognition of a shared symbol. If your only observation is their **sum**, a score of one could arise from familiarity one and symbol recognition zero, or the other way around. No perfectly accurate calculator can recover both ingredients from that one total. A second observation aimed at familiarity can distinguish them in the project's exact integer example. This is **identifiability**: can the permitted observations separate the proposed explanations?

That example says nothing yet about whether familiarity and symbols really add, whether the two probes are valid, or how noisy responses behave. Those are substantive assumptions. The mathematical point is that more computational power cannot reconstruct a distinction absent from the observed information. The next design question is which measurement would add the missing information.

## Six foundations and their everyday questions

**Measurement.** If two groups give different scores, did the underlying attribute differ, or did the instrument behave differently? The model writes observed score as latent value plus an intercept. A shared intercept leaves differences intact. An unequal intercept can reverse an apparent order. If we can justify a maximum bias difference, Lean checks an interval for the latent difference. The bound is an assumption, never a confidence interval estimated from data.

**Causality.** Two stories can fit the same observations and disagree about an intervention. If a background factor causes both treatment and outcome, observational agreement with a direct treatment effect may be deceptive. The binary toy models have identical observed mappings but different intervention outcomes. It follows that no rule using only that mapping can always recover the effect across this model class. Randomization or well-justified restrictions can change what is identifiable; the theorem does not condemn all observational research.

**Learning.** In an exact-label world, a candidate rule remains plausible if it agrees with every observed example. A carefully chosen new example can rule out a rival. A mislabeled example can also rule out the true rule. Real learners have noise, repetition, uncertainty, shifting categories, and limited memory. The module is a clean logical baseline, not a psychological learning theory.

**Collective action.** A group can cover tasks through complementary skills even when neither specialist can work alone. But producing a surplus is distinct from sharing it so that each person accepts participation. In the toy example, rewards of zero and three exceed two costs of one in total, yet the person offered zero declines under the model. Giving them one and the other person two satisfies both constraints. Feasibility, consent, justice, and durable governance remain separate matters.

**Aggregation.** In two contexts, A's rates are 9/10 versus B's 80/100, and 20/100 versus B's 1/10. A is higher in each. Pool the differently sized groups and B has 81/110 versus A's 29/110. This is a synthetic Simpson-style reversal. Lean checks the exact count comparisons. The example tells us to inspect composition and the desired comparison before reading a pooled statistic as a mechanism; it does not say the pooled or stratified number is always the correct causal answer.

**Auditability.** The repository connects theorem names, plain-language descriptions, source files, references, source hashes, and a build record. This makes disagreement more precise: one can challenge the assumptions, the mapping from words to definitions, the proof, the empirical fit, or the claimed novelty separately.

## Where sociology and anthropology enter

The earlier solidarity model distinguishes having a direct contact from being connected by a chain, and having a chain from trusting someone. It distinguishes membership overlap from uniform identity, and a feasible incentive from cultural similarity. A Durkheim-inspired next model asks how complementary roles support production and how allocation affects participation. It is one interpretation of interdependence, not a machine certification of Durkheim.

At larger scales, meanings, power, shared histories, diffusion, and institutions matter. A mathematical label for a person does not encode an ethnicity. Nesting a city within a state does not prove that city-level and nation-level dynamics obey the same law. The project proposes richer models and empirical tests, but the present theorems stay inside their stated toy settings.

## What counts as a discovery here?

There are three possible contributions to distinguish. **A checked implementation** is a new artifact: this particular library and its links to research questions. **A mathematical discovery** would require a theorem that meaningfully advances beyond known results, with careful comparison to predecessors and independent review. **A scientific discovery** would require evidence that a well-defined social or psychological mechanism operates in the world, with credible measurement and uncertainty analysis. This release clearly has the first. It makes no claim to the latter two.

The source research map records predecessors in measurement invariance, causal identification, version spaces, Simpson's paradox, social choice formalization, and theory construction. Several readings were abstract-only or partial. The literature search was targeted, so even a novel-looking encoding cannot establish priority. For a curious reader, the achievement is a way to see exactly what has been proved and where a new study would have to begin.

# Part II The research and every theorem


# The earlier solidarity theory and its 16 Lean results


### A reader guide to the mathematics the evidence and the next research steps

Prepared for Nolan Downard and readers of Formalizing Soft Sciences. Research assistance by Codex. Version 0.1, 27 September 2026 Pacific time.

**Lean checks whether a precisely written conclusion follows from precisely written definitions and assumptions.** Our current project uses that ability to separate personal connections, group membership, trust, and incentives. Its 16 checked theorems clarify what follows inside a few small models. They do not establish a new psychological law, certify a political ideology, or prove that any historical thinker was right about society.

The mathematics currently used is elementary and familiar. Formalizing parts of social science in proof assistants also has substantial precedent. The useful contribution here is an inspectable connection between research questions, model assumptions, proofs, evidence, and limitations. Whether a later extension makes an original research contribution requires comparison with prior work and independent review.

The initial paper, report, evidence tables, and Lean source are publicly readable on main in [Formalizing Soft Sciences](https://github.com/Sodelin/Formalizing-Soft-Sciences). The larger earlier mathematics and psychology corpus requested by Nolan has not yet been recovered. Its import remains a separate, unfinished requirement. Nothing in this guide should be mistaken for an inventory or replacement of that older work.

### 1 What kind of mathematics this is

This project combines **discrete mathematics and elementary game theory**, expressed using mathematical logic. Graph theory is often treated as part of combinatorics. Counting groups, possible memberships, or network configurations would add more explicit combinatorial questions. Number theory usually investigates arithmetic structure, such as divisibility and primes; using natural numbers as person labels or integers as payoff tokens does not make this a number theory project.

| Mathematical area | What it does here |
|---|---|
| Graph theory | Distinguishes direct neighbors from people reachable through intermediaries. |
| Sets and relations | Represents membership, inclusion, overlap, and a separate trust relation. |
| Logic and proof | Makes quantifiers, assumptions, implications, and counterexamples explicit. |
| Game theory | Checks whether unilateral defection improves a payoff in a specified game. |
| Probability and statistics | Needed to estimate psychological effects; not implemented in the current Lean file. |

**Yes, game theory can be encoded in Lean.** Players, actions, preferences, payoffs, deviations, and equilibrium conditions can all be represented mathematically. Our file handles one symmetric two-player example. Existing public projects go beyond this example, and published Lean work already covers voting theory [N02–N04]. We have not imported or independently rebuilt those projects.

Your Kennewick, Washington, and American identities raise a membership question. They also raise an empirical question about when each identity becomes salient. The current membership proof addresses only the first kind of question, and only after inclusion is assumed. Place of residence, citizenship, and felt belonging are different variables; actual identities need not follow administrative boundaries. The proofs do not establish that cities, states, and nations are mathematically self-similar or have identical political dynamics.

### 2 What a checked proof buys us

There are three different jobs. First, interpretation translates an informal question into variables and definitions. Second, deduction establishes consequences of those definitions and assumptions. Third, empirical research tests whether the chosen representation helps explain or predict observations. Lean primarily assists the second job, while making choices made in the first easier to inspect.

For example, “people can coordinate beyond their immediate friends” might mean that messages can travel through a network, that people trust strangers, or that they willingly contribute resources. Those are different propositions. A graph proof about paths cannot silently become evidence about trust or cooperation.

Lean checks proof terms against formal statements. Its official documentation explains this checking process and its trusted components [N05]. A successful check can still accompany an inappropriate definition, an implausible social assumption, or a theorem that answers the wrong question. Reading the statement and connecting its variables to observations remains essential.

This is especially useful when informal arguments skip a step. The project constructs a connected network with no trust at all. That demonstrates that connectivity alone does not logically entail trust in this formal vocabulary. It does not demonstrate that human networks typically lack trust. A counterexample to a claimed logical implication and an estimate of how often something happens serve different purposes.

### 3 The complete current theorem inventory

All names below occur in `Solidarity.lean`. The build uses Lean 4.19.0 and its bundled standard library. These are the actual 16 declarations, including supporting lemmas; they are not 16 independent empirical discoveries.

#### Paths and direct contacts

**1 adj_symm.** If one number is adjacent to another in our path, the reverse adjacency also holds. Adjacency means the numbers differ by one. This checks that the example graph is undirected; it does not assume that real friendships or obligations are always reciprocal.

**2 reach_trans.** A path from A to B and a path from B to C can be combined into a path from A to C. This is the mathematical basis for reaching someone through intermediaries. It says nothing about whether a message arrives accurately or whether a recipient acts on it.

**3 reach_symm.** A path can be traversed in reverse in this graph. The result depends on its symmetric edges. A hierarchy with one-way communication would require a different model.

**4 zero_reaches.** Starting at person 0, every natural-number label can be reached by a finite sequence of neighboring labels. Induction supplies the proof: first reach 0, then extend a path one step at a time.

**5 path_connected.** Every pair of vertices is connected by a finite path. Each individual journey is finite even though the mathematical population has no final vertex. This is not a claim that an actual population is infinite.

**6 at_most_two_neighbors.** Every neighbor of a vertex must be one of its two adjacent numerical labels. At the endpoint 0, there is only one actual neighbor. The theorem gives containment in a set of at most two candidates; it does not estimate anyone's friendship capacity.

**7 unbounded_reachable.** For every proposed numerical bound, some vertex beyond that bound remains reachable from 0. Together with the neighbor result, this separates small local degree from unlimited indirect reach in the example. It gives neither a time bound nor a bound on communication loss.

This path is a simple counterexample to the assertion that a bound on each person's direct contacts must also bound the size of every connected society. It does not refute hypotheses about the cognitive effort needed to maintain emotionally meaningful relationships. The separate literature review considers the uncertainty around a universal fixed “Dunbar number” [S01].

#### Membership and trust

**8 membership_nesting.** If every member of A belongs to B, and every member of B belongs to C, then every member of A belongs to C. This is transitivity of inclusion. It checks the inference after both inclusion assumptions have been supplied; it does not discover those assumptions from geographic names.

**9 overlapping_memberships.** Two groups can share a member while each also has a member absent from the other, and both can lie within one larger population. The concrete example uses A containing 0 and 1, and B containing 0 and 2. This shows that overlapping membership is logically coherent. It does not establish whether people recognize, value, or tolerate that overlap.

**10 connected_without_trust.** There is a connected network for which the independently defined trust relation is false everywhere. Reachability therefore does not force trust. Since trust has no behavioral connection to the graph in this construction, the result cannot measure a real connectivity–trust relationship.

#### Incentives and cooperation

**11 cooperation_stable_iff.** In the specified donation game, mutual contribution resists a unilateral payoff-improving deviation exactly when the sanction for defection is at least the contribution cost. Equality gives indifference, so this is weak stability rather than a strict preference to contribute. The next section works through the arithmetic.

**12 no_sanction_failure.** If contributing costs a positive amount and the sanction is zero, mutual contribution is not stable under that game's payoff rule. This does not show that unsanctioned human cooperation is impossible. Reciprocity, concern for others, norms, reputation, and repetition are absent from this payoff rule.

**13 heterogeneous_cooperation_exists.** Two players can have different labels and still satisfy the game's stability condition. The witness uses benefit 3, cost 1, and sanction 2. Labels are deliberately absent from the payoff function, so this is a possibility result inside the model, not evidence that identity never matters.

**14 homogeneous_cooperation_can_fail.** Players with the same label can fail the stability condition. The witness uses benefit 3, cost 1, and sanction 0. This shows that shared labels do not logically supply a missing incentive in a model that assigns no payoff effect to labels.

**15 symbols_alone_insufficient.** Giving both players the same marker also leaves an unstable example. This is the same limitation made explicit for a shared symbol. It does not test a theory in which symbols change expectations, preferences, or obligations. Such a theory needs those mechanisms represented.

**16 mutual_gain.** Mutual contribution gives each player a higher payoff than mutual defection if contribution cost is less than benefit plus sanction. This compares two outcomes; it does not by itself establish stability. It also omits the cost and distribution of institutional enforcement.

The label and symbol witnesses are deliberately modest. Their value is to expose the missing mechanism in a sweeping argument, not to settle an empirical debate by defining the debated variable out of the payoff function.

### 4 Reading the game without knowing Lean

There are two choices: contribute or defect. A contribution benefits the other player. A contributor pays a cost; a defector pays an externally imposed sanction. Each person's payoff equals the benefit received from the other, minus either their own contribution cost or their defection sanction. Benefits, costs, and sanctions are integer tokens.

Take benefit 3, contribution cost 1, and defection sanction 2. Each cell below lists the row player's payoff first and the column player's payoff second.

| Row player choice | Column contributes | Column defects |
|---|---|---|
| Contribute | 2 and 2 | minus 1 and 1 |
| Defect | 1 and minus 1 | minus 2 and minus 2 |

If the other person contributes, contributing gives you 2 and defecting gives you 1. Defection does not improve your payoff. Symmetry supplies the same reasoning for the other person. This is the mutual-contribution equilibrium condition used here.

Now remove the sanction. Against a contributor, contribution still gives you 2 but defection gives you 3. That changes the incentive to deviate. The benefit cancels when comparing these two actions because the other person's contribution is held fixed. Only the comparison between your contribution cost and your defection sanction remains.

**This is a conditional game-theory result, not a recommendation to maximize punishment.** Enforcement is perfectly reliable and externally supplied in this model. Financing, abuse, legitimacy, mistakes, inequality, resistance, and long-run behavior are omitted. Even the mathematical theorem allows arbitrary integer parameters; the socially familiar interpretation additionally assumes nonnegative benefits and sanctions and a positive contribution cost. Those sign assumptions must be stated whenever that interpretation is used.

A payoff table is not automatically a psychological theory. Treating a token payoff as a person's complete motivation is an additional modeling choice. Stable mutual contribution also need not be what people learn, choose, or regard as just. Those are further questions.

### 5 What this contributes to psychology

**No theorem in the current file proves an empirical psychological effect.** There are no participant data, fitted parameters, probability distributions over choices, or tests of a psychological measurement model in that file. Its immediate psychological contribution is to separate concepts and check consequences of clearly stated hypothetical relationships.

Your original question proposes at least two mechanisms. A stranger might feel familiar because they resemble an important person in your life. Alternatively, a stranger might recognize shared symbols and thereby signal common expectations. A third possibility is that cooperation depends mainly on material incentives and the reliability of an institution. These mechanisms can interact, and they should not be represented by one variable called “homogeneity.”

The literature gives reasons to examine these distinctions. Relational-self theory discusses how representations of significant others can shape responses to new people [S05]. Cultural-marker research examines how markers can acquire social significance [S04]. Work on identity complexity distinguishes different representations of multiple memberships [S06, S28]. The project records access limitations for these sources; an abstract-level reading does not justify a full reconstruction of a published psychological model.

#### What we would have to measure

| Construct | Possible observation | Main interpretation problem |
|---|---|---|
| Perceived personal familiarity | A rating of resemblance to a significant person | Resemblance may also change warmth or perceived status. |
| Symbol recognition | Recognition and interpretation of a shared sign | Recognizing a sign need not imply endorsement. |
| Expected cooperation | A forecast of the partner's contribution | Beliefs can differ from the person's own preferences. |
| Identity structure | Membership reports and judgments of overlap | Administrative categories can differ from felt identity. |
| Cooperation | A costly contribution or a completed joint task | One task may not generalize to other settings. |

These are proposed measurements, not variables already validated for this project. The empirical protocol in the repository separates manipulations and outcomes so that a future study can investigate them. The existing meta-analytic and experimental evidence in the report concerns particular populations and tasks; it cannot identify a universal mechanism by itself [S03–S06].

#### What future psychology proofs could establish

A specified learning rule could support a theorem that its predictions remain within an allowed range. A decision model could support a theorem that increasing one incentive changes a predicted choice under explicit assumptions. A measurement model could support an identifiability result showing whether different latent explanations can produce exactly the same observable distribution. These are valuable mathematical targets. None is implemented in the present file, and none would establish that people actually follow that model without empirical evidence.

A useful extension would allow personal familiarity and symbol recognition to change beliefs about a partner, or allow identity to enter preferences explicitly. We could then compare models that otherwise produce similar behavior. If two mechanisms give the same predictions for all observations collected, that is a reason to redesign the study. A proof of indistinguishable predictions would reveal an evidential limitation rather than establish which mechanism is psychologically true.

For example, high contribution following a shared symbol might reflect trust, a felt obligation, fear of sanctions, or a desire to appear loyal. Observing only contribution cannot automatically separate those explanations. Future models need a clear account of which additional observation or intervention would distinguish them. That account should precede claims that an identity mechanism has been proved.

#### Carrying forward the existing psychology corpus

The substantial earlier mathematics and psychology development belongs in this project with its provenance intact. Its location is unresolved in the accessible history and repositories. Screenshots may supply a conversation title, filename, theorem name, repository, or commit that makes recovery possible. A screenshot can be a locator; complete source files and their configuration are needed for a reproducible import.

The import process will preserve an unchanged snapshot, record its source and file hashes, reproduce its original build, and map each theorem to its informal meaning and assumptions. Only then should presentation or module organization change. The reader inventory will report original, imported, checked, and unresolved items separately. If a module requires a different Lean version, it can retain that environment until a migration has been independently checked.

This is not a reason to replace the older development with newly written examples. The current guide explains only the available 16 theorems. The older corpus's size, content, and check status remain unknown here, and the project must continue to label its import as pending.

### 6 How Durkheim could guide a formal model

Durkheim distinguishes solidarity associated with shared beliefs and sentiments from solidarity associated with differentiated, interdependent functions. In the excerpt examined, these are distinguishable aspects of social life, not simply a claim that everybody must become alike [S14]. That distinction directly motivates our research question about whether groups need similarity, compatible expectations, complementary roles, or some combination.

A responsible formalization would select a particular claim and identify its textual basis. It would state a proposed mathematical interpretation, explain what it leaves out, and distinguish that interpretation from Durkheim's wording. It would also examine alternative interpretations. Encoding a complete body of sociological thought as one proposition would hide too many choices.

Here is a concrete next model, **proposed rather than already proved**. A finite group must complete several tasks. Individuals have different capabilities; a task requires an appropriate capability. Define successful collective production using task coverage and a feasible assignment. Separately define whether each person prefers participating to an outside option. Add rules for sharing gains, enforcing commitments, and leaving the arrangement.

One proof target is a conditional existence result: when the required tasks can be assigned among complementary participants and each assigned participant receives enough to cover their cost, collective production can be feasible and individually acceptable. A second target is a counterexample: capability complementarity and aggregate surplus can coexist with one participant receiving too little to accept the arrangement. A third target asks what changes when a necessary role withdraws or an institution loses reliability.

These targets keep productive dependence, participation incentives, and fairness distinct. They do not identify occupational specialization with racial or ethnic difference. They also do not assume that dependence is voluntary or legitimate. They are proposed mathematical interpretations inspired by a question in classical sociology, not claims that Durkheim proved those exact statements.

For the cultural-sign question, a later model would need an explicit learning or coordination mechanism. Merely assigning two people the same symbol and then assuming trust would place the desired conclusion inside the premises. The research task is to explain and test the link between signs, interpretation, expectations, and behavior.

It is not necessary to formalize every classical author before doing ethnological research. A more productive route is to move repeatedly between selected texts, ethnographic or historical cases, precise models, and observations that challenge the models. Differences in local meaning, colonial histories, institutions, and power must inform variable definitions. Ethnic categories should not be treated as fixed biological essences or used as interchangeable substitutes for task roles.

### 7 What is established prior work and what might become novel

Proof assistants have already been used in social choice. Nipkow's Isabelle/HOL work formalized Arrow's impossibility theorem and a related Gibbard–Satterthwaite result [N01]. Holliday, Norman, and Pacuit's 2021 paper developed voting theory in Lean, including properties of the Split Cycle voting method [N02]. Public Lean 4 repositories also address social choice and game-theoretic structures [N03, N04]. This project is therefore not the first attempt to connect proof assistants with social science.

| Candidate contribution | Present assessment |
|---|---|
| Path connectivity and membership logic | Established elementary mathematics; no mathematical novelty claimed. |
| Donation-game threshold | Elementary consequence of the chosen payoff rule; no new equilibrium theorem claimed. |
| This exact Lean script | A new project artifact; priority or uniqueness has not been established. |
| Evidence linked to assumptions and proofs | A useful methodological and educational product; research novelty remains to be assessed. |
| Formal reconstruction of Durkheim | A proposed project; neither completed nor established as the first of its kind. |
| A new psychological or ethnological finding | Not established by the current formal file or review. |

The targeted search covered named proof assistants, voting theory, game theory, psychology, and Durkheim. It located decisive precedents for the broad activity. It did not establish a prior Lean reconstruction of the particular Durkheim claims discussed here. That search result is insufficient to claim none exists: projects can use different terminology, live outside indexed repositories, or remain unpublished. The search record states its bounds.

To make a stronger novelty claim, compare theorem statements and assumptions against the closest formal and informal predecessors. Reusing a known theorem to illuminate a neglected social-science question may be worthwhile even when the theorem is old. A publishable contribution might instead be a faithful reconstruction of a contested argument, a reusable verified model library, a previously unnoticed implication, or an empirical study that distinguishes rival mechanisms. Each would require its own evidence.

### 8 How the work reaches readers

**Available now:** the public GitHub main branch contains the research package, source evidence, and checked formal source. Friends can read the Markdown without installing Lean. PDFs provide a stable reading layout, and DOCX files support editing. The verification receipt identifies the exact checked source and build, rather than relying on a general claim that the repository is verified.

**Next public revision:** add this guide, keep the psychology recovery status visible, and maintain a brief change record. Invite corrections through the repository's normal discussion or issue mechanisms. A short shareable description is included in the publication folder. It is a draft for the project owner to use; no email or social-media message has been sent on the owner's behalf.

**A citable release:** after reviewing authorship, licensing, source rights, and the completeness of the imported corpus, choose a version and create an immutable release snapshot. Zenodo documents a GitHub-release archiving route that can assign a DOI [N06]. This integration has not been configured and no DOI has been issued for this project. Archival availability is different from peer review.

**A research submission:** obtain review from people competent in formal verification and the relevant social science. The formal review should check statements, assumptions, and reproducibility; the substantive review should check interpretation, evidence, and the model–world connection. A methods paper should clearly state its contribution beyond these elementary examples. A preprint venue should be selected for its actual subject scope and contribution. arXiv has subject, endorsement, and moderation requirements, so posting there cannot be promised [N07]. No journal submission or acceptance is claimed.

Dissemination should preserve a link from a claim to its evidence or theorem, the exact version containing it, and the limitations that govern its interpretation. A polished document must not quietly strengthen the claim made by the proof. When the evidence or formalization changes, both the plain-language explanation and the technical record must change together.

### 9 What has actually been verified

The first complete package on the requested repository was committed as `5eb4de33b6f03af1f689d710c239ededf2aaa708`. Its [GitHub Actions run](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36367099147) passed with Lean 4.19.0. The source contains no unfinished proof placeholders or custom social-science axioms. Eleven public results also have explicit axiom-dependency output; some rely on Lean's standard propositional extensionality and quotient soundness. The receipt records these dependencies.

The hosted local environment could not start the Lean executable successfully. The verified build occurred on the independent GitHub runner. This distinction matters for reproducibility and is retained in the record. Documentation-only changes do not create new formal results.

There are separate checks for source references, document structure, and output files. The documents are rendered and visually reviewed to catch broken tables, unreadable symbols, and layout problems. These checks establish that the supplied artifacts can be used as intended; they do not establish the empirical truth of their claims.

### 10 How to read the project critically

For every result, ask what its variables mean, which assumptions are supplied, what the theorem actually concludes, and what observations would support the interpretation. Check whether a mathematical possibility has been mistaken for a frequent outcome, whether a statistical association has been mistaken for a mechanism, and whether a value judgment has been presented as a proved fact.

The present research recommendation is conditional on equal rights, non-domination, and broadly shared material gains. Within those goals, the report favors investigating protected group voice, practical cooperation across groups, and accountable institutions. The full package has not been tested as one intervention. Lean does not select those values or certify that recommendation; it helps make narrower pieces of the reasoning inspectable.

The immediate next substantive tasks are to recover the earlier psychology source, obtain stronger access to decisive literature, and choose one mechanism for a richer model and empirical test. The proposed task-interdependence model provides a concrete route from the present examples toward classical sociology. It should earn its interpretation and usefulness through careful textual work, formal checking, and comparison with actual social life.

The guide's [references and access notes](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/main/projects/solidarity-at-scale/sources/formalization-prior-work.md) are also included at the end of the PDF and editable document. The [search record](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/main/projects/solidarity-at-scale/sources/formalization-search-log.md) explains the limits of the novelty assessment.


# The six new foundations: research report


Version 0.2 · 28 September 2026 UTC · A working research report prepared for Nolan Downard. The formal development was produced with AI assistance and checked by Lean. Independent scholarly review remains outstanding.

### 0 Executive brief

The project now has a foundation beyond solidarity and small groups: **measurement, identification, causal reasoning, learning, collective action, and aggregation**. Six new modules contain 51 theorem declarations. Together with the original 16, the repository contains 67 checked declarations. Supporting lemmas, illustrative counterexamples, and main results are included in that count; it is not a count of scientific discoveries.

Three particularly useful results are these. First, a difference between scores can reliably indicate an underlying ordering in a simple additive model if it exceeds an assumed bound on differential measurement bias. Second, identical observational information can be compatible with different causal effects, so an estimator cannot recover both effects without additional information or restrictions. Third, a coalition can have complementary capabilities and positive aggregate surplus while a member remains unwilling to participate under the chosen allocation.

These are established kinds of mathematical reasoning, now expressed in a small checked library with explicit assumptions. No field-level open problem has been solved. The immediate achievement is to make several research questions precise, answer their restricted versions, and identify the extra mathematics and evidence needed for broader answers.

The next highest-value step is a measurement-and-design development: replace exact integer scores with a justified statistical model, distinguish structural identification from estimation uncertainty, and test whether proposed observations separate psychological mechanisms. The larger earlier mathematics-of-psychology corpus must be recovered before choosing overlapping material to reimplement.

### 1 Scope and research question

The guiding question is: **Which inferences in social research can be made explicit enough to check, and which depend on information the model does not contain?** Solidarity is one application. The same question applies to a psychological scale, an experiment on learning, a comparison of institutions, or a cross-cultural association.

This is a foundations project in the practical sense of reusable definitions and verified implications. It does not propose a complete axiomatization of psychology or a reduction of culture to mathematics. Meanings, historical interpretation, construct validity, and the choice of outcomes require substantive inquiry.

Three distinct tasks govern the work: formalize a precise model, prove consequences inside it, and assess whether its assumptions represent the setting of interest. Only the first two are completed for the new elementary examples.

### 2 Method and evidence

This is a targeted methodological literature map paired with an executable formal development. It is not a systematic review, a meta-analysis, or a preregistered empirical study. Searches followed conceptual links from theory construction, computational-model recovery, and measurement invariance to social-network identification and cross-cultural dependence. Primary papers, author repositories, official teaching materials, and Lean documentation were preferred.

The [source register](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/sources/source-register.csv) records access depth and claim-bearing locations. Some sources were available as selected full-text passages; others only as abstracts, figure captions, or publisher summaries. Paywalls, challenges, and extraction failures are recorded in the [search log](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/sources/search-log.md). PsycINFO and subscription databases were not searched. The literature map cannot establish priority or exhaustiveness.

Formal work uses Lean 4.19.0 and its bundled standard library. The original source is preserved. A successful remote build and an audit of all 67 declarations establish the reported check status; this environment's local Lean launcher did not run successfully. See the [verification receipt](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/verification.md).

### 3 Why formalize these foundations?

Borsboom and colleagues distinguish the construction of a formal theoretical model from assessing its adequacy and wider scientific value [F01]. This project adds machine checking to a narrow part of that process: the step from explicit assumptions to consequences. It does not automate theory selection.

An informal argument can conceal a missing assumption. For example, comparing observed scores tacitly assumes something about how the instruments behave across groups. Inferring influence from resemblance tacitly assumes something about common causes. Inferring cooperation from collective benefit tacitly assumes something about allocation and individual incentives. Writing those arguments as theorem statements makes the missing premise visible.

The mathematical areas here are logic and functions, elementary algebra and inequalities, discrete modeling, causal identification, elementary learning theory, and a small part of cooperative economic reasoning. The original network module uses graph-like reachability, and its donation game is game theory. Using integers for scores and tokens does not make the project a contribution to number theory. Combinatorics will matter more when finite populations, networks, and experiment designs are developed.

### 4 Identifiability: can observations distinguish explanations?

Let a candidate mechanism predict an output for each available probe. Two candidates are observationally equivalent under a design when they produce the same output at every probe that design permits. The design identifies the candidate when equivalent candidates must be equal.

The module proves that adding probes preserves any identification already achieved. It also proves that applying the same transformation to identical outputs cannot create a distinction. This provides a common interface for measurement and aggregation: one concerns the observations a design supplies, the other the distinctions its summaries discard.

In the worked example, two unknown integer components are `a` and `b`. The baseline probe reports `a + b`; a second probe reports `a`. Baseline data cannot distinguish `(1, 0)` from `(0, 1)`. With both exact probes, the first component and then the second are identified. This answers a specific design question, not the general problem of experimental design.

For psychology, the components might provisionally represent two mechanisms contributing to a response. That interpretation is a proposal, not a validated measurement equation. Wilson and Collins discuss parameter and model recovery as practical checks in computational behavioral modeling [F02]. Our result addresses exact structural distinguishability; it supplies no finite-sample recovery guarantee or evidence that these two mechanisms describe people.

### 5 Measurement: what does a score comparison mean?

The illustrative measurement equation is `observed = latent + intercept`. A common intercept preserves order and differences. But increasing every latent value by an amount and decreasing the intercept by the same amount changes no observations. An arbitrary origin is therefore not recoverable from these observations alone. Knowing an intercept identifies a person's latent score; knowing an anchor's latent value identifies the intercept in this restricted equation.

For two observations, let the observed difference be `d` and the intercept difference lie between `−δ` and `δ`. The theorem establishes that the latent difference lies in the interval `[d − δ, d + δ]`. If the observed difference exceeds the upper bound on differential bias, its sign identifies the latent ordering. The interval is a **sensitivity bound**, not a statistical confidence interval. The theorem assumes the bound; it neither estimates nor validates it.

For example, an observed difference of 5 with a justified differential-bias bound of 2 constrains the latent difference to 3 through 7 in these score units. If the bound is 6, the corresponding interval crosses zero, so the ordering is unresolved by this argument. An explicit counterexample shows that unequal intercepts can reverse an ordering.

Measurement-invariance research concerns whether comparisons retain their intended interpretation across groups or occasions [F03]. Our one-indicator, unit-loading, error-free integer model is much narrower than factor analysis or item-response theory. It does not establish invariance for any existing instrument, equate constructs across cultures, or justify comparing populations merely because a common numeric label is available.

### 6 Causality: why more of the same observations may not settle a mechanism

The causal example has a binary background variable `U`, treatment `T`, and outcome `Y`. Observational assignment sets `T = U`. Model A sets `Y = T`; Model B sets `Y = U`. In both, the observed treatment and outcome are `(U, U)` for either possible background value.

An intervention that sets treatment to true while background is false separates the models: A yields true and B yields false. The code sums the treatment contrasts over both background values. This numerator is 2 in A and 0 in B; under a uniform background distribution the average effects would be 1 and 0. Probability and division are not implemented in this module.

The impossibility theorem quantifies over every estimator that takes only the observational function as input. Such an estimator receives equal inputs in these two cases, so it must give the same answer, although the correct numerators differ. Consequently no such estimator is correct for every model in the specified class. This is a counterexample to unrestricted observational identification, not a claim that all causal inference from observational data is impossible.

Social resemblance poses related identification problems. Shalizi and Thomas analyze latent homophily and contagion [F04]. McFowland and Shalizi give positive consistency results under particular latent-network and linear-outcome assumptions [F05]. These are complementary warnings about assumptions, not mutually exclusive verdicts. The new binary theorem is not a formalization of either full paper and does not solve peer-effect identification in realistic networks.

### 7 Learning: exact consistency and its limits

The learning module defines a hypothesis as a function from inputs to labels. It fits a finite evidence list when it assigns every recorded input its recorded label. Adding evidence can only remove fitting hypotheses; a query at which two hypotheses disagree can eliminate a rival when the true label is supplied.

The proofs also expose the fragility of exact fitting. Two different labels at the same input make exact consistency impossible. A single incorrect label excludes the true hypothesis. Duplicating the same list adds no new exact-consistency constraint. That last statement does **not** say that repeated independent measurements are statistically useless: probability, noise, and evidence weight are absent here.

This is the logical core of a version-space perspective on learning, an established tradition [F08]. It is not the full candidate-elimination algorithm and includes no efficient representation of general and specific hypothesis boundaries. It does not prove how people learn cultural signs, update beliefs, or acquire concepts. Those applications would need an explicit account of noise, changing meanings, memory, sampling, and social context.

### 8 Collective action: complementarity, allocation, and participation

Here a group is feasible when each required task has a capable member. Two specialists with different capabilities can jointly cover tasks that neither can cover alone. If the only capable member for a needed task withdraws, the remaining group cannot cover every task. These statements are useful starting points for division of labor and organizational dependence.

Participation is a separate condition: each member's reward must meet their cost, relative to a zero outside option. A synthetic two-person economy has cost 1 for each person and rewards 0 and 3. Total reward exceeds total cost, but the first person's participation constraint fails. Changing the allocation to 1 and 2 satisfies both constraints and retains feasible task coverage.

More generally, with two costs and a fixed budget, an unrestricted integer allocation satisfying both constraints exists exactly when the budget covers the sum of the costs. The acceptable share for the first member runs from their cost to the budget minus the second member's cost. This is a complete answer within the model, not a new result in bargaining theory.

The comparison is inspired by the distinction between similarity and interdependence discussed in the original Durkheim reading [S14 in the earlier bibliography]. It formalizes one possible representation of complementary roles, not Durkheim's theory as a whole. It does not establish trust, democratic legitimacy, justice, equilibrium, enforcement, or the social effects of ethnic diversity. Capabilities are not ethnicity. A member may perform arbitrarily many tasks here, with no time constraint; extending to matching or scheduling changes feasibility.

### 9 Aggregation: what disappears when we pool?

The synthetic table gives an exact reversal. Every cell has a positive denominator and a success count no larger than its total.

| Context | A successes / total | B successes / total | Higher observed rate |
| --- | --- | --- | --- |
| Context 1 | 9 / 10 | 80 / 100 | A: 90% versus 80% |
| Context 2 | 20 / 100 | 1 / 10 | A: 20% versus 10% |
| Pooled | 29 / 110 | 81 / 110 | B: approximately 73.6% versus 26.4% |

Lean verifies the comparisons by integer cross-multiplication, avoiding rounding. The groups have different context compositions. The familiar reversal belongs to established work on aggregation and contingency tables [F09]; these particular counts are synthetic examples, not research data.

A second result reuses the identifiability module: observing a sum loses the distinction between two possible component assignments, and subsequent recoding cannot recover it. For a sociologist this motivates checking the unit of inference. An aggregate association does not automatically specify the individual mechanism behind it.

Cross-cultural non-independence is a different problem. Societies can share ancestry, diffusion pathways, or common causes. HRAF's methods materials present multiple approaches [F07], and a 2026 article cautions against treating all dependence with one automatic adjustment [F06]. Neither that dependence nor a valid sampling correction is represented in the present aggregation module. A checked pooled-count example is not a solution to Galton's problem.

### 10 What is old, what is new, and what remains open?

The algebraic identification arguments, consistency lemmas, allocation condition, and aggregation reversal are established mathematical ideas. This release contributes their explicit Lean implementation, shared interfaces, and interpretation for the project's research questions. A distinct source file is not evidence of mathematical novelty. No claim is made to the first Lean proof of these facts.

Formalized social science has substantial predecessors. For example, Holliday, Norman, and Pacuit developed voting theory in Lean [F10]. The earlier [formalization review](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/solidarity-at-scale/sources/formalization-prior-work.md) also records social-choice and game-theory projects. Upstream projects were not rebuilt as part of this expansion.

The [problem register](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/open-problems.md) identifies six bounded questions now resolved, seven proposed development tasks, and several broader methodological challenges. A source's historical future-work suggestion is a research lead until current literature establishes that it remains open. We do not label a problem open merely because this repository lacks a proof.

### 11 Process integrity

The implementation preserves `Solidarity.lean` and adds separate modules. Source hashes, the pinned toolchain, theorem inventory, complete axiom-printing audit, and successful CI run are recorded. Every new declaration has an explanation. The proof count is separated from substantive-result count, and the original psychology import remains explicitly pending.

The initial staging check found a Lean elaboration issue in three concrete rate comparisons. Unfolding their named predicate exposed the decidable arithmetic; the subsequent build and audit passed. There are no admitted goals or custom scientific assumptions declared as axioms. Reported logical dependencies are limited to Lean's standard `propext`, `Classical.choice`, and `Quot.sound`, with some proofs using none. No independent second-kernel verification or external human code review is claimed.

The evidence process has limitations: a targeted search, incomplete full-text access, no dual screening, and no independent extraction check. A systematic-review quality score would be inappropriate. These limitations constrain claims about literature coverage and novelty; they do not replace the separate check of the stated mathematical implications.

### 12 Inference robustness

The main threats are model misspecification and interpretation, not arithmetic rounding. The measurement result depends on unit loadings and the assumed bias bound. The causal impossibility depends on which information and model class are allowed. Exact-learning results depend on deterministic labels. Coalition feasibility omits congestion and participation omits bargaining dynamics. Aggregation results concern a deliberately selected example rather than typical prevalence.

Several counterexamples make these boundaries concrete: an intercept can reverse a score ordering; common causes can mimic a treatment effect observationally; a wrong label can eliminate truth; positive total surplus can coexist with nonparticipation. The repository therefore gives both positive implications and reasons a tempting broader inference fails.

No empirical effect-size synthesis, heterogeneity statistic, publication-bias estimate, or sensitivity meta-analysis was conducted. There is no dataset from which to calculate them. The proposed empirical bridge is to specify constructs and observations, test recovery under a realistic data-generating model, examine assumption violations, and evaluate predictions on held-out data. Those tasks remain to be done.

### 13 Next development and publication

Priority one is recovering and validating the prior psychology corpus. In parallel, the most coherent mathematical extension is to connect measurement ambiguity with experiment selection: which anchors or probes remove which equivalence classes, and how does a bounded perturbation change the answer? Any substantive novelty claim would then require a focused comparison with existing identification and design results.

Priority two adds probability and noisy observations, using a maintained mathematical library after checking toolchain compatibility. Priority three develops finite task assignment, outside options, and enforceable allocation. An anthropology track should specify cultural descent and diffusion separately before proposing a dependence correction. These are scoped development tasks, not promises to solve whole disciplines.

The immediate public deliverable is the repository's main branch with code, this report, theorem explanations, and provenance. The [publication plan](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/publication.md) stages external review, archival release, and a possible methods manuscript. No messages to scholars, journal submission, preprint submission, or archival DOI have been sent or created by this expansion.

### 14 References and reusable materials

See the [annotated references](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/sources/references.md) for F01–F11 and access limits, and the [BibTeX export](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/sources/references.bib) for citation-manager import. The [source relationship file](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/sources/source-relations.csv) records connections proposed in this synthesis; these are not automatically claims of direct citation between the original authors. The [Obsidian-compatible reading note](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/notes/foundations-map.md) uses ordinary Markdown and relative links. No live Zotero collection or private vault has been changed.

The [theorem guide](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/theorem-guide.md), [problem register](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/open-problems.md), and [verification receipt](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/verification.md) complete the bridge between the prose, the precise formal claims, and the check results.


# Every new theorem explained


The declarations below were checked with Lean 4.19.0. The [verification receipt](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/verification.md) gives the exact source revision and audit. A theorem's name is a navigation aid; its statement and definitions determine what it says. Supporting lemmas and examples are included in the count. None is presented as a new empirical law.

Read each section as **model → implication → possible use → boundary**. The [research report](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/report.md) develops the applications and source context. The [inventory](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/theorem-inventory.csv) maps every name to its file and explanation. The [original guide](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/solidarity-at-scale/formal/what-lean-proves.md) continues to cover the earlier 16 declarations.

### 1 Identifiability — 9 declarations

[Source: Identifiability.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Identifiability.lean). Namespace: `SocialScience.Identifiability`.

A model parameter predicts an exact output for each probe. A design specifies which probes are available. `Equivalent` means two candidates give the same outputs on that design. `Identified` means no distinct candidates remain equivalent.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `equivalent_refl` | A candidate is observationally equivalent to itself. |
| `equivalent_symm` | If A and B are equivalent, B and A are equivalent. |
| `equivalent_trans` | Equivalence through a third candidate is transitive. |
| `restrict_design` | Candidates equivalent on a larger probe set remain equivalent on a subset. |
| `more_probes_preserve_identification` | Expanding an already identifying probe set preserves identification. |
| `postprocess_preserves_equivalence` | Applying one common function to equal outputs cannot distinguish them. |
| `baseline_ambiguous` | The sum-only probe gives the same output for component pairs `(1, 0)` and `(0, 1)`. |
| `baseline_not_identified` | Therefore the sum-only design does not identify both components over the specified parameter space. |
| `both_probes_identify` | Observing both the sum and the first component identifies the ordered pair exactly. |

**Psychology use:** before collecting data, ask whether the proposed task can distinguish the mechanisms being compared. **Boundary:** a structurally identifying task may still estimate parameters poorly with noisy, finite data. No statistical efficiency or human mechanism is proved here. Generalization is within the specified candidate class; omitted alternatives are not ruled out.

### 2 Measurement — 9 declarations

[Source: Measurement.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Measurement.lean). Namespace: `SocialScience.Measurement`.

The equation is `response = latent + intercept`, using integer units, a loading of one, and no random error. The latent value is a formal unknown, not a validated psychological construct.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `common_intercept_preserves_order` | With the same intercept, response order and latent order agree in both directions. |
| `common_intercept_preserves_difference` | The response difference equals the latent difference when intercepts match. |
| `shift_invariance` | Adding a shift to the latent value and subtracting it from the intercept leaves the response unchanged. |
| `population_shift_invariance` | The same shift can be made for every person while preserving the entire response function. |
| `known_intercept_identifies` | Equal responses with the same specified intercept imply equal latent values. |
| `anchor_identifies_intercept` | Equal responses for the same specified latent anchor imply equal intercepts. |
| `group_intercepts_can_reverse_order` | A concrete pair of unequal intercepts reverses a latent ordering in the responses. |
| `bounded_bias_interval` | If differential intercept bias lies between `−δ` and `δ`, the latent difference lies within `δ` of the observed difference. |
| `difference_exceeding_bias_identifies_order` | An observed difference larger than an upper bound on differential bias establishes the latent ordering. |

**Psychology use:** separate assumptions about comparable measurement from conclusions about group differences. The bound can support a sensitivity analysis once its size is substantively justified. **Boundary:** these are not results about reliability, factor-model fit, partial scalar invariance, or an actual instrument. An anchor that is only assumed comparable may conceal the very bias being investigated.

### 3 Causality — 6 declarations

[Source: Causality.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Causality.lean). Namespace: `SocialScience.Causality`.

Both models set observed treatment equal to a binary background variable. One model makes the outcome copy treatment; the other makes it copy background. The observational object is the exact mapping from background to the observed treatment–outcome pair. The effect numerator sums the two treatment contrasts over the two background values.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `observational_equivalence` | The two models have exactly the same observational mapping. |
| `intervention_disagreement` | At treatment true and background false, their intervention outcomes differ. |
| `treatment_effect_numerator` | The treatment-copy model has an effect numerator of 2. |
| `common_cause_numerator` | The background-copy model has an effect numerator of 0. |
| `no_universal_observational_estimator` | No function of this observational mapping returns the correct effect numerator for every candidate binary model. |
| `all_responses_identify` | If two deterministic models agree for every treatment and background combination, their outcome functions, and hence the models, are equal. |

**Social-science use:** identify what additional assumption or observation a causal claim requires. **Boundary:** the last theorem assumes complete exact response information, including background; it is not a proof that any randomized finite experiment recovers a whole causal model. The impossibility result does not prohibit identification in a restricted model class. No full causal graph calculus, sampling distribution, or network process is encoded.

### 4 Learning — 9 declarations

[Source: Learning.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Learning.lean). Namespace: `SocialScience.Learning`.

`Fits` means a deterministic hypothesis agrees with every input–label pair in a finite list. This describes exact consistency, not a likelihood or degree of belief.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `fits_empty` | Every hypothesis fits an empty evidence list. |
| `fits_cons_iff` | Fitting a new observation plus the old list is equivalent to matching the new label and fitting the old list. |
| `fits_append_iff` | Fitting two combined lists is equivalent to fitting each separately. |
| `more_evidence_narrows_models` | Any hypothesis fitting a larger evidence list fits its included sublist. |
| `truth_survives_correct_label` | A truth function that fits the old evidence still fits after one correctly labeled example. |
| `distinguishing_query_eliminates_rival` | A rival that disagrees at a queried input cannot fit evidence containing the truth's label there. |
| `conflicting_labels_impossible` | If the list assigns distinct labels to the same input, no deterministic hypothesis fits it. |
| `incorrect_label_excludes_truth` | An incorrect label excludes the truth function from exact-fitting candidates. |
| `duplicate_evidence_same_models` | Appending the same evidence list to itself changes no exact-fitting candidates. |

**Psychology use:** a transparent baseline for concept learning, cultural classification, or designing a discriminating query. **Boundary:** it includes no psychological process, memory constraint, noise model, prior, or finite-sample generalization bound. Repeated independent observations can still be informative in statistical models. The definition treats input meanings as stable; cultural change may violate that assumption.

### 5 Collective action — 10 declarations

[Source: CollectiveAction.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/CollectiveAction.lean). Namespace: `SocialScience.CollectiveAction`.

`Feasible` means every task has a capable group member. `Accepts` means every member's reward meets their cost. `Ready` is their conjunction. The name does not assert a real organization is ready to operate. Costs and rewards are integer tokens; outside options are normalized to zero.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `adding_members_preserves_feasibility` | Adding members cannot destroy task coverage when capabilities are fixed and uncongested. |
| `restricting_members_preserves_acceptance` | Removing members preserves the remaining members' participation inequalities when their rewards and costs stay fixed. |
| `union_accepts_iff` | A union satisfies these inequalities exactly when each component group does, using the same reward and cost functions. |
| `indispensable_member_withdrawal` | If every capable group member for a specified task must be one particular agent, excluding that agent makes coverage impossible. |
| `complementary_pair_feasible` | In the two-role example, the pair covers both tasks. |
| `no_specialist_alone_feasible` | Neither specialist alone covers both tasks. |
| `aggregate_surplus_not_participation` | Costs 1 and 1 with rewards 0 and 3 yield positive aggregate surplus but fail `Ready`. |
| `repaired_allocation_ready` | Rewards 1 and 2 cover both participation constraints in the feasible pair. |
| `two_person_budget_iff` | An acceptable division of an unrestricted integer budget exists exactly when it covers both costs in total. |
| `acceptable_share_interval` | A particular share is acceptable to both exactly when it lies between the first cost and budget minus the second cost. |

**Sociology use:** distinguish complementary roles, feasible production, allocation, and participation. **Boundary:** coverage does not enforce simultaneous scheduling; acceptance is a specified inequality, not a psychological survey response. `Ready` is not a Nash equilibrium or a core allocation. There is no strategic deviation model, property-rights mechanism, endogenous enforcement, or fairness criterion. A single person's withdrawal theorem does not demonstrate the original group was feasible unless that is separately established.

### 6 Aggregation — 8 declarations

[Source: Aggregation.lean](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Aggregation.lean). Namespace: `SocialScience.Aggregation`.

`Higher` compares rates by cross-multiplying natural-number counts. Positive denominators are required to interpret that predicate as a rate comparison. They are checked for the concrete example; the generic predicate alone does not enforce them.

| Declaration | Precisely scoped meaning |
| --- | --- |
| `reversal_cells_valid` | All four example cells have positive denominators and admissible success counts. |
| `first_stratum_advantage` | A's rate 9/10 exceeds B's rate 80/100 in context 1. |
| `second_stratum_advantage` | A's rate 20/100 exceeds B's rate 1/10 in context 2. |
| `pooled_reversal` | Pooling produces a higher rate for B: 81/110 versus 29/110. |
| `simpson_reversal` | The two within-context advantages and their pooled reversal hold together. |
| `equal_weight_addition_preserves_order` | Adding two integer inequalities with the same unit weights preserves order. This is not a theorem about arbitrary weighted means. |
| `aggregate_cannot_identify_components` | Reuses the proof that a sum-only observation cannot identify both unknown components. |
| `recoding_cannot_restore_components` | Any common recoding of that sum still leaves the demonstrated pair indistinguishable. |

**Anthropology and ethnology use:** scrutinize pooling and the level of an inference before attributing an aggregate pattern to an individual or cultural mechanism. **Boundary:** the example is synthetic, not an estimate of how often reversals occur. It does not decide which adjustment is causally appropriate or model shared ancestry and cultural diffusion.

### How these foundations fit together

Identifiability supplies the language for both informative measurements and lossy summaries. Measurement adds a particular response equation and sensitivity bound. Causality distinguishes observational equivalence from intervention behavior. Learning tracks which candidates remain compatible with exact evidence. Collective action separates capability constraints from participation constraints. Aggregation checks whether a summary preserves the comparison one intended to make.

That is a reusable starting point for formal research. The [problem register](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/open-problems.md) specifies what would have to be added before claiming a more realistic psychological or sociological result.


# What remains open


Status at 28 September 2026 UTC. **None of the results in this release is claimed to solve a field-level open problem.** An implementation gap, a proposed modeling question, and an unresolved scientific problem are different statuses. This register keeps them separate.

### A. Restricted questions answered in this release

| ID | Question and exact scope | Answer | Status |
| --- | --- | --- | --- |
| B01 | Can a sum-only probe identify two arbitrary integer components? Can adding the first-component probe help? | No for the first design; yes for both exact probes. | Established mathematical idea; verified model question. |
| B02 | What does an assumed differential intercept-bias bound imply in an additive score equation? | A latent-difference interval; its sign is determined when the observed gap exceeds the bound. | Elementary sensitivity result; verified model question. |
| B03 | Can every deterministic binary model's effect be recovered from the specified observational function? | No: two models have equal observations and different effects. | Standard non-identification argument; verified model question. |
| B04 | Does one discriminating, correctly labeled query eliminate a rival exact-fitting hypothesis? | Yes; a wrong label can also eliminate truth. | Established consistency reasoning; verified model question. |
| B05 | When can a two-person integer budget meet both participation constraints? | Exactly when it covers their combined costs, with the stated unrestricted transfers. | Elementary allocation condition; verified model question. |
| B06 | Can pooling reverse two within-context rate comparisons with valid counts? | Yes; the checked synthetic example supplies a witness. | Established aggregation phenomenon; verified model question. |

These are useful small answers. Calling them new solutions to long-standing open problems would be misleading. Their proofs are in the [theorem guide](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/theorem-guide.md).

### B. Concrete next formal developments

| ID / priority | Proposed task | Dependencies and completion criterion | Novelty status |
| --- | --- | --- | --- |
| D01 / first | Recover the earlier psychology corpus and map its constructs and theorems. | Original repository, archive, or git bundle; preserve hashes and provenance, reproduce its original build, then identify reusable modules. | Recovery and integration; not a new theorem. |
| D02 / first | Generalize additive measurement to several indicators and explicitly constrained anchors. | Specify parameter transformations and identify an exact invariance class; prove a necessary/sufficient condition for identification in that class, or give a counterexample. | Standard identification literature must be checked before any novelty claim. |
| D03 / first | Formalize distinguishing probe selection for a finite candidate family. | Finite hypotheses and probes; characterize identification as separation of each distinct pair; compare a proposed probe set with that condition. | Likely established combinatorial content; useful infrastructure. |
| D04 / next | Replace exact consistency with bounded corruption or probabilistic evidence. | Choose a noise model and loss; prove a survival/error bound with all sampling assumptions explicit. Extend from compatible toolchain/library support. | Established learning theory is the starting point; no new bound claimed. |
| D05 / next | Model finite tasks with capacity and nonzero outside options. | Explicit assignment function and budget constraints; prove when an assignment and acceptable allocation coexist. Avoid assuming one person has unlimited capacity. | Matching, scheduling, and cooperative-game predecessors need comparison. |
| D06 / next | Prove aggregation conditions under fixed common composition weights. | Positive denominators, common weights, and a specified target estimand; distinguish arithmetic preservation from causal adjustment. | Established statistics and order properties; formalization target. |
| D07 / later | Express a restricted social-network causal identification result. | First formalize the graph, latent variables, probability assumptions, and observation scheme. Reproduce a published positive result before weakening assumptions. | F04–F05 are predecessors; not an unclaimed open theorem. |

No deadline or unattended continuation is implied. These tasks are ordered so later proofs reuse earlier definitions rather than accumulating disconnected examples.

### C. Broader scientific questions that remain unresolved here

**Measurement across settings.** When do different languages, response styles, social roles, and settings preserve the construct being measured? Identification conditional on a measurement equation is not evidence for that equation. A worthwhile project combines formal invariances with instrument-specific validity evidence. F03 is methodological background, not proof that no adequate methods already exist.

**Mechanism discrimination in psychology.** Which feasible tasks distinguish competing theories once noise and model misspecification are allowed? D02–D04 provide possible building blocks. The practical challenges discussed in F01–F02 cannot be solved by treating a model's parameters as observed facts.

**Homophily and social influence.** Which restrictions identify effects in a particular network, and how sensitive are estimates to violations? F04 gives a confounding analysis; F05 gives positive results in restricted settings. F05's preprint also mentions possible extensions involving support conditions and finite-sample bias bounds. Those are **historical research leads**: this search did not establish that they remain open in 2026. They are not advertised as unsolved targets ready for a novelty claim.

**Cultural dependence and comparison.** How should ancestry, diffusion, shared environments, and measurement differences enter a particular causal question? F06–F07 motivate making those pathways explicit. Generic dependence adjustment can answer the wrong question. This release does not estimate a cross-cultural effect or recommend a universal correction.

**Institutional stability and distribution.** Can cooperation persist when rewards, enforcement, outside options, and capabilities change together? The allocation condition here says only that a feasible transfer exists. Existence does not supply a bargaining process, credible commitment, political legitimacy, or a criterion of justice. Each of those requires its own definitions and evidence.

**Composition across social levels.** Which relationships survive moving from individuals to organizations, regions, and nations? A nesting map for memberships is not proof of self-similar causal dynamics. A concrete next case should define the lower-level dynamics, the aggregation map, and the macro-level claim before attempting a preservation theorem.

### D. What would count as an actual advance?

A new theorem would need a precise statement, a comparison against the strongest relevant prior results, a proof, and independent review of both its correctness and novelty. A new empirical result would additionally need valid measures, appropriate data, a credible design, and uncertainty analysis. A new formalization can be valuable without either kind of scientific novelty, but should say exactly which established result it encodes and which prior libraries it reuses.

For this release, the defensible claims are checked elementary results, explicit assumptions, useful counterexamples, and a connected implementation. See [references and access depth](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/sources/references.md) and [verification](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/verification.md).

# Part III Evidence and source code


# References and access notes for the new foundations


Targeted methodological reading for Foundations I. Accessed 28 September 2026 UTC. These records distinguish inspected material from reading leads. Identifiers are stable across the report, BibTeX, and source register. No exhaustive priority search is claimed.

### F01 — Theory construction

Borsboom, D., van der Maas, H. L. J., Dalege, J., Kievit, R. A., and Haig, B. D. (2021). *Theory Construction Methodology: A Practical Framework for Building Theories in Psychology*. Perspectives on Psychological Science, 16(4), 756–766. [DOI](https://doi.org/10.1177/1745691620969647) · [Author manuscript](https://pure.uva.nl/ws/files/68321294/1745691620969647.pdf).

Access: selected full-text sections, especially steps 3–5, printed pages 761–762. Formal-model development is followed by adequacy and theory evaluation; proof checking here contributes to only part of that process.

### F02 — Computational-model recovery

Wilson, R. C., and Collins, A. G. E. (2019). *Ten simple rules for the computational modeling of behavioral data*. eLife, 8, e49547. [DOI](https://doi.org/10.7554/eLife.49547) · [PubMed record](https://pubmed.ncbi.nlm.nih.gov/31769410/).

Access: abstract and figure captions, including Boxes 4–7. Publisher and archival attempts encountered challenges or failed retrievals. Used for the importance of parameter/model recovery; no full methods extraction or replication was performed.

### F03 — Measurement comparability

Putnick, D. L., and Bornstein, M. H. (2016). *Measurement Invariance Conventions and Reporting: The State of the Art and Future Directions for Psychological Research*. Developmental Review, 41, 71–90. [DOI](https://doi.org/10.1016/j.dr.2016.06.004) · [PubMed record](https://pubmed.ncbi.nlm.nih.gov/27942093/).

Access: abstract and bibliographic metadata. Full-text routes were blocked or challenged. Supports the methodological relevance of comparability across groups and occasions; the new additive proofs are independent derivations, not a formalization of this review's full framework.

### F04 — Confounding in social networks

Shalizi, C. R., and Thomas, A. C. (2011). *Homophily and Contagion Are Generically Confounded in Observational Social Network Studies*. Sociological Methods & Research, 40, 211–239. [DOI](https://doi.org/10.1177/0049124111404820) · [Author preprint](https://arxiv.org/abs/1004.4704).

Access: preprint introduction and identification discussion, especially sections 1–2; not an independent audit of every derivation. This is a network-specific predecessor, substantially richer than the binary counterexample in this repository.

### F05 — Identification under additional structure

McFowland III, E., and Shalizi, C. R. (2023). *Estimating Causal Peer Influence in Homophilous Social Networks by Inferring Latent Locations*. Journal of the American Statistical Association, 118, 707–718. [DOI](https://doi.org/10.1080/01621459.2021.1953506) · [Author preprint](https://arxiv.org/abs/1607.06565).

Access: 2021 preprint revision, abstract and selected sections 2–3, including assumptions and Theorem 2. Positive results require specified latent-network, exogeneity, and outcome assumptions. Historical future-work suggestions were not verified as still open.

### F06 — Cross-cultural dependence

Akaliyski, P., and Sng, O. (2026; first online 1 September 2025). *Non-Independence of Nations: Revisiting a Centuries-Old Methodological Challenge*. Cross-Cultural Research, 60(1), 3–22. [Publisher and DOI](https://doi.org/10.1177/10693971251375124).

Access: publisher abstract and metadata; full text requires access. The authors distinguish dependence mechanisms and caution against an automatic universal correction. Their simulations were not inspected or reproduced here.

### F07 — Cross-cultural sampling instruction

Human Relations Area Files, Yale University (undated). *Sampling for Cross-Cultural Anthropological Research*. [Official methods page](https://hraf.yale.edu/advanced-ccc/8.%20Sampling%20for%20Cross-Cultural%20Anthropological%20Research/sampling.html).

Access: page descriptions of lessons by Carol Ember and Fiona Jordan. Embedded lectures and slides were not fully reviewed. The page includes contrasting views on Galton's problem; it is a methods gateway, not an empirical effect estimate.

### F08 — Version spaces

Mitchell, T. M. (1997). *Machine Learning*, chapter 2. McGraw-Hill. [Author's book page](https://www.cs.cmu.edu/~tom/mlbook.html) · [Textbook lecture slides hosted by CMU](https://www.cs.cmu.edu/afs/cs/academic/class/45873-f98/classnotes/ch2.pdf).

Access: author metadata; slides visually inspected at PDF pages 10, 19, and 21 (printed slide numbers 31, 40, and 42) after text extraction failed. The consistency/version-space definition is on PDF page 10. The book download failed; no full-book reading is claimed.

### F09 — Contingency-table precedent

Simpson, E. H. (1951). *The Interpretation of Interaction in Contingency Tables*. Journal of the Royal Statistical Society: Series B, 13(2), 238–241. [Publisher summary and DOI](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x).

Access: publisher summary and metadata, not the complete article. Historical attribution only. The release's numerical table is a synthetic construction verified directly in Lean, not data or an example extracted from this paper.

### F10 — Prior Lean social-choice work

Holliday, W. H., Norman, C., and Pacuit, E. (2021). *Voting Theory in the Lean Theorem Prover*. LORI VIII postprint, arXiv:2110.08453. [Primary preprint record](https://arxiv.org/abs/2110.08453).

Access: abstract/metadata checked for this release; the earlier project guide also records reading the preprint. Establishes prior Lean voting-theory work. Its development was not rebuilt here. This record corresponds to N02 in the earlier formalization review.

### F11 — What a Lean check establishes

Lean project (current online manual). *Validating a Lean Proof*. [Official documentation](https://lean-lang.org/doc/reference/latest/ValidatingProofs/).

Access: proof-checking and axiom-printing sections. The online manual describes newer releases as well; the actual build receipt establishes behavior of this project's pinned Lean 4.19.0. Kernel acceptance and the intended interpretation of a theorem remain separate questions.

### Earlier project sources

The limited Durkheim connection uses the earlier source **S14**, preserved with its excerpt-only access record in [the original bibliography](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/solidarity-at-scale/sources/references.md). Broader game-theory and social-choice precedents are in [the original formalization review](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/solidarity-at-scale/sources/formalization-prior-work.md). Neither a historical theory nor an entire discipline is certified by the new modules.


# Verification receipt


The 51 new and 16 preserved theorem declarations passed Lean 4.19.0. This receipt identifies the proof-source check; the repository's workflow separately checks subsequent documentation commits and main.

| Item | Recorded result |
| --- | --- |
| Checked source commit | [`099908b5d781adc2d5bcdecfe909e57ec75776c4`](https://github.com/Sodelin/Formalizing-Soft-Sciences/commit/099908b5d781adc2d5bcdecfe909e57ec75776c4) |
| Successful workflow | [Run 36369678567](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36369678567) |
| Job | 108763148520, conclusion `success` |
| Toolchain | Lean 4.19.0, compiler commit `6caaee842e94`, Linux x86_64 |
| Build | `lake build`, both libraries |
| Full declaration audit | `lake env lean SocialScience/Audit.lean`, all 67 declarations |
| Source policy | No admitted goals, custom axioms, or native decision shortcuts in the project's Lean sources |
| Logical dependencies | Only `propext`, `Classical.choice`, and `Quot.sound`, or no axioms |
| Existing work | `Solidarity.lean` retained unchanged; its 16 declarations remain in the audit |

The [saved check output](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/formal-check-output.txt) includes the build result and logical dependencies. The [manifest](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/projects/foundations/verification-manifest.json) records SHA-256 digests of all nine Lean files and the two toolchain/build configuration files. Later commits may add documentation without changing those checked source bytes. The check script refuses a hash mismatch rather than assuming that a later file still has the old verification status.

The initial [staging run](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36369590300) failed because three rate comparisons needed their named predicate unfolded before Lean could select decidable arithmetic. The fix changed only those proof scripts; the next run passed. This failed attempt is part of the provenance and was not represented as a successful check.

The local Lean launcher returned `error: failed to locate application`, so no successful local compilation is claimed. Compilation occurred on GitHub Actions using the official pinned Lean release. No independent external proof checker, adversarial proof audit, or human peer review was performed. Standard kernel checks and the documented dependencies establish logical derivability of the written statements; they do not establish empirical applicability or novelty.

### Reproduce from the repository root

```sh
lake build
lake env lean SocialScience/Audit.lean
python3 scripts/check_foundations.py
python3 projects/solidarity-at-scale/scripts/validate_project.py --check-only
```

The Python checks verify documentation structure, theorem coverage, hashes, and recorded audit content. They do not run Lean themselves. The workflow runs the build and these checks separately. The earlier validation script's `--check-only` option preserves its historical manifest.


# Appendix Complete Lean source

The code below is copied from the merged source snapshot. The links point to commit `780f1b83aef15a9cf455566bab9df2a47d738074`. The source includes definitions and theorems; the audit file lists all 67 declarations. Read the preceding theorem guides for meaning.


## Solidarity.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/Solidarity.lean)

```lean
import Std

/-! Elementary results separating network reach, membership, and incentives.
These are model implications, not empirical or normative conclusions.
Only Lean's bundled standard library is needed. -/
namespace Solidarity

def Adj (a b : Nat) : Prop := b = a + 1 ∨ a = b + 1

inductive Reach : Nat → Nat → Prop where
  | refl (a : Nat) : Reach a a
  | step {a b c : Nat} : Reach a b → Adj b c → Reach a c

theorem adj_symm {a b : Nat} (h : Adj a b) : Adj b a := Or.symm h

theorem reach_trans {a b c : Nat} (h : Reach a b) (g : Reach b c) : Reach a c := by
  induction g with
  | refl => exact h
  | step _ edge ih => exact Reach.step ih edge

theorem reach_symm {a b : Nat} (h : Reach a b) : Reach b a := by
  induction h with
  | refl => exact Reach.refl _
  | step _ edge ih =>
    exact reach_trans (Reach.step (Reach.refl _) (adj_symm edge)) ih

theorem zero_reaches (n : Nat) : Reach 0 n := by
  induction n with
  | zero => exact Reach.refl 0
  | succ n ih => exact Reach.step ih (Or.inl rfl)

theorem path_connected (a b : Nat) : Reach a b :=
  reach_trans (reach_symm (zero_reaches a)) (zero_reaches b)

/-- Each vertex's neighbors are contained in a set of at most two vertices. -/
theorem at_most_two_neighbors (a b : Nat) (h : Adj a b) :
    b = a + 1 ∨ b = a - 1 := by
  rcases h with h | h
  · exact Or.inl h
  · right; omega

/-- Arbitrarily many distinct vertices remain reachable with this degree bound. -/
theorem unbounded_reachable (bound : Nat) :
    ∃ n, bound < n ∧ Reach 0 n :=
  ⟨bound + 1, Nat.lt_succ_self bound, zero_reaches (bound + 1)⟩

def Included {α : Type} (localGroup largerGroup : α → Prop) : Prop :=
  ∀ x, localGroup x → largerGroup x

theorem membership_nesting {α : Type} {a b c : α → Prop}
    (ab : Included a b) (bc : Included b c) : Included a c :=
  fun x hx => bc x (ab x hx)

/-- Overlap, A-only, and B-only witnesses inside one common population. -/
theorem overlapping_memberships :
    ∃ (a b common : Nat → Prop),
      Included a common ∧ Included b common ∧
      (∃ x, a x ∧ b x) ∧ (∃ x, a x ∧ ¬ b x) ∧ (∃ x, b x ∧ ¬ a x) := by
  refine ⟨(fun n => n = 0 ∨ n = 1), (fun n => n = 0 ∨ n = 2),
    (fun _ => True), ?_, ?_, ?_, ?_, ?_⟩
  · intro _ _; trivial
  · intro _ _; trivial
  · exact ⟨0, Or.inl rfl, Or.inl rfl⟩
  · refine ⟨1, Or.inr rfl, ?_⟩; omega
  · refine ⟨2, Or.inr rfl, ?_⟩; omega

/-- Connectedness places no constraint on an independent trust relation. -/
theorem connected_without_trust :
    ∃ trust : Nat → Nat → Prop,
      (∀ a b, Reach a b) ∧ ¬ trust 0 1 := by
  exact ⟨(fun _ _ => False), path_connected, fun h => h⟩

/- A two-player donation game. True = contribute, false = defect.
Benefit accrues from the other's contribution. Each contributor pays cost.
A reliable external institution charges sanction to each defector.
Payoffs are integer tokens. Institution financing and legitimacy are omitted. -/
def payoff (benefit cost sanction : Int) (own other : Bool) : Int :=
  (if other then benefit else 0) - (if own then cost else sanction)

def StableCC (benefit cost sanction : Int) : Prop :=
  ∀ deviation : Bool,
    payoff benefit cost sanction deviation true ≤ payoff benefit cost sanction true true

/-- Exact condition for mutual contribution to resist unilateral deviation. -/
theorem cooperation_stable_iff (benefit cost sanction : Int) :
    StableCC benefit cost sanction ↔ cost ≤ sanction := by
  constructor
  · intro h
    have hfalse := h false
    simp [payoff] at hfalse
    omega
  · intro h deviation
    cases deviation <;> simp [payoff] <;> omega

theorem no_sanction_failure (benefit cost : Int) (positive : 0 < cost) :
    ¬ StableCC benefit cost 0 := by
  intro h
  have hc := (cooperation_stable_iff benefit cost 0).mp h
  omega

/-- Attribute labels play no payoff role in this specified model. -/
theorem heterogeneous_cooperation_exists :
    ∃ labels : Bool → Bool,
      labels false ≠ labels true ∧ StableCC 3 1 2 := by
  refine ⟨id, by decide, ?_⟩
  exact (cooperation_stable_iff 3 1 2).mpr (by decide)

theorem homogeneous_cooperation_can_fail :
    ∃ labels : Bool → Bool,
      labels false = labels true ∧ ¬ StableCC 3 1 0 := by
  exact ⟨(fun _ => false), rfl, no_sanction_failure 3 1 (by decide)⟩

/-- Same symbols cannot change stability when they do not enter the payoffs. -/
theorem symbols_alone_insufficient :
    ∃ marker : Bool → Nat,
      marker false = marker true ∧ ¬ StableCC 3 1 0 := by
  exact ⟨(fun _ => 7), rfl, no_sanction_failure 3 1 (by decide)⟩

/-- Mutual contribution also improves on mutual defection when this holds. -/
theorem mutual_gain (benefit cost sanction : Int) (h : cost < benefit + sanction) :
    payoff benefit cost sanction false false < payoff benefit cost sanction true true := by
  simp [payoff]
  omega

#print axioms path_connected
#print axioms at_most_two_neighbors
#print axioms unbounded_reachable
#print axioms membership_nesting
#print axioms overlapping_memberships
#print axioms connected_without_trust
#print axioms cooperation_stable_iff
#print axioms heterogeneous_cooperation_exists
#print axioms homogeneous_cooperation_can_fail
#print axioms symbols_alone_insufficient
#print axioms mutual_gain
end Solidarity
```


## SocialScience.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience.lean)

```lean
import SocialScience.Identifiability
import SocialScience.Measurement
import SocialScience.Causality
import SocialScience.Learning
import SocialScience.CollectiveAction
import SocialScience.Aggregation

/-! Foundations for explicit social-scientific models. Every result is conditional
on its definitions and assumptions. Empirical applicability requires separate evidence. -/
```


## SocialScience/Identifiability.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Identifiability.lean)

```lean
import Std

namespace SocialScience.Identifiability

/-- A design is the set of probes whose outputs can be observed. -/
def Equivalent {Θ X Y : Type} (predict : Θ → X → Y) (design : X → Prop)
    (θ φ : Θ) : Prop := ∀ x, design x → predict θ x = predict φ x

/-- Structural identifiability, with exact outputs rather than noisy samples. -/
def Identified {Θ X Y : Type} (predict : Θ → X → Y) (design : X → Prop) : Prop :=
  ∀ θ φ, Equivalent predict design θ φ → θ = φ

theorem equivalent_refl {Θ X Y : Type} (predict : Θ → X → Y)
    (design : X → Prop) (θ : Θ) : Equivalent predict design θ θ :=
  fun _ _ => rfl

theorem equivalent_symm {Θ X Y : Type} {predict : Θ → X → Y}
    {design : X → Prop} {θ φ : Θ} (h : Equivalent predict design θ φ) :
    Equivalent predict design φ θ := fun x hx => (h x hx).symm

theorem equivalent_trans {Θ X Y : Type} {predict : Θ → X → Y}
    {design : X → Prop} {θ φ ψ : Θ}
    (h : Equivalent predict design θ φ) (g : Equivalent predict design φ ψ) :
    Equivalent predict design θ ψ := fun x hx => (h x hx).trans (g x hx)

theorem restrict_design {Θ X Y : Type} {predict : Θ → X → Y}
    {small large : X → Prop} {θ φ : Θ}
    (included : ∀ x, small x → large x) (h : Equivalent predict large θ φ) :
    Equivalent predict small θ φ := fun x hx => h x (included x hx)

theorem more_probes_preserve_identification {Θ X Y : Type} {predict : Θ → X → Y}
    {small large : X → Prop} (included : ∀ x, small x → large x)
    (h : Identified predict small) : Identified predict large :=
  fun θ φ g => h θ φ (restrict_design included g)

/-- Transforming indistinguishable outputs cannot make them distinguishable. -/
theorem postprocess_preserves_equivalence {Θ X Y Z : Type}
    {predict : Θ → X → Y} {design : X → Prop} {θ φ : Θ}
    (transform : Y → Z) (h : Equivalent predict design θ φ) :
    Equivalent (fun p x => transform (predict p x)) design θ φ :=
  fun x hx => congrArg transform (h x hx)

/-- The baseline probe observes a sum; the second probe isolates one component. -/
def twoComponent (θ : Int × Int) (probe : Bool) : Int :=
  if probe then θ.1 else θ.1 + θ.2

theorem baseline_ambiguous :
    Equivalent twoComponent (fun probe => probe = false) (1, 0) (0, 1) := by
  intro probe h
  subst probe
  decide

theorem baseline_not_identified :
    ¬ Identified twoComponent (fun probe => probe = false) := by
  intro h
  have bad := congrArg Prod.fst (h (1, 0) (0, 1) baseline_ambiguous)
  have : (1 : Int) = 0 := bad
  omega

theorem both_probes_identify : Identified twoComponent (fun _ => True) := by
  intro θ φ h
  have first := h true trivial
  have total := h false trivial
  simp [twoComponent] at first total
  apply Prod.ext
  · exact first
  · omega

end SocialScience.Identifiability
```


## SocialScience/Measurement.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Measurement.lean)

```lean
import SocialScience.Identifiability

namespace SocialScience.Measurement

/-- An illustrative additive indicator, in integer score units. -/
def response (latent intercept : Int) : Int := latent + intercept

theorem common_intercept_preserves_order (a b intercept : Int) :
    response a intercept ≤ response b intercept ↔ a ≤ b := by
  simp only [response]
  omega

theorem common_intercept_preserves_difference (a b intercept : Int) :
    response a intercept - response b intercept = a - b := by
  simp only [response]
  omega

theorem shift_invariance (latent intercept shift : Int) :
    response (latent + shift) (intercept - shift) = response latent intercept := by
  simp only [response]
  omega

theorem population_shift_invariance {Person : Type} (latent : Person → Int)
    (intercept shift : Int) :
    (fun p => response (latent p + shift) (intercept - shift)) =
      (fun p => response (latent p) intercept) := by
  funext p
  exact shift_invariance (latent p) intercept shift

theorem known_intercept_identifies (a b intercept : Int)
    (same : response a intercept = response b intercept) : a = b := by
  simp only [response] at same
  omega

theorem anchor_identifies_intercept (anchor first second : Int)
    (same : response anchor first = response anchor second) : first = second := by
  simp only [response] at same
  omega

/-- Unequal intercepts can reverse a latent ordering. This is a synthetic witness. -/
theorem group_intercepts_can_reverse_order :
    (0 : Int) < 1 ∧ response 1 0 < response 0 2 := by decide

/-- An assumed bound on differential bias yields a bound on the latent difference. -/
theorem bounded_bias_interval (a b biasA biasB δ : Int)
    (lower : -δ ≤ biasA - biasB) (upper : biasA - biasB ≤ δ) :
    (response a biasA - response b biasB) - δ ≤ a - b ∧
    a - b ≤ (response a biasA - response b biasB) + δ := by
  simp only [response]
  omega

theorem difference_exceeding_bias_identifies_order (a b biasA biasB δ : Int)
    (upper : biasA - biasB ≤ δ)
    (gap : δ < response a biasA - response b biasB) : b < a := by
  simp only [response] at gap
  omega

end SocialScience.Measurement
```


## SocialScience/Causality.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Causality.lean)

```lean
import SocialScience.Identifiability

namespace SocialScience.Causality

/-- Outcome indexed by treatment and an unobserved binary background variable. -/
structure BinaryModel where
  outcome : Bool → Bool → Bool

def treatmentEffect : BinaryModel := ⟨fun treatment _ => treatment⟩
def commonCause : BinaryModel := ⟨fun _ background => background⟩

/-- Observational assignment is treatment = background in both candidate models. -/
def observed (model : BinaryModel) (background : Bool) : Bool × Bool :=
  (background, model.outcome background background)

def indicator (b : Bool) : Int := if b then 1 else 0

/-- Twice the average treatment effect if background is uniformly distributed. -/
def effectNumerator (model : BinaryModel) : Int :=
  indicator (model.outcome true false) + indicator (model.outcome true true) -
  (indicator (model.outcome false false) + indicator (model.outcome false true))

theorem observational_equivalence : observed treatmentEffect = observed commonCause := by
  funext background
  rfl

theorem intervention_disagreement :
    treatmentEffect.outcome true false ≠ commonCause.outcome true false := by decide

theorem treatment_effect_numerator : effectNumerator treatmentEffect = 2 := by decide

theorem common_cause_numerator : effectNumerator commonCause = 0 := by decide

/-- No rule using only this observational function recovers every candidate's effect. -/
theorem no_universal_observational_estimator :
    ¬ ∃ estimate : (Bool → Bool × Bool) → Int,
      ∀ model, estimate (observed model) = effectNumerator model := by
  rintro ⟨estimate, correct⟩
  have same := congrArg estimate observational_equivalence
  have first := correct treatmentEffect
  have second := correct commonCause
  rw [treatment_effect_numerator] at first
  rw [common_cause_numerator] at second
  omega

/-- Complete exact response information suffices within this deterministic model class. -/
theorem all_responses_identify (first second : BinaryModel)
    (same : ∀ treatment background,
      first.outcome treatment background = second.outcome treatment background) :
    first = second := by
  cases first with
  | mk f =>
    cases second with
    | mk g =>
      have eq : f = g := by
        funext treatment background
        exact same treatment background
      cases eq
      rfl

end SocialScience.Causality
```


## SocialScience/Learning.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Learning.lean)

```lean
import Std

namespace SocialScience.Learning

/-- Exact consistency with a finite list of labeled observations. -/
def Fits {X Y : Type} (hypothesis : X → Y) (evidence : List (X × Y)) : Prop :=
  ∀ item, item ∈ evidence → hypothesis item.1 = item.2

theorem fits_empty {X Y : Type} (hypothesis : X → Y) : Fits hypothesis [] := by
  intro item h
  simp at h

theorem fits_cons_iff {X Y : Type} (hypothesis : X → Y) (x : X) (y : Y)
    (evidence : List (X × Y)) :
    Fits hypothesis ((x, y) :: evidence) ↔ hypothesis x = y ∧ Fits hypothesis evidence := by
  constructor
  · intro h
    constructor
    · exact h (x, y) (by simp)
    · intro item member
      exact h item (by simp [member])
  · rintro ⟨atNew, atOld⟩ item member
    simp only [List.mem_cons] at member
    rcases member with same | old
    · subst item
      exact atNew
    · exact atOld item old

theorem fits_append_iff {X Y : Type} (hypothesis : X → Y)
    (first second : List (X × Y)) :
    Fits hypothesis (first ++ second) ↔ Fits hypothesis first ∧ Fits hypothesis second := by
  constructor
  · intro h
    constructor
    · intro item member
      exact h item (List.mem_append.mpr (Or.inl member))
    · intro item member
      exact h item (List.mem_append.mpr (Or.inr member))
  · rintro ⟨hfirst, hsecond⟩ item member
    rcases List.mem_append.mp member with hf | hs
    · exact hfirst item hf
    · exact hsecond item hs

theorem more_evidence_narrows_models {X Y : Type} (hypothesis : X → Y)
    {small large : List (X × Y)} (included : ∀ item, item ∈ small → item ∈ large)
    (fitsLarge : Fits hypothesis large) : Fits hypothesis small :=
  fun item member => fitsLarge item (included item member)

theorem truth_survives_correct_label {X Y : Type} (truth : X → Y)
    (evidence : List (X × Y)) (x : X) (fits : Fits truth evidence) :
    Fits truth ((x, truth x) :: evidence) :=
  (fits_cons_iff truth x (truth x) evidence).mpr ⟨rfl, fits⟩

theorem distinguishing_query_eliminates_rival {X Y : Type} (truth rival : X → Y)
    (evidence : List (X × Y)) (x : X) (different : rival x ≠ truth x) :
    ¬ Fits rival ((x, truth x) :: evidence) := by
  intro fits
  exact different ((fits_cons_iff rival x (truth x) evidence).mp fits).1

theorem conflicting_labels_impossible {X Y : Type} (hypothesis : X → Y)
    (evidence : List (X × Y)) (x : X) (a b : Y)
    (first : (x, a) ∈ evidence) (second : (x, b) ∈ evidence) (different : a ≠ b) :
    ¬ Fits hypothesis evidence := by
  intro fits
  exact different ((fits (x, a) first).symm.trans (fits (x, b) second))

theorem incorrect_label_excludes_truth {X Y : Type} (truth : X → Y)
    (evidence : List (X × Y)) (x : X) (label : Y) (wrong : truth x ≠ label) :
    ¬ Fits truth ((x, label) :: evidence) := by
  intro fits
  exact wrong ((fits_cons_iff truth x label evidence).mp fits).1

/-- Duplicating the same list changes no exact-consistency constraint. -/
theorem duplicate_evidence_same_models {X Y : Type} (hypothesis : X → Y)
    (evidence : List (X × Y)) :
    Fits hypothesis (evidence ++ evidence) ↔ Fits hypothesis evidence := by
  rw [fits_append_iff]
  exact ⟨fun h => h.1, fun h => ⟨h, h⟩⟩

end SocialScience.Learning
```


## SocialScience/CollectiveAction.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/CollectiveAction.lean)

```lean
import Std

namespace SocialScience.CollectiveAction

/-- Every required task has a capable member. Congestion and time are omitted. -/
def Feasible {Agent Task : Type} (canDo : Agent → Task → Prop)
    (group : Agent → Prop) : Prop := ∀ task, ∃ agent, group agent ∧ canDo agent task

/-- Individual participation constraints relative to a zero outside option. -/
def Accepts {Agent : Type} (cost reward : Agent → Int) (group : Agent → Prop) : Prop :=
  ∀ agent, group agent → cost agent ≤ reward agent

def Ready {Agent Task : Type} (canDo : Agent → Task → Prop)
    (cost reward : Agent → Int) (group : Agent → Prop) : Prop :=
  Feasible canDo group ∧ Accepts cost reward group

theorem adding_members_preserves_feasibility {Agent Task : Type}
    {canDo : Agent → Task → Prop} {small large : Agent → Prop}
    (included : ∀ agent, small agent → large agent) (h : Feasible canDo small) :
    Feasible canDo large := by
  intro task
  rcases h task with ⟨agent, member, capable⟩
  exact ⟨agent, included agent member, capable⟩

theorem restricting_members_preserves_acceptance {Agent : Type}
    {cost reward : Agent → Int} {small large : Agent → Prop}
    (included : ∀ agent, small agent → large agent) (h : Accepts cost reward large) :
    Accepts cost reward small := fun agent member => h agent (included agent member)

theorem union_accepts_iff {Agent : Type} (cost reward : Agent → Int)
    (first second : Agent → Prop) :
    Accepts cost reward (fun a => first a ∨ second a) ↔
      Accepts cost reward first ∧ Accepts cost reward second := by
  constructor
  · intro h
    exact ⟨fun a ha => h a (Or.inl ha), fun a ha => h a (Or.inr ha)⟩
  · rintro ⟨hf, hs⟩ a (ha | ha)
    · exact hf a ha
    · exact hs a ha

theorem indispensable_member_withdrawal {Agent Task : Type}
    (canDo : Agent → Task → Prop) (group : Agent → Prop) (agent : Agent) (task : Task)
    (unique : ∀ other, group other → canDo other task → other = agent) :
    ¬ Feasible canDo (fun other => group other ∧ other ≠ agent) := by
  intro h
  rcases h task with ⟨other, ⟨member, distinct⟩, capable⟩
  exact distinct (unique other member capable)

/-- A two-role economy: each agent can perform precisely their own role. -/
def specialist (agent task : Bool) : Prop := agent = task

theorem complementary_pair_feasible : Feasible specialist (fun _ => True) := by
  intro task
  exact ⟨task, trivial, rfl⟩

theorem no_specialist_alone_feasible (agent : Bool) :
    ¬ Feasible specialist (fun other => other = agent) := by
  intro h
  cases agent with
  | false =>
    rcases h true with ⟨other, member, capable⟩
    simp [specialist, member] at capable
  | true =>
    rcases h false with ⟨other, member, capable⟩
    simp [specialist, member] at capable

def unitCost (_ : Bool) : Int := 1
def unequalReward (agent : Bool) : Int := if agent then 3 else 0
def repairedReward (agent : Bool) : Int := if agent then 2 else 1

/-- Positive aggregate surplus does not entail individual willingness. -/
theorem aggregate_surplus_not_participation :
    unitCost false + unitCost true < unequalReward false + unequalReward true ∧
    ¬ Ready specialist unitCost unequalReward (fun _ => True) := by
  constructor
  · decide
  · intro h
    have bad := h.2 false trivial
    simp [unitCost, unequalReward] at bad

theorem repaired_allocation_ready :
    Ready specialist unitCost repairedReward (fun _ => True) := by
  refine ⟨complementary_pair_feasible, ?_⟩
  intro agent _
  cases agent <;> decide

/-- Exact feasible-transfer condition; transfers are unrestricted integers. -/
theorem two_person_budget_iff (costA costB budget : Int) :
    (∃ share : Int, costA ≤ share ∧ costB ≤ budget - share) ↔ costA + costB ≤ budget := by
  constructor
  · rintro ⟨share, first, second⟩
    omega
  · intro h
    exact ⟨costA, by omega, by omega⟩

theorem acceptable_share_interval (costA costB budget share : Int) :
    (costA ≤ share ∧ costB ≤ budget - share) ↔
      (costA ≤ share ∧ share ≤ budget - costB) := by omega

end SocialScience.CollectiveAction
```


## SocialScience/Aggregation.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Aggregation.lean)

```lean
import SocialScience.Identifiability

namespace SocialScience.Aggregation

/-- Cross-multiplied rate comparison; use only with positive denominators. -/
def Higher (successA sizeA successB sizeB : Nat) : Prop :=
  successB * sizeA < successA * sizeB

/-- All four synthetic cells are valid positive-denominator counts. -/
theorem reversal_cells_valid :
    9 ≤ (10 : Nat) ∧ 80 ≤ (100 : Nat) ∧ 20 ≤ (100 : Nat) ∧ 1 ≤ (10 : Nat) ∧
    0 < (10 : Nat) ∧ 0 < (100 : Nat) := by decide

theorem first_stratum_advantage : Higher 9 10 80 100 := by
  unfold Higher
  decide

theorem second_stratum_advantage : Higher 20 100 1 10 := by
  unfold Higher
  decide

theorem pooled_reversal : Higher (80 + 1) (100 + 10) (9 + 20) (10 + 100) := by
  unfold Higher
  decide

theorem simpson_reversal :
    Higher 9 10 80 100 ∧ Higher 20 100 1 10 ∧
    Higher (80 + 1) (100 + 10) (9 + 20) (10 + 100) :=
  ⟨first_stratum_advantage, second_stratum_advantage, pooled_reversal⟩

/-- Equal-weight addition preserves two count inequalities. -/
theorem equal_weight_addition_preserves_order (a b c d : Int)
    (first : a ≤ b) (second : c ≤ d) : a + c ≤ b + d := by omega

/-- A sum loses the component distinction even when values are exact. -/
theorem aggregate_cannot_identify_components :
    ¬ Identifiability.Identified Identifiability.twoComponent (fun probe => probe = false) :=
  Identifiability.baseline_not_identified

/-- No downstream recoding restores a distinction already lost by summing. -/
theorem recoding_cannot_restore_components {Y : Type} (recode : Int → Y) :
    Identifiability.Equivalent
      (fun p probe => recode (Identifiability.twoComponent p probe))
      (fun probe => probe = false) (1, 0) (0, 1) :=
  Identifiability.postprocess_preserves_equivalence recode Identifiability.baseline_ambiguous

end SocialScience.Aggregation
```


## SocialScience/Audit.lean

[View exact source](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/780f1b83aef15a9cf455566bab9df2a47d738074/SocialScience/Audit.lean)

```lean
import Solidarity
import SocialScience

/-! Logical dependency audit of every public theorem in both developments. -/
#print axioms Solidarity.adj_symm
#print axioms Solidarity.reach_trans
#print axioms Solidarity.reach_symm
#print axioms Solidarity.zero_reaches
#print axioms Solidarity.path_connected
#print axioms Solidarity.at_most_two_neighbors
#print axioms Solidarity.unbounded_reachable
#print axioms Solidarity.membership_nesting
#print axioms Solidarity.overlapping_memberships
#print axioms Solidarity.connected_without_trust
#print axioms Solidarity.cooperation_stable_iff
#print axioms Solidarity.no_sanction_failure
#print axioms Solidarity.heterogeneous_cooperation_exists
#print axioms Solidarity.homogeneous_cooperation_can_fail
#print axioms Solidarity.symbols_alone_insufficient
#print axioms Solidarity.mutual_gain
#print axioms SocialScience.Aggregation.reversal_cells_valid
#print axioms SocialScience.Aggregation.first_stratum_advantage
#print axioms SocialScience.Aggregation.second_stratum_advantage
#print axioms SocialScience.Aggregation.pooled_reversal
#print axioms SocialScience.Aggregation.simpson_reversal
#print axioms SocialScience.Aggregation.equal_weight_addition_preserves_order
#print axioms SocialScience.Aggregation.aggregate_cannot_identify_components
#print axioms SocialScience.Aggregation.recoding_cannot_restore_components
#print axioms SocialScience.Causality.observational_equivalence
#print axioms SocialScience.Causality.intervention_disagreement
#print axioms SocialScience.Causality.treatment_effect_numerator
#print axioms SocialScience.Causality.common_cause_numerator
#print axioms SocialScience.Causality.no_universal_observational_estimator
#print axioms SocialScience.Causality.all_responses_identify
#print axioms SocialScience.CollectiveAction.adding_members_preserves_feasibility
#print axioms SocialScience.CollectiveAction.restricting_members_preserves_acceptance
#print axioms SocialScience.CollectiveAction.union_accepts_iff
#print axioms SocialScience.CollectiveAction.indispensable_member_withdrawal
#print axioms SocialScience.CollectiveAction.complementary_pair_feasible
#print axioms SocialScience.CollectiveAction.no_specialist_alone_feasible
#print axioms SocialScience.CollectiveAction.aggregate_surplus_not_participation
#print axioms SocialScience.CollectiveAction.repaired_allocation_ready
#print axioms SocialScience.CollectiveAction.two_person_budget_iff
#print axioms SocialScience.CollectiveAction.acceptable_share_interval
#print axioms SocialScience.Identifiability.equivalent_refl
#print axioms SocialScience.Identifiability.equivalent_symm
#print axioms SocialScience.Identifiability.equivalent_trans
#print axioms SocialScience.Identifiability.restrict_design
#print axioms SocialScience.Identifiability.more_probes_preserve_identification
#print axioms SocialScience.Identifiability.postprocess_preserves_equivalence
#print axioms SocialScience.Identifiability.baseline_ambiguous
#print axioms SocialScience.Identifiability.baseline_not_identified
#print axioms SocialScience.Identifiability.both_probes_identify
#print axioms SocialScience.Learning.fits_empty
#print axioms SocialScience.Learning.fits_cons_iff
#print axioms SocialScience.Learning.fits_append_iff
#print axioms SocialScience.Learning.more_evidence_narrows_models
#print axioms SocialScience.Learning.truth_survives_correct_label
#print axioms SocialScience.Learning.distinguishing_query_eliminates_rival
#print axioms SocialScience.Learning.conflicting_labels_impossible
#print axioms SocialScience.Learning.incorrect_label_excludes_truth
#print axioms SocialScience.Learning.duplicate_evidence_same_models
#print axioms SocialScience.Measurement.common_intercept_preserves_order
#print axioms SocialScience.Measurement.common_intercept_preserves_difference
#print axioms SocialScience.Measurement.shift_invariance
#print axioms SocialScience.Measurement.population_shift_invariance
#print axioms SocialScience.Measurement.known_intercept_identifies
#print axioms SocialScience.Measurement.anchor_identifies_intercept
#print axioms SocialScience.Measurement.group_intercepts_can_reverse_order
#print axioms SocialScience.Measurement.bounded_bias_interval
#print axioms SocialScience.Measurement.difference_exceeding_bias_identifies_order
```
