"""Preserve the 85-declaration publication audit against an immutable source snapshot.

Run with --check to compare the checked-in CSV/JSON with the reviewed annotations.
This checks inventory completeness and source identity, not theorem truth or novelty.
"""
from pathlib import Path
import csv
import hashlib
import io
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SNAPSHOT = '7835157627548823f03f29dd3987e55601807b55'
BASE = 'https://github.com/Sodelin/Formalizing-Soft-Sciences/blob/' + SNAPSHOT + '/'

# Each line was compared with the actual declaration and its proof on 29 September.
# Roles describe the contribution within this package, not mathematical novelty.
ANNOTATIONS = '''
adj_symm|support|Symmetry of the successor/predecessor relation; supplies the undirected graph convention.
reach_trans|support|Concatenation is proved by induction on the second path.
reach_symm|support|Path reversal follows from adjacency symmetry and concatenation.
zero_reaches|support|Induction reaches every natural number from zero.
path_connected|endpoint|The natural-number ray is connected; finite paths join every pair.
at_most_two_neighbors|endpoint|Every neighbor is one of a+1 or a-1; this is containment, not a separate degree-cardinality formalization.
unbounded_reachable|endpoint|For every bound, bound+1 supplies a reachable vertex beyond it; no communication-time or human-capacity bound follows.
membership_nesting|consequence|Transitivity of supplied set inclusions; geographic and psychological membership assumptions are not inferred.
overlapping_memberships|witness|Sets {0,1} and {0,2} exhibit shared and exclusive members inside a common population.
connected_without_trust|witness|The trust relation is independently chosen to be empty; the result identifies a missing logical premise.
cooperation_stable_iff|endpoint|The payoff comparison cancels the other player's benefit, leaving cost <= sanction; equality is weak stability.
no_sanction_failure|consequence|Positive cost and zero sanction violate that exact threshold in the specified one-shot payoff model.
heterogeneous_cooperation_exists|witness|Different labels coexist with StableCC 3 1 2 because labels do not enter this payoff function.
homogeneous_cooperation_can_fail|witness|Equal labels coexist with failure of StableCC 3 1 0; the model assigns labels no incentive mechanism.
symbols_alone_insufficient|witness|A constant marker and the same unstable game exhibit the same omitted-mechanism point; not an independent behavioral discovery.
mutual_gain|consequence|The mutual-contribution payoff exceeds mutual defection when cost < benefit+sanction; this comparison differs from unilateral stability.
equivalent_refl|support|Reflexivity of equality at every permitted probe.
equivalent_symm|support|Symmetry of equality at every permitted probe.
equivalent_trans|support|Transitivity of equality at every permitted probe.
restrict_design|support|Universal agreement restricts to an included set of probes.
more_probes_preserve_identification|consequence|An injective observation design remains identifying when probes are added.
postprocess_preserves_equivalence|support|A common deterministic function preserves equal outputs; this is the exact information-loss mechanism used later.
baseline_ambiguous|witness|The distinct integer pairs (1,0) and (0,1) have the same sum.
baseline_not_identified|endpoint|The sum observation is non-injective on the declared parameter space; witnessed by the preceding pair.
both_probes_identify|endpoint|The first-coordinate probe plus the sum determines both coordinates by subtraction.
common_intercept_preserves_order|consequence|Adding a common integer intercept preserves and reflects order.
common_intercept_preserves_difference|consequence|The common intercept cancels in subtraction.
shift_invariance|support|A latent shift compensated by the opposite intercept shift leaves one response unchanged.
population_shift_invariance|consequence|Function extensionality applies the same compensated shift at every person.
known_intercept_identifies|endpoint|Cancellation identifies a latent value when the intercept is specified and common.
anchor_identifies_intercept|endpoint|Cancellation identifies the intercept from a specified latent anchor.
group_intercepts_can_reverse_order|witness|A concrete bias difference reverses the underlying ordering; it is synthetic arithmetic.
bounded_bias_interval|endpoint|The assumed differential-bias interval translates into a latent-difference interval of the same radius.
difference_exceeding_bias_identifies_order|endpoint|Only an upper bound on differential bias is needed for this one-sided sign conclusion.
observational_equivalence|witness|Treatment-copy and background-copy models agree when treatment equals background.
intervention_disagreement|witness|Setting treatment true and background false distinguishes the two models.
treatment_effect_numerator|support|Enumeration gives effect numerator 2 for the treatment-copy model; the uniform-background average would be 1.
common_cause_numerator|support|Enumeration gives effect numerator 0 for the background-copy model.
no_universal_observational_estimator|endpoint|Every estimator of the given observational function fails on at least one candidate with the same observations and a different effect numerator.
all_responses_identify|endpoint|Agreement at all treatment/background pairs is equality of the complete deterministic outcome function.
fits_empty|support|Universal agreement on an empty evidence list is vacuous.
fits_cons_iff|support|Consistency with a new item splits into its label equation and consistency with the old list.
fits_append_iff|support|Consistency over concatenated lists is conjunction of their consistency constraints.
more_evidence_narrows_models|consequence|Every candidate consistent with the larger list is consistent with an included sublist.
truth_survives_correct_label|consequence|A truth function already fitting the old evidence survives its own correctly labeled observation.
distinguishing_query_eliminates_rival|endpoint|A query at which two hypotheses disagree removes the rival after the truth's label is recorded.
conflicting_labels_impossible|consequence|A deterministic function cannot assign two distinct labels to the same input.
incorrect_label_excludes_truth|consequence|One wrong exact label suffices to remove the truth function from the version space.
duplicate_evidence_same_models|consequence|Repeating identical constraints does not change exact consistency; this does not model repeated independent noisy measurements.
adding_members_preserves_feasibility|consequence|Task coverage is monotone when capabilities are fixed and task congestion is absent.
restricting_members_preserves_acceptance|consequence|Removing agents preserves the retained agents' inequalities with unchanged costs and rewards.
union_accepts_iff|support|Universal participation inequalities over a union split into the two groups.
indispensable_member_withdrawal|endpoint|If every capable group member for a task must be the removed agent, the retained group cannot cover that task.
complementary_pair_feasible|witness|Both Boolean specialists together cover the two matching roles.
no_specialist_alone_feasible|witness|One Boolean specialist cannot cover the other role.
aggregate_surplus_not_participation|witness|Total rewards 3 exceed total costs 2 while the agent rewarded zero refuses the stipulated inequality.
repaired_allocation_ready|witness|Rewards (1,2) restore both inequalities while preserving task coverage.
two_person_budget_iff|endpoint|An unrestricted integer transfer exists exactly when total budget covers the sum of costs; share=costA is a witness.
acceptable_share_interval|endpoint|The acceptable first-agent share lies between costA and budget-costB; no bargaining mechanism is supplied.
reversal_cells_valid|integrity|Positive denominators and success counts bounded by sample sizes license the rate interpretation.
first_stratum_advantage|support|Exact cross multiplication verifies 9/10 > 80/100.
second_stratum_advantage|support|Exact cross multiplication verifies 20/100 > 1/10.
pooled_reversal|support|Exact cross multiplication verifies 81/110 > 29/110 after pooling.
simpson_reversal|endpoint|Packages the three comparisons into one checked synthetic aggregation reversal.
equal_weight_addition_preserves_order|consequence|Addition of two integer inequalities; no unequal-rate or causal-adjustment assertion is hidden here.
aggregate_cannot_identify_components|reuse|Direct reuse of baseline_not_identified, not an additional independent non-identification discovery.
recoding_cannot_restore_components|reuse|Instantiates postprocess_preserves_equivalence with the already checked equal-sum pair.
approach_trajectory|support|The pinned transition columns generate start, stimulus, approach, interact over four time points.
avoidance_trajectory|support|The pinned avoidance transition columns generate start, stimulus, avoid, safetyCost.
avoidance_observational_equivalence|witness|Safe and dangerous states have identical complete four-modality observations along the declared avoidance trajectory.
avoidance_no_perfect_classifier|endpoint|The identical trajectory cannot be mapped to the correct danger Boolean for both states by any deterministic classifier.
approach_observations_differ|witness|Enumeration finds different observed trajectories under the two states when approach is fixed.
approach_identifies_state|endpoint|Among these two latent states, equality of the complete fixed approach observations forces equality of the states.
safe_columns_total_mass|integrity|Each reconstructed safe weight column sums to 10*u algebraically, for all integer u,c.
danger_columns_total_mass|integrity|Each reconstructed danger weight column sums to 10*u algebraically, for every integer u.
safe_columns_nonnegative|integrity|Positive u and 0 <= c <= 10*u make every component of the safe weights nonnegative.
danger_columns_nonnegative|integrity|Positive u makes every component of the fixed danger weights nonnegative.
implicit_mappings_equal_at_tenth|consequence|Putting c=u makes both symbolic implicit mappings identical at every phase; u>0 supplies the CABi=0.1 interpretation.
approach_implicit_equality_iff|endpoint|Equality of the approach weight columns holds iff c=u; the algebraic theorem has no positivity premise, while its normalized parameter interpretation needs u>0.
avoidance_implicit_columns_equal|consequence|Both avoidance-phase implicit columns ignore c and the safe/danger label in this fragment.
explicit_prior_weights|integrity|The two unnormalized prior weights are nonnegative and sum to scale under the specified bounds; normalization is an interpretation.
source_sensory_columns|integrity|All six phases match the four selected upstream spider/arousal matrices column by column.
source_affective_columns|integrity|All six phases match the selected upstream safe/danger affect matrices column by column.
source_transition_columns|integrity|Both reconstructed transition functions match all columns of the selected upstream transition matrices.
source_implicit_columns|integrity|Both symbolic weight functions match every selected upstream implicit column after the explicit scaling translation.
'''

