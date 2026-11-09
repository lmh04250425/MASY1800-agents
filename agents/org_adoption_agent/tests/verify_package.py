"""Read-only structural and integrity checks for the Assignment 7 package. No model API.

Checks only what code can check: frozen core, contracts, archive hashes, case design and the
properties the v1.1 specialist promises (separation, step-relative verdicts, eight rated dimensions,
gap-traced actions, case-sourced owners, the information request, the weak-decision probe).
It does not judge truth or quality; see tests/cycle_1/review.md and tests/cycle_2/review.md.
"""
from pathlib import Path
import hashlib, json, re, subprocess, sys


class FrozenContractValidator:
    """Validates only the schema keywords used in the frozen course contracts."""
    def __init__(self, schema): self.schema = schema
    def validate(self, value): self._check(value, self.schema, '$')
    def _check(self, value, schema, where):
        kinds = {'object': dict, 'array': list, 'string': str}
        if 'type' in schema: assert isinstance(value, kinds[schema['type']]), where + ' type mismatch'
        if isinstance(value, dict):
            for key in schema.get('required', []): assert key in value, where + ' missing ' + key
            props = schema.get('properties', {})
            if schema.get('additionalProperties') is False: assert set(value) <= set(props), where + ' extra keys'
            for key, item in value.items():
                if key in props: self._check(item, props[key], where + '.' + key)
        if isinstance(value, list) and 'items' in schema:
            for i, item in enumerate(value): self._check(item, schema['items'], f'{where}[{i}]')


agent = Path(__file__).resolve().parents[1]
root = agent.parents[1]
out_v = FrozenContractValidator(json.loads((root / 'core/output_schema.json').read_text()))
in_v = FrozenContractValidator(json.loads((root / 'core/input_schema.json').read_text()))
CASES = ['primary', 'contrast_1', 'contrast_2', 'decision_probe']
ASSESSED = ['primary', 'contrast_1', 'contrast_2']
VERSIONS = {1: '1.0', 2: '1.1'}
checks = []
def ok(label): checks.append(label); print('PASS:', label)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
words = lambda s: set(re.findall(r'[a-z]+', s.lower()))
jac = lambda a, b: len(words(a) & words(b)) / len(words(a) | words(b))

r = subprocess.run([sys.executable, str(root / 'tools/check_frozen_core.py')], capture_output=True, text=True)
assert r.returncode == 0, r.stdout + r.stderr
ok(r.stdout.strip())

# ---------------- case design
cases = {}
for c in CASES:
    cases[c] = json.loads((agent / f'cases/{c}.json').read_text()); in_v.validate(cases[c])
    ok('Common input schema: ' + c)
assert len({cases[c]['emerging_technology'] for c in CASES}) == 1
ok('Technology held constant across all four cases')
VARY = {'organization', 'users_stakeholders', 'capabilities_constraints', 'management_question', 'additional_context'}
for c in ['contrast_1', 'contrast_2']:
    diff = {k for k in cases['primary'] if cases['primary'][k] != cases[c][k]}
    assert diff == VARY, (c, diff)
ok('Contrasts differ from primary only in organization, stakeholders, capabilities/constraints, question wording and context; application, posture, industry, need, risk and horizon held constant')
diff = {k for k in cases['contrast_1'] if cases['contrast_1'][k] != cases['decision_probe'][k]}
assert diff == {'intended_application', 'management_question', 'additional_context'}, diff
ok('Decision probe keeps the contrast-1 organization profile and changes only the application')

# ---------------- archives
results = {}
for cyc in (1, 2):
    folder = agent / f'tests/cycle_{cyc}'
    manifest = json.loads((folder / 'run_manifest.json').read_text())
    generals = []
    for c in CASES:
        resp = folder / f'{c}_response.json'; data = json.loads(resp.read_text())
        out_v.validate(data)
        assert data['agent']['version'] == VERSIONS[cyc]
        r = subprocess.run([sys.executable, str(root / 'tools/validate_response.py'), str(resp)], capture_output=True, text=True)
        assert r.returncode == 0, r.stdout + r.stderr
        item = next(x for x in manifest['cases'] if x['case'] == c)
        prompt = agent / f'tests/prompts/cycle_{cyc}/{c}.txt'
        assert sha(prompt) == item['prompt_sha256'] and sha(resp) == item['response_sha256'], 'hash mismatch'
        text = prompt.read_text()
        case_text = text.split('# CASE CONTEXT\n', 1)[1].split('# REQUIRED OUTPUT SCHEMA', 1)[0]
        assert json.loads(case_text) == cases[c], 'input changed across cycles'
        assert (folder / 'specialist_instructions.md').read_text() in text, 'prompt lacks archived instructions'
        generals.append(data['general_et_finding']); results[(cyc, c)] = data
        if cyc == 2: assert resp.read_bytes() == (agent / f'responses/{c}_response.json').read_bytes()
        ok(f'Cycle {cyc} {c}: frozen validator, strict schema, version, unchanged input, archived instructions and hashes')
    assert len(set(generals)) == 1
    ok(f'Cycle {cyc}: general technology finding identical across all four contexts')

