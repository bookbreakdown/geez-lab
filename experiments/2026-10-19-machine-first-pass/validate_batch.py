#!/usr/bin/env python3
"""Check frozen inputs and structural coverage, not language accuracy.
Ge’ez Lab / https://ethiopiancanon.com. MIT.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def check(data, source):
    expected = {s['side']: {line['line'] for line in s['lines']} for s in source['sides']}
    assert [s['side'] for s in data['sides']] == list(expected), 'Side order or identity differs'
    counts = {}
    for side in data['sides']:
        seen = set()
        for block in side['blocks']:
            assert block['english'].strip(), 'Empty English block'
            numbers = block['lines']
            assert numbers and all(type(n) is int for n in numbers), 'Invalid line numbers'
            assert set(numbers) <= expected[side['side']], 'Out-of-range source line'
            assert len(numbers) == len(set(numbers)), 'Repeated line within block'
            seen.update(numbers)
        assert seen == expected[side['side']], ('Unassigned source lines', side['side'], expected[side['side']] - seen)
        counts[side['side']] = len(seen)
    return counts


def main():
    for name, digest in json.loads((HERE / 'freeze.json').read_text()).items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, 'Frozen source changed: ' + name
    source = json.loads((HERE / 'source-lines.json').read_text())
    for label in ['translate-five-sides', 'review-format-recovery']:
        request = json.loads((HERE / 'requests' / (label + '.json')).read_text())
        saved = json.loads((HERE / 'runs' / (label + '.json')).read_text())
        digest = hashlib.sha256(json.dumps(request, ensure_ascii=False).encode()).hexdigest()
        assert saved['request_sha256'] == digest, 'Request hash mismatch'
        assert not saved.get('error'), 'Inference failed'
    failed = json.loads((HERE / 'runs/review-five-sides.json').read_text())
    assert failed.get('error'), 'Original review failure record missing'
    original_request = json.loads((HERE / 'requests/review-five-sides.json').read_text())
    assert failed['request_sha256'] == hashlib.sha256(json.dumps(original_request, ensure_ascii=False).encode()).hexdigest()
    raw = json.loads((HERE / 'runs/translate-five-sides.json').read_text())['response']
    final = json.loads((HERE / 'reviewed-draft.json').read_text())
    counts = check(raw, source)
    assert check(final, source) == counts
    changes = json.loads((HERE / 'revision-log.json').read_text())['changes']
    expected_final = json.loads(json.dumps(raw))
    for change in changes:
        side = next(s for s in expected_final['sides'] if s['side'] == change['side'])
        block = side['blocks'][change['block_index']]
        assert block['english'] == change['before'], 'Revision source does not match'
        block['english'] = change['after']
    for change in json.loads((HERE / 'revision-log.json').read_text()).get('metadata_changes', []):
        target = expected_final if change['side'] is None else next(s for s in expected_final['sides'] if s['side'] == change['side'])
        assert target.get(change['field']) == change['before'], 'Metadata revision mismatch'
        target[change['field']] = change['after']
    assert expected_final == final, 'Unlogged difference between raw and final draft'
    print('Frozen source and exact request hashes passed; raw and reviewed drafts assign', sum(counts.values()), 'source lines across five sides; all English changes are logged.')
    print('These checks do not establish clause completeness, accuracy, or expert approval.')


if __name__ == '__main__':
    main()
