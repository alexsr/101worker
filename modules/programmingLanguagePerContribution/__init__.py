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

# To Do: 1. Get list of all programming languages:
#             (loop through namespace language, select those who are "programming" languages)
#        2. Loop through contributions in wiki pages (see below) and search for "Uses::Language:<language>"
#        3. Write <contribution>: <language> in JSON as example below does it for Java

    languages = ["Java"]

    contributions = {}
    for x in languages:
        for item in pages:
            namespace = item["namespace"]
            if namespace == "Contribution":
                title = item["title"]
                usedLinks = item["used_links"]
                contributions[title] = [x if [True for i in usedLinks if "Uses::Language:"+x in usedLinks] else None]
    print(contributions)
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