GROUPS = {
 'Solidarity': ('Solidarity.lean', 'Project solidarity specification', 'Elementary graph, inclusion and payoff reasoning; original guide N01-N04 give broader formalization precedents.', 'Specified natural-number path, separate trust/labels, integer one-shot donation payoffs. No empirical behavioral conclusion.'),
 'Identifiability': ('SocialScience/Identifiability.lean', 'B01', 'F02 motivates model recovery; the equal-sum witness and cancellation are project examples of established identification reasoning.', 'Exact deterministic predictions and declared parameter/probe spaces; no noisy inference guarantee.'),
 'Measurement': ('SocialScience/Measurement.lean', 'B02', 'F03, scalar-invariance section: intercept equality is an established comparability issue. The repository uses an independently derived integer additive special case.', 'Unit-loading additive integer indicator, theorem-specific bias premises; no empirical bias bound or construct validation.'),
 'Causality': ('SocialScience/Causality.lean', 'B03', 'F04 sections 1-2 supplies a richer network non-identification predecessor; this deterministic binary example is not its resolution or full formalization.', 'Treatment equals binary background observationally; effects defined on the complete response function; no probability or general graphical calculus.'),
 'Learning': ('SocialScience/Learning.lean', 'B04', 'F08 Mitchell version-space reasoning. Related Lean version-space properties also occur in the current Cslib module linked in SOURCES.md.', 'Deterministic hypotheses, finite labeled lists and exact consistency; no noise model or statistical generalization bound.'),
 'CollectiveAction': ('SocialScience/CollectiveAction.lean', 'B05', 'Project capability/participation model; established set monotonicity and linear feasibility rather than an external open conjecture.', 'Fixed uncongested capabilities, integer transfers without sign constraints, zero outside options; no equilibrium or enforcement process.'),
 'Aggregation': ('SocialScience/Aggregation.lean', 'B06', 'F09 Simpson (1951), sections 8-11, is historical aggregation context. The strict numerical reversal here is a separately constructed example.', 'Synthetic positive-denominator counts; no empirical prevalence claim or universal causal adjustment rule.'),
 'PublishedCBT': ('clinical/ClinicalModels/PublishedCBT.lean', 'Source-derived fragment verification', 'Smith, Moutoussis and Bilek (2021), model section/Figure 2, Ineffective CAB interactions, Discussion; upstream CBT_model.m pinned at 82a0a3d.', 'Spider-present deterministic four-time-point fragment, fixed policy and two danger states; symbolic integer weights. Full inference/learning and clinical efficacy are outside the proof.'),
 'SourceBridge': ('clinical/ClinicalModels/SourceBridge.lean', 'Source transcription correspondence', 'Pinned upstream MATLAB tables extracted without execution, followed by Lean equality checks; source_bridge.py specifies ten matrices and six guards.', 'Bounded extraction and scaling bridge; no proof of MATLAB/SPM semantics, complete upstream simulation or model selection.'),
}

