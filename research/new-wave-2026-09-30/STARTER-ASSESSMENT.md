# CBT starter: HOLD, not an admitted proof task

30 September 2026. Source-review outcome: reject immediate extension of the existing deterministic Lean fragment as an open-problem contribution. Investigate the target and its current status first.

Primary source: Smith, Moutoussis and Bilek (2021), *Simulating the computational mechanisms of cognitive and behavioral psychotherapeutic interventions: insights from active inference*, DOI [10.1038/s41598-021-89047-0](https://doi.org/10.1038/s41598-021-89047-0), [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8115057/). Locator: Discussion, paragraph beginning “Yet another important topic not addressed is intolerance of uncertainty”; existing source ledger identifies Discussion XML Sec11, paragraph 12.

The authors describe a model extension needed to investigate uncertainty tolerance. Information seeking could hinder generalization by requiring confidence before approach, whereas acquiring information through partial approach could facilitate exposure. They call for explicit simulations. This is an author-stated extension task, not a verbatim mathematical conjecture.

Our operational question is: **When does information seeking sustain avoidance versus facilitate exposure through partial approach, and what follows for subsequent generalization?**

| Required mechanism | Existing fragment | Gap |
|---|---|---|
| Hidden-state inference | Boolean danger label | Probabilistic posterior and updating |
| Policy selection | Externally chosen approach/avoid transitions | Agent-selected policy and partial-approach action |
| Information and reward | Deterministic observation tuples | Stochastic observations and specified information-value coefficient |
| Exposure learning | No inference or therapeutic learning | Source-consistent likelihood/parameter learning |
| Generalization | No learned cross-context behavior | Explicit contexts and endpoint |

The present fragment proves outcomes conditional on selected behavior. It cannot answer the mechanism selecting and learning that behavior. Adding a generic action-value threshold would not by itself resolve the source task or demonstrate mathematical novelty.

The bounded subsequent-work search did not establish continuing openness. A relevant later perspective is *Using computational models of learning to advance cognitive behavioral therapy* (2025), DOI [10.1038/s44271-025-00251-4](https://doi.org/10.1038/s44271-025-00251-4). Its existence establishes neither closure nor openness of this exact extension. Do not advertise a newly solved open problem.

The next admissible investigation must return: (1) closest subsequent computational results and a dated status judgment; (2) a source-consistent extended equation set with modeling choices explicitly marked; (3) behavior and generalization endpoints; (4) one precise ambitious claim and its contribution beyond existing decision theory; and (5) a finite work budget.

A possible target form is a sharp necessary-and-sufficient characterization of avoidance versus informative partial exposure across a specified parameter family, followed by a generalization guarantee or counterexample. This is a proposed direction only: novelty, tractability and fidelity have not been established. No new proof or clinical conclusion is claimed in this packet.
