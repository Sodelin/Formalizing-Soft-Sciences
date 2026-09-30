# Decision-sufficient shadows and complementary research

## 0. Result

This packet develops one useful part of Nolan's generalizability hypothesis: a hidden system need not be reconstructed completely to support correct action. We prove an exact finite criterion, quantify loss when it fails, and demonstrate two failures of research allocation: maximizing irrelevant information and stopping before complementary steps pay off.

These are elementary decision-theoretic results applied to Nolan's proposed workflow, not claims of new mathematical discoveries or a solved generalization problem. The general statements have handwritten proofs. The executable checks are exact finite calculations, not Lean verification or a model-performance experiment.

## 1. Relationship to the existing theory

Builds on [NOLAN-THEORY-ANALYSIS.md](../NOLAN-THEORY-ANALYSIS.md), particularly omitted candidate targets and observation-preserving transfer. Nolan's central concern is upstream: an agent may optimize within a candidate set that omitted the consequential question. Decision sufficiency supplies a criterion for evaluating proposed distinctions **after a task and actions have been specified**. It does not solve candidate discovery.

## 2. Definitions

Let S be a finite nonempty set of possible states, A a finite nonempty set of actions, u(s,a) a real utility, and O:S→Z an observation or shadow. A deterministic observation-based policy chooses π(O(s)). A fiber F_z consists of states with the same observation. Write Opt(s)=argmax_a u(s,a).

Utility must represent the user's outcome, not merely local acceptance tests. The idealized available actions must be stated explicitly; tools, permissions, time and computational constraints can change what policies are feasible.

## 3. Exact decision-sufficiency theorem

An observation-based policy is optimal in every state if and only if every nonempty fiber satisfies

$$\bigcap_{s\in F_z}\operatorname{Opt}(s)\ne\varnothing.$$

Proof: the policy chooses the same action on a fiber. If pointwise optimal, that action is in every state's optimal-action set. Conversely, choose one action from each nonempty intersection; there are finitely many fibers. That policy is optimal everywhere.

Randomization does not rescue exact sufficiency: a distribution attaining each state's maximum must put all its probability on actions optimal in that state.

This is weaker than recovering the state or utility vector. For example, two indistinguishable states with utility vectors (2,0) and (7,1) both admit action 0. Their distinction need not be recovered for this task. For a different task, it may matter.

## 4. Quantitative loss when sufficiency fails

Define regret r(s,a)=max_b u(s,b)−u(s,a). The least worst-case regret of deterministic observation-based policies is

$$R^*(O)=\max_{z:F_z\ne\varnothing}\min_{a\in A}\max_{s\in F_z}r(s,a).$$

Proof: every policy's worst regret is at least each fiber's best attainable worst regret. Choosing a minimizing action independently in every fiber attains their maximum. Thus R*=0 exactly when Section 3 holds. Randomized policies require minimizing over action distributions instead and can reduce positive worst-case regret.

This gives a practical question: which unresolved distinction causes consequential regret, and which proposed observation removes it?

## 5. Refinement and limits of more information

For prior p, the optimal expected utility is

$$W(O)=\sum_{z:P(z)>0}P(z)\max_a\mathbb E[u(s,a)\mid O(s)=z].$$

If O=g∘O′, then W(O′)≥W(O): a policy using the finer shadow can reproduce any coarse policy by ignoring extra distinctions. This result assumes fixed actions/utilities, free observations and unrestricted optimization. It does not say that extra context improves a bounded-compute model, that gains exceed acquisition costs, or that improvement is strict.

## 6. Worked failure: irrelevant information

There are eight equiprobable states (q,n₁,n₂), each coordinate a fair bit. The task is to predict q; utility is 1 for a correct answer. Each proposed observation costs the same and the budget allows one.

| Observation | State entropy removed | Optimal accuracy |
|---|---:|---:|
| Nothing | 0 bits | 1/2 |
| Both nuisance bits n₁,n₂ | 2 bits | 1/2 |
| Target bit q | 1 bit | 1 |

Maximizing raw state information chooses the wrong observation for this task. Decision value chooses q. This is a counterexample to a universal information-volume rule, not a claim that entropy-based methods never work.

## 7. Worked failure: premature stopping

There are four equiprobable states (x,y). Predict x XOR y; correct prediction earns 1. Querying either bit costs 1/10.

| Plan | Accuracy | Net expected utility |
|---|---:|---:|
| Stop | 1/2 | 1/2 |
| Query x only | 1/2 | 2/5 |
| Query y only | 1/2 | 2/5 |
| Query both | 1 | 4/5 |