def git_bytes(path):
    return subprocess.check_output(['git', 'show', f'{SNAPSHOT}:{path}'], cwd=ROOT)

def generate():
    reviewed = {}
    for line in ANNOTATIONS.strip().splitlines():
        name, role, note = line.split('|', 2)
        assert name not in reviewed
        reviewed[name] = (role, note)
    old = {r['declaration']: r for r in csv.DictReader(io.StringIO(git_bytes('projects/foundations/theorem-inventory.csv').decode('utf-8')))}
    result = []
    for group, (file, question, prior, scope) in GROUPS.items():
        raw = git_bytes(file)
        source = raw.decode('utf-8')
        namespace = re.search(r'^namespace (\S+)', source, re.M)[1]
        for match in re.finditer(r'^theorem\s+(\w+)\b', source, re.M):
            name = match[1]
            role, note = reviewed.pop(name)
            full = namespace + '.' + name
            line = source.count('\n', 0, match.start()) + 1
            # All declarations in this fixed snapshot use := to delimit the proof.
            signature = source[match.start():source.index(':=', match.end())].strip()
            previous = old.get(full, {})
            result.append(dict(number=len(result)+1, declaration=full, family=group,
                role=role, meaning=previous.get('meaning', note), review_note=note,
                assumptions=previous.get('assumptions', scope), scope=scope,
                project_question=question, prior_relation=prior,
                external_open_problem_closure='not established',
                publication_route='formalization and source-verification dossier',
                source_commit=SNAPSHOT, source_file=file, line=line,
                source_sha256=hashlib.sha256(raw).hexdigest(),
                source_url=BASE+file+'#L'+str(line), formal_signature=signature))
    assert not reviewed, reviewed
    assert len(result) == len({r['declaration'] for r in result}) == 85
    assert {r['declaration'] for r in result if r['family'] in ('Identifiability','Measurement','Causality','Learning','CollectiveAction','Aggregation')} == set(old)
    counts={group:sum(r['family']==group for r in result) for group in GROUPS}
    assert list(counts.values()) == [16,9,9,6,9,10,8,14,4]
    data=dict(date='2026-09-29', source_snapshot=SNAPSHOT, declaration_count=85,
        group_counts=counts, review_type='AI-assisted source and statement audit; no independent human novelty certification',
        established_external_open_problem_closures=0, declarations=result)
    output={'theorem-audit.json':json.dumps(data,ensure_ascii=False,indent=2)+'\n'}
    buf=io.StringIO(newline='')
    writer=csv.DictWriter(buf,fieldnames=list(result[0]),lineterminator='\n');writer.writeheader();writer.writerows(result)
    output['theorem-audit.csv']=buf.getvalue()
    lines=['# Every declaration accounted for','',
        'Source snapshot: `'+SNAPSHOT+'`. All 85 declarations were compared with their formal statements and proofs. Roles below are within-package roles, not counts of discoveries. Exact signatures, assumptions, source hashes and immutable line links are in [JSON](theorem-audit.json) and [CSV](theorem-audit.csv). See [publication judgment](README.md) and [source comparisons](SOURCES.md).','']
    for group, (_,question,prior,scope) in GROUPS.items():
        lines+=['## '+group+' ('+str(counts[group])+')','', 'Question: '+question+'. '+scope,'', prior,'', '| # | Declaration | Role | Audited contribution |','|---|---|---|---|']
        for r in result:
            if r['family']==group:
                lines.append(f"| {r['number']} | [{r['declaration'].split('.')[-1]}]({r['source_url']}) | {r['role']} | {r['review_note']} |")
        lines.append('')
    output['THEOREM-BY-THEOREM.md']='\n'.join(lines)+'\n'
    return output

if __name__ == '__main__':
    expected=generate()
    if sys.argv[1:] == ['--check']:
        for name,text in expected.items():
            assert (OUT/name).read_text(encoding='utf-8') == text, name
        print('PASS: all 85 declarations accounted for; 16+51+18; source signatures, anchors and hashes pinned; no omitted or duplicate declarations.')
    elif not sys.argv[1:]:
        for name,text in expected.items(): (OUT/name).write_text(text,encoding='utf-8',newline='\n')
        print('Wrote complete 85-declaration audit.')
    else:
        raise SystemExit('Usage: python build_inventory.py [--check]')
