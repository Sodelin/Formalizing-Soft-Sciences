"""Exact finite checks; Python standard library only. Not a Lean proof."""
from fractions import Fraction as F
from itertools import product
import json

def optimal_sets(u):
    return [{a for a, v in enumerate(row) if v == max(row)} for row in u]

def fiber_criterion(u, obs):
    opts = optimal_sets(u)
    return all(set.intersection(*(opts[s] for s in range(len(u)) if obs[s] == z))
               for z in set(obs))

def policy_exists(u, obs):
    opts = optimal_sets(u)
    return any(all(policy[obs[s]] in opts[s] for s in range(len(u)))
               for policy in product(range(len(u[0])), repeat=max(obs)+1))

def bayes_value(u, obs):
    # Uniform prior; maximize joint utility separately in each fiber.
    return sum(max(sum(F(u[s][a], len(u)) for s in range(len(u)) if obs[s] == z)
                   for a in range(len(u[0]))) for z in set(obs))

def min_worst_regret(u, obs):
    return max(min(max(max(u[s])-u[s][a] for s in range(len(u)) if obs[s] == z)
                   for a in range(len(u[0]))) for z in set(obs))

def brute_regret(u, obs):
    return min(max(max(u[s])-u[s][policy[obs[s]]] for s in range(len(u)))
               for policy in product(range(len(u[0])), repeat=max(obs)+1))

def refines(fine, coarse):
    return all(fine[s] != fine[t] or coarse[s] == coarse[t]
               for s in range(len(fine)) for t in range(len(fine)))

def main():
    observations = list(product(range(3), repeat=3))
    criterion_checks = refinement_checks = regret_checks = 0
    for bits in product(range(2), repeat=6):
        u = [bits[2*s:2*s+2] for s in range(3)]
        for obs in observations:
            assert bool(fiber_criterion(u, obs)) == policy_exists(u, obs)
            criterion_checks += 1
            r = min_worst_regret(u, obs)
            assert r == brute_regret(u, obs)
            assert (r == 0) == bool(fiber_criterion(u, obs))
            regret_checks += 1
        for fine in observations:
            for coarse in observations:
                if refines(fine, coarse):
                    assert bayes_value(u, fine) >= bayes_value(u, coarse)
                    refinement_checks += 1

    states = list(product(range(2), repeat=2))
    xor_u = [[int(a == (x ^ y)) for a in range(2)] for x, y in states]
    xor_values = {
        "none": bayes_value(xor_u, [0]*4),
        "x": bayes_value(xor_u, [x for x,y in states]),
        "y": bayes_value(xor_u, [y for x,y in states]),
        "both": bayes_value(xor_u, list(range(4))),
    }
    assert xor_values == {"none": F(1,2), "x": F(1,2), "y": F(1,2), "both": F(1)}
    cost = F(1,10)
    xor_net = {k: v-cost*{"none":0,"x":1,"y":1,"both":2}[k]
               for k,v in xor_values.items()}
    assert xor_net["both"]-xor_net["none"] == F(3,10)

    states = list(product(range(2), repeat=3))
    u = [[int(a == q) for a in range(2)] for q,n1,n2 in states]
    nuisance_values = {
        "none": bayes_value(u, [0]*8),
        "nuisance_two_bits": bayes_value(u, [2*n1+n2 for q,n1,n2 in states]),
        "target_one_bit": bayes_value(u, [q for q,n1,n2 in states]),
    }
    assert nuisance_values == {"none":F(1,2), "nuisance_two_bits":F(1,2), "target_one_bit":F(1)}
    result = {
        "status": "all assertions passed",
        "decision_sufficiency_cases": criterion_checks,
        "deterministic_minimax_regret_cases": regret_checks,
        "free_refinement_cases": refinement_checks,
        "xor_accuracy": {k:str(v) for k,v in xor_values.items()},
        "xor_net_utility_at_cost_1_over_10": {k:str(v) for k,v in xor_net.items()},
        "nuisance_accuracy": {k:str(v) for k,v in nuisance_values.items()},
        "scope": "Exhaustive 3-state, 2-action binary-utility cases; uniform prior for refinement. General claims have handwritten proofs in REPORT.md."
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
