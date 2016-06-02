import os

config = {
    'wantdiff': False,
    'wantsfiles': True,
    'threadsafe': False,
    'behavior': {
        'creates': [['dump', 'locPerContributionPerLanguage']],
        'uses': [
            ['resource', 'loc'],
            ['resource', 'lang']
        ]
    }
}

def run(env, res):
    data = env.read_dump('locPerContributionPerLanguage')

    if data is None:
        data = {}

    f = res['file']
    if f.startswith('contributions' + os.sep):
        contribution = f.split(os.sep)[1]
        if data.get(contribution, None) is None:
            data[contribution] = {}
        language = env.get_derived_resource(f, 'lang')
        if data[contribution].get(language, None) is None:
            data[contribution][language] = 0
        data[contribution][language] += env.get_derived_resource(f, 'loc')

    env.write_dump('locPerContributionPerLanguage', data)

import unittest
from unittest.mock import Mock

class LocPerContributionPerLanguage(unittest.TestCase):

    def setUp(self):
        self.env = Mock()
        self.env.read_dump.return_value = { 'python': {"Python": 42} }

    def test_run_diff_lang(self):
        res = {
            'file': 'contributions' + os.sep + 'python' + os.sep + 'README.md'
        }
        def run_side_effect(*args, **kwargs):
            if args[1] == "lang":
                return "Plain Text"
            if args[1] == "loc":
                return 15
        self.env.get_derived_resource.side_effect = run_side_effect
        run(self.env, res)
        self.env.write_dump.assert_called_with('locPerContributionPerLanguage', {'python': {"Python": 42, "Plain Text": 15}})

    def test_run_same_lang(self):
      res = {
      'file': 'contributions' + os.sep + 'python' + os.sep + 'sample.py'
      }
      def run_side_effect(*args, **kwargs):
        if args[1] == "lang":
          return "Python"
          if args[1] == "loc":
            return 15
            self.env.get_derived_resource.side_effect = run_side_effect
            run(self.env, res)
            self.env.write_dump.assert_called_with('locPerContributionPerLanguage', {'python': {"Python": 57}})
    def test_new_contribution(self):
        res = {
            'file': 'contributions' + os.sep + 'ruby' + os.sep + 'sample.ruby'
        }
        def new_contribution_side_effect(*args, **kwargs):
            if args[1] == "lang":
                return "Ruby"
            if args[1] == "loc":
                return 15
        self.env.get_derived_resource.side_effect = new_contribution_side_effect
        run(self.env, res)
        self.env.write_dump.assert_called_with('locPerContributionPerLanguage', {'python': {"Python": 42}, 'ruby': {"Ruby": 15}})

    def test_run_no_contribution(self):
        res = {
            'file': 'something' + os.sep + 'ruby' + os.sep + 'sample.ruby'
        }
        run(self.env, res)
        self.env.write_dump.assert_called_with('locPerContributionPerLanguage', {'python': {"Python": 42}})


def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(LocPerContributionPerLanguage)
    unittest.TextTestRunner(verbosity=2).run(suite)
