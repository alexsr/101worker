config = {
    'wantdiff': False,
    'wantsfiles': False,
    'threadsafe': True,
    'behavior': {
        'creates': [['dump', 'featuresPerContribution']],
        'uses': [['dump', 'pages']]
    }

}


def run(context):
    pages = context.read_dump('pages')

    if pages is not None and "pages" in pages.keys():
        pages = pages["pages"]
    else:
        pages = []


    features = []
    for item in pages:
        if "namespace" in item.keys() and item["namespace"] == "Feature":
           if "title" in item.keys() and "used_links" in item.keys():
                title = item["title"]
                features += [title]


    contributions = {}
    for item in pages:
        if "namespace" in item.keys() and item["namespace"] == "Contribution":
            if "title" in item.keys() and "used_links" in item.keys():
                title = item["title"]
                contributions[title] = []
                for f in features:
                    contributions[title] += [f] if "Implements::Feature:"+f in item["used_links"] else []
    context.write_dump('featuresPerContribution', contributions)


import unittest
from unittest.mock import Mock, patch

class FeaturesPerContribution(unittest.TestCase):

    def setUp(self):
    	self.env=Mock()
    	self.env.read_dump.return_value={
    	}

    def test_pages(self):
        run(self.env)
        self.env.write_dump.assert_called_with('featuresPerContribution', {'javaJson': ['Hierarchical company','Mapping','Parsing','Total','Cut']})

    def test_empty(self):
        self.env.read_dump.return_value = {}
        run(self.env)
        self.env.write_dump.assert_called_with('featuresPerContribution', {})



def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(FeaturesPerContribution)
    unittest.TextTestRunner(verbosity=2).run(suite)