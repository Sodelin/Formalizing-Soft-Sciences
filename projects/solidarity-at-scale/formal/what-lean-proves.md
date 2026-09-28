# What Lean proves in our sociology and psychology research

## A reader guide to the mathematics the evidence and the next research steps

Prepared for Nolan Downard and readers of Formalizing Soft Sciences. Research assistance by Codex. Version 0.1, 27 September 2026 Pacific time.

**Lean checks whether a precisely written conclusion follows from precisely written definitions and assumptions.** Our current project uses that ability to separate personal connections, group membership, trust, and incentives. Its 16 checked theorems clarify what follows inside a few small models. They do not establish a new psychological law, certify a political ideology, or prove that any historical thinker was right about society.

The mathematics currently used is elementary and familiar. Formalizing parts of social science in proof assistants also has substantial precedent. The useful contribution here is an inspectable connection between research questions, model assumptions, proofs, evidence, and limitations. Whether a later extension makes an original research contribution requires comparison with prior work and independent review.

The initial paper, report, evidence tables, and Lean source are publicly readable on main in [Formalizing Soft Sciences](https://github.com/Sodelin/Formalizing-Soft-Sciences). The larger earlier mathematics and psychology corpus requested by Nolan has not yet been recovered. Its import remains a separate, unfinished requirement. Nothing in this guide should be mistaken for an inventory or replacement of that older work.

## 1 What kind of mathematics this is

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

## 2 What a checked proof buys us

There are three different jobs. First, interpretation translates an informal question into variables and definitions. Second, deduction establishes consequences of those definitions and assumptions. Third, empirical research tests whether the chosen representation helps explain or predict observations. Lean primarily assists the second job, while making choices made in the first easier to inspect.

For example, “people can coordinate beyond their immediate friends” might mean that messages can travel through a network, that people trust strangers, or that they willingly contribute resources. Those are different propositions. A graph proof about paths cannot silently become evidence about trust or cooperation.

Lean checks proof terms against formal statements. Its official documentation explains this checking process and its trusted components [N05]. A successful check can still accompany an inappropriate definition, an implausible social assumption, or a theorem that answers the wrong question. Reading the statement and connecting its variables to observations remains essential.

This is especially useful when informal arguments skip a step. The project constructs a connected network with no trust at all. That demonstrates that connectivity alone does not logically entail trust in this formal vocabulary. It does not demonstrate that human networks typically lack trust. A counterexample to a claimed logical implication and an estimate of how often something happens serve different purposes.

## 3 The complete current theorem inventory

All names below occur in `Solidarity.lean`. The build uses Lean 4.19.0 and its bundled standard library. These are the actual 16 declarations, including supporting lemmas; they are not 16 independent empirical discoveries.

### Paths and direct contacts

**1 adj_symm.** If one number is adjacent to another in our path, the reverse adjacency also holds. Adjacency means the numbers differ by one. This checks that the example graph is undirected; it does not assume that real friendships or obligations are always reciprocal.

**2 reach_trans.** A path from A to B and a path from B to C can be combined into a path from A to C. This is the mathematical basis for reaching someone through intermediaries. It says nothing about whether a message arrives accurately or whether a recipient acts on it.

**3 reach_symm.** A path can be traversed in reverse in this graph. The result depends on its symmetric edges. A hierarchy with one-way communication would require a different model.

**4 zero_reaches.** Starting at person 0, every natural-number label can be reached by a finite sequence of neighboring labels. Induction supplies the proof: first reach 0, then extend a path one step at a time.

**5 path_connected.** Every pair of vertices is connected by a finite path. Each individual journey is finite even though the mathematical population has no final vertex. This is not a claim that an actual population is infinite.

**6 at_most_two_neighbors.** Every neighbor of a vertex must be one of its two adjacent numerical labels. At the endpoint 0, there is only one actual neighbor. The theorem gives containment in a set of at most two candidates; it does not estimate anyone's friendship capacity.

**7 unbounded_reachable.** For every proposed numerical bound, some vertex beyond that bound remains reachable from 0. Together with the neighbor result, this separates small local degree from unlimited indirect reach in the example. It gives neither a time bound nor a bound on communication loss.

This path is a simple counterexample to the assertion that a bound on each person's direct contacts must also bound the size of every connected society. It does not refute hypotheses about the cognitive effort needed to maintain emotionally meaningful relationships. The separate literature review considers the uncertainty around a universal fixed “Dunbar number” [S01].

### Membership and trust

**8 membership_nesting.** If every member of A belongs to B, and every member of B belongs to C, then every member of A belongs to C. This is transitivity of inclusion. It checks the inference after both inclusion assumptions have been supplied; it does not discover those assumptions from geographic names.

**9 overlapping_memberships.** Two groups can share a member while each also has a member absent from the other, and both can lie within one larger population. The concrete example uses A containing 0 and 1, and B containing 0 and 2. This shows that overlapping membership is logically coherent. It does not establish whether people recognize, value, or tolerate that overlap.

**10 connected_without_trust.** There is a connected network for which the independently defined trust relation is false everywhere. Reachability therefore does not force trust. Since trust has no behavioral connection to the graph in this construction, the result cannot measure a real connectivity–trust relationship.

### Incentives and cooperation

**11 cooperation_stable_iff.** In the specified donation game, mutual contribution resists a unilateral payoff-improving deviation exactly when the sanction for defection is at least the contribution cost. Equality gives indifference, so this is weak stability rather than a strict preference to contribute. The next section works through the arithmetic.

**12 no_sanction_failure.** If contributing costs a positive amount and the sanction is zero, mutual contribution is not stable under that game's payoff rule. This does not show that unsanctioned human cooperation is impossible. Reciprocity, concern for others, norms, reputation, and repetition are absent from this payoff rule.

**13 heterogeneous_cooperation_exists.** Two players can have different labels and still satisfy the game's stability condition. The witness uses benefit 3, cost 1, and sanction 2. Labels are deliberately absent from the payoff function, so this is a possibility result inside the model, not evidence that identity never matters.

**14 homogeneous_cooperation_can_fail.** Players with the same label can fail the stability condition. The witness uses benefit 3, cost 1, and sanction 0. This shows that shared labels do not logically supply a missing incentive in a model that assigns no payoff effect to labels.

**15 symbols_alone_insufficient.** Giving both players the same marker also leaves an unstable example. This is the same limitation made explicit for a shared symbol. It does not test a theory in which symbols change expectations, preferences, or obligations. Such a theory needs those mechanisms represented.

**16 mutual_gain.** Mutual contribution gives each player a higher payoff than mutual defection if contribution cost is less than benefit plus sanction. This compares two outcomes; it does not by itself establish stability. It also omits the cost and distribution of institutional enforcement.

The label and symbol witnesses are deliberately modest. Their value is to expose the missing mechanism in a sweeping argument, not to settle an empirical debate by defining the debated variable out of the payoff function.

## 4 Reading the game without knowing Lean

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

## 5 What this contributes to psychology

**No theorem in the current file proves an empirical psychological effect.** There are no participant data, fitted parameters, probability distributions over choices, or tests of a psychological measurement model in that file. Its immediate psychological contribution is to separate concepts and check consequences of clearly stated hypothetical relationships.

Your original question proposes at least two mechanisms. A stranger might feel familiar because they resemble an important person in your life. Alternatively, a stranger might recognize shared symbols and thereby signal common expectations. A third possibility is that cooperation depends mainly on material incentives and the reliability of an institution. These mechanisms can interact, and they should not be represented by one variable called “homogeneity.”

The literature gives reasons to examine these distinctions. Relational-self theory discusses how representations of significant others can shape responses to new people [S05]. Cultural-marker research examines how markers can acquire social significance [S04]. Work on identity complexity distinguishes different representations of multiple memberships [S06, S28]. The project records access limitations for these sources; an abstract-level reading does not justify a full reconstruction of a published psychological model.

### What we would have to measure

| Construct | Possible observation | Main interpretation problem |
|---|---|---|
| Perceived personal familiarity | A rating of resemblance to a significant person | Resemblance may also change warmth or perceived status. |
| Symbol recognition | Recognition and interpretation of a shared sign | Recognizing a sign need not imply endorsement. |
| Expected cooperation | A forecast of the partner's contribution | Beliefs can differ from the person's own preferences. |
| Identity structure | Membership reports and judgments of overlap | Administrative categories can differ from felt identity. |
| Cooperation | A costly contribution or a completed joint task | One task may not generalize to other settings. |

These are proposed measurements, not variables already validated for this project. The empirical protocol in the repository separates manipulations and outcomes so that a future study can investigate them. The existing meta-analytic and experimental evidence in the report concerns particular populations and tasks; it cannot identify a universal mechanism by itself [S03–S06].

### What future psychology proofs could establish

A specified learning rule could support a theorem that its predictions remain within an allowed range. A decision model could support a theorem that increasing one incentive changes a predicted choice under explicit assumptions. A measurement model could support an identifiability result showing whether different latent explanations can produce exactly the same observable distribution. These are valuable mathematical targets. None is implemented in the present file, and none would establish that people actually follow that model without empirical evidence.

A useful extension would allow personal familiarity and symbol recognition to change beliefs about a partner, or allow identity to enter preferences explicitly. We could then compare models that otherwise produce similar behavior. If two mechanisms give the same predictions for all observations collected, that is a reason to redesign the study. A proof of indistinguishable predictions would reveal an evidential limitation rather than establish which mechanism is psychologically true.

For example, high contribution following a shared symbol might reflect trust, a felt obligation, fear of sanctions, or a desire to appear loyal. Observing only contribution cannot automatically separate those explanations. Future models need a clear account of which additional observation or intervention would distinguish them. That account should precede claims that an identity mechanism has been proved.

### Carrying forward the existing psychology corpus

The substantial earlier mathematics and psychology development belongs in this project with its provenance intact. Its location is unresolved in the accessible history and repositories. Screenshots may supply a conversation title, filename, theorem name, repository, or commit that makes recovery possible. A screenshot can be a locator; complete source files and their configuration are needed for a reproducible import.

The import process will preserve an unchanged snapshot, record its source and file hashes, reproduce its original build, and map each theorem to its informal meaning and assumptions. Only then should presentation or module organization change. The reader inventory will report original, imported, checked, and unresolved items separately. If a module requires a different Lean version, it can retain that environment until a migration has been independently checked.

This is not a reason to replace the older development with newly written examples. The current guide explains only the available 16 theorems. The older corpus's size, content, and check status remain unknown here, and the project must continue to label its import as pending.

## 6 How Durkheim could guide a formal model

Durkheim distinguishes solidarity associated with shared beliefs and sentiments from solidarity associated with differentiated, interdependent functions. In the excerpt examined, these are distinguishable aspects of social life, not simply a claim that everybody must become alike [S14]. That distinction directly motivates our research question about whether groups need similarity, compatible expectations, complementary roles, or some combination.

A responsible formalization would select a particular claim and identify its textual basis. It would state a proposed mathematical interpretation, explain what it leaves out, and distinguish that interpretation from Durkheim's wording. It would also examine alternative interpretations. Encoding a complete body of sociological thought as one proposition would hide too many choices.

Here is a concrete next model, **proposed rather than already proved**. A finite group must complete several tasks. Individuals have different capabilities; a task requires an appropriate capability. Define successful collective production using task coverage and a feasible assignment. Separately define whether each person prefers participating to an outside option. Add rules for sharing gains, enforcing commitments, and leaving the arrangement.

One proof target is a conditional existence result: when the required tasks can be assigned among complementary participants and each assigned participant receives enough to cover their cost, collective production can be feasible and individually acceptable. A second target is a counterexample: capability complementarity and aggregate surplus can coexist with one participant receiving too little to accept the arrangement. A third target asks what changes when a necessary role withdraws or an institution loses reliability.

These targets keep productive dependence, participation incentives, and fairness distinct. They do not identify occupational specialization with racial or ethnic difference. They also do not assume that dependence is voluntary or legitimate. They are proposed mathematical interpretations inspired by a question in classical sociology, not claims that Durkheim proved those exact statements.

For the cultural-sign question, a later model would need an explicit learning or coordination mechanism. Merely assigning two people the same symbol and then assuming trust would place the desired conclusion inside the premises. The research task is to explain and test the link between signs, interpretation, expectations, and behavior.

It is not necessary to formalize every classical author before doing ethnological research. A more productive route is to move repeatedly between selected texts, ethnographic or historical cases, precise models, and observations that challenge the models. Differences in local meaning, colonial histories, institutions, and power must inform variable definitions. Ethnic categories should not be treated as fixed biological essences or used as interchangeable substitutes for task roles.

## 7 What is established prior work and what might become novel

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

## 8 How the work reaches readers

**Available now:** the public GitHub main branch contains the research package, source evidence, and checked formal source. Friends can read the Markdown without installing Lean. PDFs provide a stable reading layout, and DOCX files support editing. The verification receipt identifies the exact checked source and build, rather than relying on a general claim that the repository is verified.

**Next public revision:** add this guide, keep the psychology recovery status visible, and maintain a brief change record. Invite corrections through the repository's normal discussion or issue mechanisms. A short shareable description is included in the publication folder. It is a draft for the project owner to use; no email or social-media message has been sent on the owner's behalf.

**A citable release:** after reviewing authorship, licensing, source rights, and the completeness of the imported corpus, choose a version and create an immutable release snapshot. Zenodo documents a GitHub-release archiving route that can assign a DOI [N06]. This integration has not been configured and no DOI has been issued for this project. Archival availability is different from peer review.

**A research submission:** obtain review from people competent in formal verification and the relevant social science. The formal review should check statements, assumptions, and reproducibility; the substantive review should check interpretation, evidence, and the model–world connection. A methods paper should clearly state its contribution beyond these elementary examples. A preprint venue should be selected for its actual subject scope and contribution. arXiv has subject, endorsement, and moderation requirements, so posting there cannot be promised [N07]. No journal submission or acceptance is claimed.

Dissemination should preserve a link from a claim to its evidence or theorem, the exact version containing it, and the limitations that govern its interpretation. A polished document must not quietly strengthen the claim made by the proof. When the evidence or formalization changes, both the plain-language explanation and the technical record must change together.

## 9 What has actually been verified

The first complete package on the requested repository was committed as `5eb4de33b6f03af1f689d710c239ededf2aaa708`. Its [GitHub Actions run](https://github.com/Sodelin/Formalizing-Soft-Sciences/actions/runs/36367099147) passed with Lean 4.19.0. The source contains no unfinished proof placeholders or custom social-science axioms. Eleven public results also have explicit axiom-dependency output; some rely on Lean's standard propositional extensionality and quotient soundness. The receipt records these dependencies.

The hosted local environment could not start the Lean executable successfully. The verified build occurred on the independent GitHub runner. This distinction matters for reproducibility and is retained in the record. Documentation-only changes do not create new formal results.

There are separate checks for source references, document structure, and output files. The documents are rendered and visually reviewed to catch broken tables, unreadable symbols, and layout problems. These checks establish that the supplied artifacts can be used as intended; they do not establish the empirical truth of their claims.

## 10 How to read the project critically

For every result, ask what its variables mean, which assumptions are supplied, what the theorem actually concludes, and what observations would support the interpretation. Check whether a mathematical possibility has been mistaken for a frequent outcome, whether a statistical association has been mistaken for a mechanism, and whether a value judgment has been presented as a proved fact.

The present research recommendation is conditional on equal rights, non-domination, and broadly shared material gains. Within those goals, the report favors investigating protected group voice, practical cooperation across groups, and accountable institutions. The full package has not been tested as one intervention. Lean does not select those values or certify that recommendation; it helps make narrower pieces of the reasoning inspectable.

The immediate next substantive tasks are to recover the earlier psychology source, obtain stronger access to decisive literature, and choose one mechanism for a richer model and empirical test. The proposed task-interdependence model provides a concrete route from the present examples toward classical sociology. It should earn its interpretation and usefulness through careful textual work, formal checking, and comparison with actual social life.

The guide's [references and access notes](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/main/projects/solidarity-at-scale/sources/formalization-prior-work.md) are also included at the end of the PDF and editable document. The [search record](https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/main/projects/solidarity-at-scale/sources/formalization-search-log.md) explains the limits of the novelty assessment.