R2 = {c: results[(2, c)] for c in CASES}
head = {c: R2[c]['organization_specific_finding'].split('\n', 1)[0] for c in CASES}

# ---------------- v1.1 promises
assert all(R2[c]['application_finding'].startswith('Fit screen: PASS.') for c in ASSESSED) and R2['decision_probe']['application_finding'].startswith('Fit screen: FAIL.')
assert len({R2[c]['application_finding'] for c in ASSESSED}) == 1
assert R2['primary']['general_et_finding'].startswith('[Technology maturity - carried from the Adoption specialist (C4)')
ok('Cycle 2: separation - maturity (general), fit (application, identical for the same application) and readiness (organization) are separate findings')

BANNED = ['too immature', 'not mature enough', 'offsets the technology', 'revisit when the technology matures', 'full implementation', 'implement the agent at scale']
for c in CASES:
    t = (R2[c]['organization_specific_finding'] + R2[c]['recommendation_management_implication']).lower()
    assert not any(b in t for b in BANNED), (c, [b for b in BANNED if b in t])
ok('Cycle 2: no readiness finding blames technology maturity, and none upgrades readiness into adoption')

PAT = r'^R([1-8]) [^:\n]+: (READY|PARTIAL|GAP|UNKNOWN) \| (BLOCKING|NOT BLOCKING)'
profiles = {}
for c in ASSESSED:
    m = re.findall(PAT, R2[c]['organization_specific_finding'], re.M)
    assert sorted(int(x[0]) for x in m) == list(range(1, 9)), (c, m)
    profiles[c] = {int(n): rating for n, rating, _ in m}
ok('Cycle 2: all eight readiness dimensions (R1-R8) rated with READY/PARTIAL/GAP/UNKNOWN and a blocking flag in every assessed output')

assert head['primary'].startswith('Readiness verdict (bounded experiment with live applicants): NOT YET READY | Earlier step (proof of concept, no applicants): READY WITH CONDITIONS')
assert head['contrast_1'].startswith('Readiness verdict (bounded experiment with live applicants): READY WITH CONDITIONS | Earlier step (proof of concept): READY |')
assert head['contrast_2'].startswith('Readiness verdict (bounded experiment with live applicants): NOT YET READY | Earlier step (proof of concept): NOT YET READY')
assert head['decision_probe'].startswith('Readiness verdict: NOT ASSESSED - fit screen failed')
ok('Cycle 2: step-relative verdicts change with capabilities (SPS not yet ready live / ready-with-conditions PoC; high-readiness ready with conditions; low-readiness not yet ready)')

mcg = {c: re.search(r'Most consequential gap: ((?:GAP|PARTIAL|UNKNOWN)-R\d)', head[c]).group(1) for c in ASSESSED}
assert mcg == {'primary': 'GAP-R8', 'contrast_1': 'PARTIAL-R4', 'contrast_2': 'GAP-R5'}, mcg
for c in ASSESSED:
    assert f'Why {mcg[c]} outranks the others:' in R2[c]['organization_specific_finding']
    n = int(mcg[c][-1]); assert profiles[c][n] == mcg[c].split('-')[0], (c, mcg[c], profiles[c][n])
ok('Cycle 2: exactly one most-consequential gap per assessed case, different across cases, consistent with the profile and justified')

def acts(c): return [l for l in R2[c]['recommendation_management_implication'].split('\n') if l.startswith('ACT-')]
for c in ASSESSED:
    A = acts(c); assert 1 <= len(A) <= 6, (c, len(A))
    for a in A:
        ids = re.findall(r'(GAP|PARTIAL|UNKNOWN|VERIFY)-R(\d)', a.split(']')[0])
        assert ids, (c, a[:60])
        for kind, n in ids:
            n = int(n)
            if kind == 'VERIFY':
                assert profiles[c][n] == 'READY' and f'VERIFY-R{n}' in R2[c]['organization_specific_finding'], (c, a[:60])
            else:
                assert profiles[c][n] == kind, (c, kind, n, profiles[c][n])
