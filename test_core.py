import unittest, tempfile, json, sqlite3, copy
from pathlib import Path
import app as c

class CoreTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'test.sqlite'
        self.config = json.loads((Path(__file__).resolve().parent / 'scenario.json').read_text(encoding='utf-8'))

    def net(self):
        return c.PetriNet(self.config['transitions'], self.config['initial'], self.config['final'])

    def test_parallel(self):
        self.assertTrue(self.net().replay(['open', 'goods', 'invoice', 'pay'])['fit'])

    def test_missing(self):
        self.assertGreater(self.net().replay(['open', 'pay'])['missing_during_replay'], 0)

    def test_unknown(self):
        self.assertFalse(self.net().replay(['unknown'])['fit'])

    def test_incomplete(self):
        self.assertGreater(self.net().replay(['open'])['missing_final'], 0)

    def test_duplicate_cases(self):
        with self.assertRaises(ValueError):
            c.analyze(self.net(), self.config['cases'] * 2)

    def test_bad_arc(self):
        with self.assertRaises(ValueError):
            c.PetriNet({'a': {'consume': {'s': 0}, 'produce': {'e': 1}}}, {'s': 1}, {'e': 1})

    def test_negative_marking(self):
        with self.assertRaises(ValueError):
            c.PetriNet(self.config['transitions'], {'start': -1}, {'end': 1})

    def test_duplicate_activity(self):
        self.assertFalse(self.net().replay(['open', 'goods', 'goods', 'invoice', 'pay'])['fit'])
if __name__ == '__main__':
    unittest.main()
