"""Read-only structural and integrity checks for the Assignment 6 package. No model API.

Checks only what code can check: frozen core, contracts, archive hashes and the
invariance properties the specialist promises. It does not judge truth or quality;
see tests/cycle_1/review.md and tests/cycle_2/review.md for the qualitative review.
"""
from pathlib import Path
import hashlib, json, subprocess, sys


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
CASES = ['primary', 'contrast_1', 'contrast_2', 'qualification_probe']
VERSIONS = {1: '1.0', 2: '1.1'}
checks = []
def ok(label): checks.append(label); print('PASS:', label)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

r = subprocess.run([sys.executable, str(root / 'tools/check_frozen_core.py')], capture_output=True, text=True)
assert r.returncode == 0, r.stdout + r.stderr
ok(r.stdout.strip())

cases = {}
for c in CASES:
    cases[c] = json.loads((agent / f'cases/{c}.json').read_text()); in_v.validate(cases[c])
    ok('Common input schema: ' + c)
assert len({cases[c]['emerging_technology'] for c in CASES}) == 1
ok('Technology held constant across all four cases')
assert len({cases[c]['intended_application'] for c in ['primary','contrast_1','contrast_2']}) == 1 and len({cases[c]['adoption_posture'] for c in ['primary','contrast_1','contrast_2']}) == 3
ok('Application held constant; adoption posture varies across primary and contrasts')
diff = {k for k in cases['primary'] if cases['primary'][k] != cases['qualification_probe'][k]}
assert diff == {'additional_context', 'intended_application', 'capabilities_constraints'}, diff
ok('Qualification probe differs from primary only in the revised design, constraints and pressures')

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
        ok(f'Cycle {cyc} {c}: frozen validator, strict schema, version, input, instructions and hashes')
    assert len(set(generals)) == 1
    ok(f'Cycle {cyc}: general technology finding identical across all four contexts')

# Promised v1.1 properties
R2 = {c: results[(2, c)] for c in CASES}
CATS = ['ADOPT', 'BOUNDED EXPERIMENT', 'PROOF OF CONCEPT', 'CONTINUE MONITORING', 'DEFER', 'REJECT']
rec = {c: R2[c]['organization_specific_finding'].split(' | ')[0].replace('Recommendation: ', '') for c in CASES}
assert all(R2[c]['organization_specific_finding'].startswith('Recommendation: ') and ' | Decisive factor: ' in R2[c]['organization_specific_finding'] for c in CASES)
assert all(any(r.startswith(k) for k in CATS) for r in rec.values()), rec
ok('Cycle 2: every output states one permitted recommendation category and its decisive factor')
assert rec['primary'].startswith('PROOF OF CONCEPT') and rec['contrast_1'].startswith('BOUNDED EXPERIMENT') and rec['contrast_2'].startswith('CONTINUE MONITORING') and rec['qualification_probe'].startswith('DEFER')
assert not any(r.startswith('ADOPT') for r in rec.values())
ok('Cycle 2: posture changes the recommendation (PoC / experiment / monitor), qualification case defers, no adopt for a bleeding-edge class')
assert all(R2[c]['general_et_finding'].startswith('Course classification for this application class: BLEEDING EDGE') for c in CASES)
ok('Cycle 2: classification identical (bleeding edge) regardless of posture')
assert len({R2[c]['application_finding'] for c in ['primary', 'contrast_1', 'contrast_2']}) == 1
ok('Cycle 2: application finding identical across the three posture cases')
for c in CASES:
    t = ' '.join([R2[c]['general_et_finding'], R2[c]['application_finding'], R2[c]['organization_specific_finding']])
    assert '[General]' in t and '[Application-decisive]' in t and '[Organization-decisive]' in t
ok('Cycle 2: general vs application-decisive vs organization-decisive tags present in every output')
kinds = ['New evidence', 'Improved maturity', 'Lower cost', 'Regulatory clarification', 'Peer adoption', 'Internal capability']
assert all(all(any(t.startswith(k) for t in R2[c]['change_monitoring_triggers']) for k in kinds) for c in CASES)
ok('Cycle 2: all six memo trigger types present in every output')
assert all('Organizational Adoption specialist' in R2[c]['recommendation_management_implication'] for c in CASES)
ok('Cycle 2: handoff issue to the Organizational Adoption specialist named in every output')
assert all('grade' in e['evidence_type'] for c in CASES for e in R2[c]['evidence'])
ok('Cycle 2: every evidence item carries an evidence grade')
r1 = {c: results[(1, c)]['organization_specific_finding'] for c in CASES}
assert r1['contrast_1'].startswith('Recommendation: adopt') and r1['contrast_2'].startswith('Recommendation: reject') and r1['qualification_probe'].startswith('Recommendation: bounded experiment')
ok('Cycle 1 preserved failures archived unpatched (adopt bleeding edge; endorse ban; live pilot despite missing facts)')

print(f'\n{len(checks)} structural/integrity checks passed. They do not prove that a recommendation is right. '
      'See the qualitative reviews.')
