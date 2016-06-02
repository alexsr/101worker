config = {
    'wantdiff': False,
    'wantsfiles': False,
    'threadsafe': True
}

def run(context):
    locPerContribution = context.read_dump('locPerContribution')
    pages = context.read_dump('pages')

    if locPerContribution is None:
        locPerContribution = {}

    if pages is not None and "pages" in pages.keys():
        pages = pages["pages"]
    else:
        pages = []

    contributions = {}
    for item in pages:
        if "namespace" in item.keys():
            if item["namespace"] == "Contribution" and "title" in item.keys() and "used_links" in item.keys():
                contributions[item["title"]] = item["used_links"]

    correlation = {}
    env.write_dump('correlationLocFeatures', correlation)


import unittest
from unittest.mock import Mock, patch

class CorrelationLocFeatures(unittest.TestCase):

    def setUp(self):
        self.env = Mock()
        pass

    def test_run(self):
        pass

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(CorrelationLocFeatures)
    unittest.TextTestRunner(verbosity=2).run(suite)
