config = {
    'wantdiff': False,
    'wantsfiles': False,
    'threadsafe': True,
    'behavior': {
        'creates': [['dump', 'correlationLocFeatures']],
        'uses': [
            ['dump', 'featuresPerContribution'],
            ['dump', 'locPerLanguagePerContribution'],
            ['dump', 'programmingLanguagePerContribution']
        ]
    }
}

def run(context):
    features_per_contribution = context.read_dump('featuresPerContribution')
    loc_pl_pc = context.read_dump('locPerLanguagePerContribution')
    plang_per_contrib = context.read_dump('programmingLanguagePerContribution')

    if features_per_contribution is None:
        features_per_contribution = {}
    if loc_pl_pc is None:
        loc_pl_pc = {}
    if plang_per_contrib is None:
        plang_per_contrib = {}

    locs_per_language = {}
    features_per_language = {}
    for c, lang_locs in loc_pl_pc.items():
        for l in plang_per_contrib[c]:
            if l not in locs_per_language:
                locs_per_language[l] = 0
            locs_per_language[l] += lang_locs[l]
            if l not in features_per_language:
                features_per_language[l] = []
            features_per_language[l] = list(set(features_per_contribution[c]) | set(features_per_language[l]))

    correlation = {}
    for l in locs_per_language:
        correlation[l] = locs_per_language[l] / len(features_per_language[l])
    context.write_dump('correlationLocFeatures', correlation)

import unittest
from unittest.mock import Mock, patch

class CorrelationLocFeatures(unittest.TestCase):

    def setUp(self):
        self.env = Mock()

    def test_empty(self):
        def run_side_effect(*args, **kwargs):
            if args[0] == "featuresPerContribution":
                return {}
            if args[0] == "locPerLanguagePerContribution":
                return {}
            if args[0] == "programmingLanguagePerContribution":
                return {}
        self.env.read_dump.side_effect = run_side_effect
        run(self.env)
        self.env.write_dump.assert_called_with('correlationLocFeatures',{})


    def test_run(self):
        def run_side_effect(*args, **kwargs):
            if args[0] == "featuresPerContribution":
                return {
                        "haskellComposition": [
                            "Closed serialization",
                            "Cut",
                            "Hierarchical company",
                            "Total"
                        ]
                }
            if args[0] == "locPerLanguagePerContribution":
                return {
                        "haskellComposition": {
                            "Plain Text": 11,
                            "unkown": 41,
                            "Haskell": 147
                        }
                }
            if args[0] == "programmingLanguagePerContribution":
                return {
                        "haskellComposition": [
                            "Haskell"
                        ]
                }
        self.env.read_dump.side_effect = run_side_effect
        run(self.env)
        self.env.write_dump.assert_called_with('correlationLocFeatures', {"Haskell": 36.75})


def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(CorrelationLocFeatures)
    unittest.TextTestRunner(verbosity=2).run(suite)
