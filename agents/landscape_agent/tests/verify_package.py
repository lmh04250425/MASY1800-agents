"""Read-only structural and integrity checks for the Assignment 8 package. No model API.

Checks only what code can check: frozen core, contracts, archive hashes, case design and the properties
the v1.1 specialist promises:
- dated general finding identical for the same technology;
- application finding identical for the same application;
- ten dimensions with relevance tiers and no single score;
- relevance that moves with the application and the organization;
- typed, graded, dated evidence;
- trigger format;
- the stale claim;
- the hype probe.
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
REG = {r['id']: r for r in json.loads((agent / 'evidence/source_register.json').read_text())}
CASES = ['primary', 'contrast_1', 'contrast_2', 'hype_probe']
SAME_APP = ['primary', 'contrast_2', 'hype_probe']
VERSIONS = {1: '1.0', 2: '1.1'}
DIMS = ['Maturity & capability', 'Performance & cost trends', 'Competing technologies', 'Incumbent / conventional alternative', 'Complementary technologies',
        'Vendors & ecosystem', 'Standards & interoperability', 'Regulation', 'Investment & forecasts', 'Industry adoption']
TYPES = ('VENDOR', 'INDUSTRY', 'INDEPENDENT', 'STANDARD-REG', 'ORGANIZATION', 'INFERENCE')
checks = []
def ok(label): checks.append(label); print('PASS:', label)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
words = lambda s: set(re.findall(r'[a-z]+', s.lower()))
jac = lambda a, b: len(words(a) & words(b)) / len(words(a) | words(b))

r = subprocess.run([sys.executable, str(root / 'tools/check_frozen_core.py')], capture_output=True, text=True)
assert r.returncode == 0, r.stdout + r.stderr
ok(r.stdout.strip())

# ---------------- register and cases
for rid, rec in REG.items():
    assert rec['evidence_class'] in TYPES + ('UPSTREAM', 'FRAMEWORK') and rec['half_life'] in ('FAST', 'MEDIUM', 'SLOW') and rec['verified_on'] and rec['date'], rid
ok(f'Source register: {len(REG)} sources, each with an evidence class, refresh class, source date and verification date')

cases = {}
for c in CASES:
    cases[c] = json.loads((agent / f'cases/{c}.json').read_text()); in_v.validate(cases[c])
    ok('Common input schema: ' + c)
assert len({cases[c]['emerging_technology'] for c in CASES}) == 1
ok('Technology held constant across all four cases')
assert cases['contrast_1']['intended_application'] != cases['primary']['intended_application']
assert cases['contrast_2']['intended_application'] == cases['primary']['intended_application'] and cases['contrast_2']['organization'] != cases['primary']['organization']
d = {k for k in cases['primary'] if cases['primary'][k] != cases['hype_probe'][k]}
assert d == {'management_question', 'additional_context'}, d
ok('Contrast 1 changes the application; contrast 2 keeps the application and changes the organization; the hype probe changes only the question and the forwarded items')

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
    ok(f'Cycle {cyc}: general (broad landscape) finding identical across all four cases')

R2 = {c: results[(2, c)] for c in CASES}
org = {c: R2[c]['organization_specific_finding'] for c in CASES}

# ---------------- v1.1 promises
assert R2['primary']['general_et_finding'].startswith('As of 2026-11-15 [broad landscape')
assert len({R2[c]['application_finding'] for c in SAME_APP}) == 1 and R2['contrast_1']['application_finding'] != R2['primary']['application_finding']
assert all('Strongest competing or conventional alternative:' in R2[c]['application_finding'] for c in CASES)
alt = {c: R2[c]['application_finding'].split('Strongest competing or conventional alternative:')[1].split('.')[0] for c in CASES}
assert alt['primary'] != alt['contrast_1']
ok('Cycle 2: dated broad finding; identical application finding for the same application; a different application and strongest alternative for the coding contrast')

PAT = r'^(\d{1,2}) ([^:\n]+): .+ \| (DECISION-RELEVANT|WATCH|BACKGROUND) \| (.*)$'
tiers = {}
for c in CASES:
    m = re.findall(PAT, org[c], re.M)
    assert [int(x[0]) for x in m] == list(range(1, 11)) and [x[1] for x in m] == DIMS, (c, [x[:2] for x in m])
    tiers[c] = {int(n): t for n, _, t, _ in m}
    nd = sum(t == 'DECISION-RELEVANT' for t in tiers[c].values())
    assert 1 <= nd <= 4, (c, nd)
    assert 'Position summary (no single score):' in org[c]
ok('Cycle 2: all ten landscape dimensions present, each with a relevance tier; one to four DECISION-RELEVANT per case')

BANNED = [r'\b\d+(\.\d+)?\s*/\s*10\b', r'hype[- ]cycle position', r'peak of inflated', r'trough of disillusionment', r'landscape score', r'overall score']
for c in CASES:
    t = (org[c] + R2[c]['recommendation_management_implication']).lower()
    assert not any(re.search(b, t) for b in BANNED), c
ok('Cycle 2: no single score, composite index or hype-cycle placement anywhere in the findings or the recommendation')

reg_t = {c: tiers[c][8] for c in ['primary', 'contrast_1', 'contrast_2']}
assert reg_t == {'primary': 'WATCH', 'contrast_1': 'BACKGROUND', 'contrast_2': 'DECISION-RELEVANT'}, reg_t
mdr = {c: int(re.search(r'Most decision-relevant development \[(\d+) ', org[c]).group(1)) for c in CASES}
assert mdr['primary'] == 6 and mdr['contrast_1'] == 1 and mdr['contrast_2'] == 8 and mdr['hype_probe'] == mdr['primary'], mdr
assert all(tiers[c][mdr[c]] == 'DECISION-RELEVANT' for c in CASES)
assert tiers['hype_probe'] == tiers['primary']
ok('Cycle 2: relevance moves with context - regulation WATCH (SPS) / BACKGROUND (coding) / DECISION-RELEVANT (EU); the most decision-relevant development differs (6, 1, 8) and is itself DECISION-RELEVANT; the headlines leave SPS tiers unchanged')

nonvendor = {k for k, v in REG.items() if v['evidence_class'] in ('INDEPENDENT', 'STANDARD-REG', 'INDUSTRY', 'ORGANIZATION', 'UPSTREAM')}
for c in CASES:
    for n, name, t, ev in re.findall(PAT, org[c], re.M):
        if t == 'DECISION-RELEVANT':
            ids = set(re.findall(r'\b([CDE]\d{1,2})\b', ev))
            assert ids & nonvendor or 'INFERENCE' in ev or 'case facts' in ev, (c, n, ev)
ok('Cycle 2: diversity rule - every DECISION-RELEVANT line rests on at least one non-vendor source, case fact or labelled inference')

for c in CASES:
    for e in R2[c]['evidence']:
        assert re.match(r'^(VENDOR|INDUSTRY|INDEPENDENT|STANDARD-REG|ORGANIZATION|INFERENCE)\b.*; grade (A|B|C|n/a); refresh (FAST|MEDIUM|SLOW)$', e['evidence_type']), (c, e['evidence_type'])
        sid = re.match(r'\[([CDE]\d{1,2})\]', e['source_or_reference']).group(1)
        assert sid in REG and e['date_or_recency']
        cls = REG[sid]['evidence_class']
        assert e['evidence_type'].startswith(cls if cls not in ('UPSTREAM', 'FRAMEWORK') else 'INFERENCE'), (c, sid, cls, e['evidence_type'])
ok('Cycle 2: every evidence item is typed (vendor/industry/independent/standard-reg/organization/inference), graded, dated, given a refresh class and consistent with the register')

for c in CASES:
    cited = set(re.findall(r'\b([CDE]\d{1,2})\b', R2[c]['general_et_finding'] + R2[c]['application_finding'] + org[c] + R2[c]['recommendation_management_implication']))
    assert cited <= set(REG), (c, cited - set(REG))
ok('Cycle 2: every source cited in the findings exists in the dated register')

for c in CASES:
    T = R2[c]['change_monitoring_triggers']
    assert T[-1].startswith('REFRESH:') and len(T) >= 4
    case_text = (cases[c]['users_stakeholders'] + ' ' + cases[c]['capabilities_constraints']).lower()
    for t in T[:-1]:
        m = re.match(r'^TRIGGER \d \[(\d+) ([^\]]+)\]: Watch .+ \| Cadence .+ \| Threshold .+ \| Then .+ \| Watcher (.+)$', t)
        assert m and DIMS[int(m.group(1)) - 1] == m.group(2), (c, t[:60])
        assert m.group(3).lower() in case_text, (c, m.group(3))
ok('Cycle 2: every trigger names a dimension, what to watch, cadence, threshold, consequence and a watcher stated in the case; each case ends with a refresh schedule')

for c in CASES:
    assert 'Stale/hype-sensitive claim:' in org[c] and 'E11' in org[c] and '42.9%' in org[c] and 'D35' in org[c]
assert 'is therefore stale' in R2['primary']['general_et_finding']
ok('Cycle 2: the stale claim (E11, 30%) is named and refreshed (D35, 42.9%) in every output and in the general finding')

P = R2['hype_probe']
for i in range(1, 6): assert f'({i}) ' in P['organization_specific_finding']
assert P['recommendation_management_implication'].startswith('Position implication: do not skip the proof of concept')
assert 'Is SPS falling behind? Not on the evidence' in P['organization_specific_finding']
ok('Cycle 2: hype probe - all five forwarded items typed and graded; "falling behind" tested against a denominator; the proof of concept is kept')

assert R2['primary']['abstention_or_more_information_needed'][0].startswith('INFORMATION REQUEST: which platform runs Violet')
ok('Cycle 2: SPS information request asks for the platform fact the most decision-relevant development depends on')

o1 = [results[(1, c)]['organization_specific_finding'].split(':', 1)[1] for c in CASES]
o2 = [org[c] for c in CASES]
j1 = jac(o1[0], o1[1]); j2 = jac(o2[0], o2[1])
assert j1 > 0.8 and j2 < 0.5, (j1, j2)
ok(f'Sensitivity: organization-finding word overlap between SPS and the coding contrast fell from {j1:.2f} (v1.0, same market summary) to {j2:.2f} (v1.1)')

R1 = {c: results[(1, c)] for c in CASES}
assert all('6/10' in R1[c]['organization_specific_finding'] and 'Peak of Inflated Expectations' in R1[c]['organization_specific_finding'] for c in CASES)
assert '67 full-time work years' in R1['primary']['organization_specific_finding'] and '30% of realistic workplace' in R1['primary']['general_et_finding']
assert 'directly to a live bounded experiment' in R1['hype_probe']['recommendation_management_implication']
assert len({tuple(R1[c]['change_monitoring_triggers']) for c in CASES}) == 1
ok('Cycle 1 preserved failures archived unpatched (same market summary, score and hype-cycle label, vendor claim as finding, stale 30%, identical vague triggers, headlines moving the decision)')

print(f'\n{len(checks)} structural/integrity checks passed. They do not prove that a landscape judgment is right. See the qualitative reviews.')
