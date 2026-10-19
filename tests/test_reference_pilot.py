"""Check the experiment’s reference isolation and stop boundaries.

Ge’ez Lab / https://ethiopiancanon.com. MIT.
"""
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PILOT = Path(__file__).resolve().parents[1] / 'experiments/2026-10-16-reference-pilot'
spec = importlib.util.spec_from_file_location('reference_pilot', PILOT / 'run_pilot.py')
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)


class PilotBoundaries(unittest.TestCase):
    def test_recorded_translator_inputs_do_not_include_references(self):
        requests = list((PILOT / 'requests').glob('translate-*.json'))
        self.assertTrue(requests, 'Expected recorded pilot calls')
        dataset = json.loads((PILOT / 'dataset.json').read_text())
        for path in requests:
            request = json.loads(path.read_text())
            for passage in request['passages']:
                self.assertEqual(set(passage), {'id', 'geez'})
            serialized = json.dumps(request, ensure_ascii=False)
            for item in dataset:
                self.assertNotIn(item['reference_french'], serialized)
                self.assertNotIn(json.dumps(item['score_facts'], ensure_ascii=False), serialized)

    def test_input_freezes_still_match(self):
        for name in ['freeze.json', 'freeze-v2.json']:
            for source, expected in json.loads((PILOT / name).read_text()).items():
                self.assertEqual(hashlib.sha256((PILOT / source).read_bytes()).hexdigest(), expected)

    def test_cached_response_cannot_be_reused_with_a_different_request(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'runs').mkdir()
            (root / 'runs/test.json').write_text(json.dumps({'request_sha256': 'different', 'response': {}}))
            with patch.object(pilot, 'HERE', root), patch.object(pilot.subprocess, 'run', side_effect=AssertionError('No model call allowed')):
                with self.assertRaisesRegex(RuntimeError, 'Cached request differs'):
                    pilot.call('test', 'judge', {'request': 'changed'})

    def test_reserved_translation_requires_a_frozen_selection(self):
        with tempfile.TemporaryDirectory() as directory:
            def read(name):
                if name == 'control-v2-results.json':
                    return {'qualified': True}
                if name == 'candidates.json':
                    return {'baseline': 'Translate.'}
                raise AssertionError('Unexpected read before selection guard: ' + name)
            with patch.object(pilot, 'HERE', Path(directory)), patch.object(pilot, 'read', side_effect=read), patch.object(pilot, 'call', side_effect=AssertionError('No model call allowed')):
                with self.assertRaisesRegex(RuntimeError, 'Freeze candidate selection'):
                    pilot.translate('baseline', 'heldout')


if __name__ == '__main__':
    unittest.main()
