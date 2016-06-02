config = {
    'wantdiff': False,
    'wantsfiles': False,
    'threadsafe': True
}

def run(context):
    pages = context.read_dump('pages')

    if pages is None:
        pages = []
    else:
        pages = pages["pages"]

# What this does: 1. Get list of all programming languages:
#                     (loop through namespace language, select those who are "programming" languages)
#                 2. Loop through contributions in wiki pages (see below) and search for "Uses::Language:<language>"

    languages = []
    for item in pages:
        if item["namespace"] == "Language":
            title = item["title"]
            for x in item["used_links"]:
                if "programming language" in x:
                    languages += [title]
                    break;

    contributions = {}
    for item in pages:
        if item["namespace"] == "Contribution":
            title = item["title"]
            contributions[title] = []
            for l in languages:
                contributions[title] += [l] if "Uses::Language:"+l in item["used_links"] else []
    #print(contributions)
    context.write_dump('programmingLanguagePerContribution', contributions)


import unittest
from unittest.mock import Mock, patch

class programmingLanguagePerContribution(unittest.TestCase):

    def setUp(self):
        self.env = Mock()
        pass

    def test_run(self):
        pass

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(programmingLanguagePerContribution)
    unittest.TextTestRunner(verbosity=2).run(suite)
