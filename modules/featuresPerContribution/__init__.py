config = {
    'wantdiff': False,
    'wantsfiles': False,
    'threadsafe': True,
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
    print(features)





import unittest
from unittest.mock import Mock, patch

class FeaturesPerContribution(unittest.TestCase):

    def setUp(self):
    	self.env=Mock()
    	self.env.read_dump.return_value={}




def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(FeaturesPerContribution)
    unittest.TextTestRunner(verbosity=2).run(suite)