Both initial one-step queries have negative immediate net value, yet their two-step package improves net value by 3/10. Therefore nonpositive immediate gain is insufficient evidence for stopping. The example does not justify unbounded persistence: evaluate affordable bundles or contingent plans when dependencies suggest complementarity.

## 8. What the executable checks establish

Run `python finite_demo.py`. Python's Fraction class keeps Bayesian calculations exact. Recorded output is [results.json](results.json).

- 1,728 combinations of three-state observations and binary two-action utility tables: fiber criterion agrees with independent policy enumeration.
- 1,728 combinations: regret formula agrees with policy enumeration and zero regret agrees with exact sufficiency.
- 21,312 refining observation pairs with those utilities: free-refinement inequality holds under a uniform prior.
- XOR and nuisance examples reproduce the fractions above.

The exhaustive bounds are deliberately small. General validity comes from Sections 3–5's proofs, not extrapolating finite tests. No empirical savings, model competence comparisons or Lean compilation are reported.

## 9. Operational consequence

Keep three different choices visible: what outcome to pursue, which action candidates to generate, and what evidence/computation to acquire. Optimizing the third cannot compensate for omitting the decisive action or target in the second.

For a concrete problem, propose a consequential alternative and name what would distinguish it. Evaluate its effect on the eventual outcome, its cost and any necessary multi-step dependencies. A researcher may reasonably propose a two-step investigation with a weak first step. The executor should challenge its predicted joint value rather than dismiss it solely on immediate gain.

This is a decision rule under a specified model, not an automatic oracle. In real research the state space, probabilities, utilities and available investigations are partly unknown. Estimating their value can itself consume substantial compute.

## 10. Chat-researcher participation

Accept contributions in plain Markdown: proposed outcome/alternative, reasoning, distinguishing observation, predicted result and requested execution. These are useful fields, not a mandatory admission checklist. Partial insights and counterexamples remain admissible.

Record the intellectual contributor separately from the executor and verifier. Tool access determines who can perform an operation, not whose proposal is scientifically admissible. Readers must see the hypothesis, evidence, uncertainty and next unresolved question without opening a terminal.

With identical admissible policies, observations and utilities, optimal attainable value is independent of a researcher label. That mathematical fact does not prove equal real-world compute, memory, intelligence or permissions. Equal participation must be implemented through access and attribution.

## 11. Limitations

This packet addresses task-relevant observation and effort allocation. It does not prove hidden topology recoverable, universal generalization, discovery completeness, optimal LLM reasoning effort, or the original framework's novelty. Re-encoding a shadow as a graph or matrix cannot recover distinctions it has discarded. Shared observations can support shared decisions without uniquely identifying the underlying system.

## 12. Next discriminating experiment

Use previously unseen real tasks with adjudicable outcomes and equal total budgets. Compare (a) ordinary solving, (b) correctness auditing, (c) intervention that generates a consequential alternative and checks complementary investigations. Count all coordinator, researcher, executor and repair tokens, calls and time. Blindly assess useful outcome improvement, correctness and unresolved consequential omissions. Record model/effort explicitly where observable.

Predeclare the task sample, budget and success measure. Avoid tasks whose improved solutions are already in this repository. If the intervention generates more notes but no better outcomes, it has failed this test. Medium-versus-higher effort needs its own matched comparison; this packet does not establish their equivalence.

## 13. Prior work

- Sezener & Dayan (2020), [Static and Dynamic Values of Computation in MCTS](https://proceedings.mlr.press/v124/sezener20a.html): evaluates computation through its effect on eventual action quality, including future computations. Supports the framing; does not validate this workflow.
- Golovin & Krause, [Adaptive Submodularity](https://arxiv.org/abs/1003.3967), revised 2017: greedy guarantees require structural assumptions. The XOR example illustrates complementary gains outside a universal diminishing-returns premise.

The elementary finite proofs here are presented in full. No novelty claim is made for them. Nolan's motivating scope-discovery hypothesis remains distinct from these supporting constructions.

## 14. Handoff

This is an additive packet. It does not replace NEW-WAVE.md or NOLAN-THEORY-ANALYSIS.md. The next worker should first assess relevance to the user's actual research task, then select one concrete application or run Section 12's experiment. A future Lean port should mechanize Sections 3–4 only if it serves that application. Do not report Python checks as a Lean theorem or this packet as empirical validation.
