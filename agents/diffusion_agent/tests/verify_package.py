"""Read-only structural and integrity checks for the Assignment 5 package. No model API.

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
CASES = ['primary', 'contrast_1', 'contrast_2', 'evidence_probe']
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
assert len({cases[c]['intended_application'] for c in CASES}) == 1 and len({cases[c]['adoption_posture'] for c in ['primary','contrast_1','contrast_2']}) == 3
ok('Application held constant; adoption posture varies across primary and contrasts')
diff = {k for k in cases['primary'] if cases['primary'][k] != cases['evidence_probe'][k]}
assert diff == {'additional_context'}, diff
ok('Evidence probe differs from primary only in additional_context')

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
L3 = {c: R2[c]['application_finding'].split(' Peer group and organization (L4):')[0] for c in CASES}
assert all(R2[c]['application_finding'].startswith('Application (L3, same for every organization') for c in CASES)
assert len(set(L3.values())) == 1
ok('Cycle 2: application-level (L3) paragraph identical across all four contexts')
assert all(R2[c]['organization_specific_finding'].startswith('Adopter posture: ') and ' | Timing implication: ' in R2[c]['organization_specific_finding'] for c in CASES)
timing = {c: R2[c]['organization_specific_finding'].split(' | Timing implication: ')[1].split('.')[0] for c in ['primary', 'contrast_1', 'contrast_2']}
assert len(set(timing.values())) == 3, timing
ok('Cycle 2: posture header present; timing implication differs across the three postures')
assert all(any(x.startswith('Weakest diffusion claim') for x in R2[c]['contrary_evidence_or_limitations']) for c in CASES)
ok('Cycle 2: weakest diffusion claim named in every output')
assert all('grade' in e['evidence_type'] for c in CASES for e in R2[c]['evidence'])
ok('Cycle 2: every evidence item carries an evidence grade')
p, q = R2['primary'], R2['evidence_probe']
assert q['application_finding'] == p['application_finding']
assert q['organization_specific_finding'].startswith(p['organization_specific_finding'])
assert q['recommendation_management_implication'].startswith(p['recommendation_management_implication'])
assert sum(x.startswith('Memo claim') for x in q['contrary_evidence_or_limitations']) == 5
ok('Cycle 2: evidence probe - all five memo claims graded; findings and recommendation unchanged from primary')
assert 'crossed the chasm' in results[(1, 'primary')]['general_et_finding'] and 'before the chasm' in R2['primary']['general_et_finding']
assert results[(1, 'evidence_probe')]['organization_specific_finding'].endswith('consistent with this assessment.')
ok('Cycle 1 preserved failures archived unpatched (chasm overclaim; probe accepted memo conclusion)')

print(f'\n{len(checks)} structural/integrity checks passed. They do not prove factual validity or real-world diffusion. '
      'See the qualitative reviews.')
