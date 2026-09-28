# What the Lean development establishes

The checked file is `../../../Solidarity.lean`, using Lean 4.19.0 and its standard library. No Mathlib dependency is needed for these elementary constructions. These are pedagogical models and counterexamples, not claims of mathematical novelty.

| Informal question | Definition or result | Interpretation boundary |
|---|---|---|
| Does a limit on direct contacts bound the whole population? | `Adj a b` on naturals joins consecutive numbers; `Reach` is finite-path reachability; `path_connected`, `at_most_two_neighbors`, `unbounded_reachable` | Neighbors lie in a set of at most two candidates. Reachability ignores time, bandwidth, trust, and organizational viability. |
| Can identities nest or overlap? | `Included`, `membership_nesting`, `overlapping_memberships` | Membership is a predicate; the model does not explain why people identify or how strongly. |
| Does connectedness imply trust? | `connected_without_trust` | A witness sets trust false everywhere while preserving reachability. This is a logical non-implication. |
| What makes mutual contribution stable in a specified game? | `payoff`, `StableCC`, `cooperation_stable_iff` | A symmetric two-player donation game with certain, externally funded sanctions. |
| Is homogeneous labeling sufficient or necessary in that game? | `heterogeneous_cooperation_exists`, `homogeneous_cooperation_can_fail`, `symbols_alone_insufficient` | Labels have no payoff effect by construction; results show possibility, not real-world prevalence. |
| When do both players prefer mutual contribution to mutual defection? | `mutual_gain` | Compares the two profiles only; does not establish fairness, global optimality, or legitimacy. |

For integers b, c, s, row payoff is the benefit b if the other contributes, minus cost c if the row player contributes, otherwise minus sanction s. A contribution is Boolean true. The mutual-contribution payoff is b − c; deviating yields b − s. Thus weak resistance to unilateral deviation is equivalent to c ≤ s. At equality the actor is indifferent. The definition checks one player's deviations; symmetry gives the same condition for the other. Parameters are unrestricted integers in the general theorem; the concrete economic examples use positive benefits and costs and nonnegative sanctions.

The cooperative witness has benefit 3, cost 1, sanction 2, with different Boolean labels for the two actors. The failed-cooperation witness has benefit 3, cost 1, sanction 0, with constant labels. Changing label assignments changes no payoff. This explicit assumption is why the construction must never be advertised as proving that ethnicity is empirically irrelevant.

Sanctions are certain and have no financing, information, administration, corruption, or legitimacy cost. To study a real institution, extend the model with enforcement probability and cost, monitoring, unequal treatment, exit, and repeated interaction. Then connect parameters to observations. A theorem about chosen definitions cannot supply evidence that those definitions represent a society.

The graph proof avoids a cardinality library by proving that every neighbor is one of two candidates. It proves unbounded reachable naturals from zero, not that a finite person maintains infinitely many ties. Membership witnesses similarly show logical compatibility without asserting statistical or psychological frequency.

Prospective formal work: a finite family of graphs with degree bounded independently of size; a probabilistic enforcement threshold with explicitly stated expected-utility assumptions; and a representation model with resource constraints and contestability. Leave empirical hypotheses as hypotheses. Never add them as axioms and label their consequences evidence that the hypotheses are true.