ok('Cycle 2: gap-trace - every action names a gap or assumption that exists in the same output profile (at most six actions)')

texts = [re.sub(r'^ACT-\d+ \[[^\]]*\] ', '', a).split(' Owner:')[0] for c in CASES for a in acts(c)]
assert len(texts) == len(set(texts))
assert not any(a.split(' Owner:')[0].endswith(('Secure executive sponsorship and a clear AI vision.', 'Establish an AI governance committee and policies.')) for c in CASES for a in acts(c))
ok('Cycle 2: no action text is reused across organizations, and the v1.0 generic actions are absent')

for c in CASES:
    case_text = (cases[c]['users_stakeholders'] + ' ' + cases[c]['capabilities_constraints']).lower()
    for owner in re.findall(r'Owner: (.*?)\. Done when', R2[c]['recommendation_management_implication']):
        if owner.startswith('owner to be named by '):
            parts = [owner[len('owner to be named by '):].split(' (')[0]]
        elif re.match(r'the operating owner named in ACT-\d', owner):
            continue
        else:
            assert '(stated role' in owner, (c, owner); parts = owner.split(' (')[0].split(' with ')
        for p in parts:
            p = p.lower().removeprefix('the ').strip()
            assert p in case_text, (c, p)
ok('Cycle 2: owner rule - every named owner is a role stated in the case, or explicitly to be named by a stated role')

P = R2['primary']
assert profiles['primary'][3] == 'UNKNOWN' and P['abstention_or_more_information_needed'][0].startswith('INFORMATION REQUEST (ask now; do not assume) - approval-queue capacity')
assert 'Decision rule when it arrives' in P['abstention_or_more_information_needed'][0]
assert 'can absorb' not in json.dumps(P).lower()
assert all(R2[c]['abstention_or_more_information_needed'][0].startswith('No blocking information') for c in ['contrast_1', 'contrast_2'])
ok('Cycle 2: unknown rule - SPS approval capacity stays UNKNOWN with an explicit request and decision rule; nothing invented; contrasts with supplied facts ask nothing')

assert 'WEAK TECHNOLOGY DECISION + READY ORGANIZATION' in head['decision_probe'] and all('SOUND DECISION' in head[c] for c in ASSESSED)
assert not re.search(r'closes (GAP|PARTIAL|UNKNOWN)-R', R2['decision_probe']['recommendation_management_implication'])
ok('Cycle 2: decision diagnosis - the probe is a weak technology decision in a ready organization, with no readiness program; the other three are sound decisions')

assert all('grade' in e['evidence_type'] for c in CASES for e in R2[c]['evidence'])
ok('Cycle 2: every evidence item carries an evidence grade')

v1_actions = lambda d: d['recommendation_management_implication'].split(' Recommended readiness actions: ')[1]
a1 = [v1_actions(results[(1, c)]) for c in CASES]
a2 = [' '.join(acts(c)) for c in CASES]
pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
j1 = min(jac(a1[i], a1[j]) for i, j in pairs); j2 = max(jac(a2[i], a2[j]) for i, j in pairs)
assert j1 == 1.0 and j2 < 0.5, (j1, j2)
ok(f'Sensitivity: action-list word overlap between organizations fell from {j1:.2f} (v1.0, identical checklist) to at most {j2:.2f} (v1.1)')

R1 = {c: results[(1, c)] for c in CASES}
assert len({v1_actions(R1[c]) for c in CASES}) == 1
assert 'too immature' in R1['contrast_2']['organization_specific_finding'] and 'offsets the technology' in R1['contrast_1']['organization_specific_finding']
assert 'can absorb approval' in R1['primary']['organization_specific_finding'] and R1['decision_probe']['organization_specific_finding'].startswith('Overall readiness: High - Ready')
ok('Cycle 1 preserved failures archived unpatched (identical generic actions; maturity confusion both ways; invented capacity; readiness masking a weak decision)')

print(f'\n{len(checks)} structural/integrity checks passed. They do not prove that a readiness judgment is right. '
      'See the qualitative reviews.')
