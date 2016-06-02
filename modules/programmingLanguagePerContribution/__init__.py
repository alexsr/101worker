config = {
    'wantdiff': False,
    'wantsfiles': False,
    'threadsafe': True
}


def run(context):
    pages = context.read_dump('pages')

    if pages is not None and "pages" in pages.keys():
        pages = pages["pages"]
    else:
        pages = []

# What this does: 1. Get list of all programming languages:
#                     (loop through namespace language, select those who are "programming" languages)
#                 2. Loop through contributions in wiki pages (see below) and search for "Uses::Language:<language>"

    languages = []
    for item in pages:
        if "namespace" in item.keys() and item["namespace"] == "Language":
           if "title" in item.keys() and "used_links" in item.keys():
                title = item["title"]
                for x in item["used_links"]:
                    if "programming language" in x:
                        languages += [title]
                        break;

    contributions = {}
    for item in pages:
        if "namespace" in item.keys() and item["namespace"] == "Contribution":
            if "title" in item.keys() and "used_links" in item.keys():
                title = item["title"]
                contributions[title] = []
                for l in languages:
                    contributions[title] += [l] if "Uses::Language:"+l in item["used_links"] else []
    context.write_dump('programmingLanguagePerContribution', contributions)

import unittest
from unittest.mock import Mock, patch


class ProgrammingLanguagePerContribution(unittest.TestCase):

    def setUp(self):
        self.env = Mock()
        self.env.read_dump.return_value = {
            "pages": [
                {
                    "namespace": "Language",
                     "title": "Java",
                     "used_links": [
                         "OO programming language",
                         "Technology:Java platform",
                         "Technology:Java SE",
                         "InstanceOf::OO programming language"
                     ]
                 },
                {
                    "namespace": "Contribution",
                    "title": "javaJson",
                     "used_links": [
                         "Language:JSON",
                         "Language:Java",
                         "Technology:javax.json",
                         "API",
                         "Contribution:dom",
                         "Contribution:jdom",
                         "Language:JSON",
                         "Language:XML",
                         "Contribution:javaJsonHttp",
                         "Technology:Gradle",
                         "Technology:Eclipse",
                         "Implements::Feature:Hierarchical company",
                         "Implements::Feature:Mapping",
                         "Implements::Feature:Parsing",
                         "Implements::Feature:Total",
                         "Implements::Feature:Cut",
                         "MemberOf::Theme:Java mapping",
                         "Uses::Language:Java",
                         "Uses::Language:JSON",
                         "Uses::Technology:javax.json",
                         "Uses::Technology:JUnit",
                         "Uses::Technology:Gradle",
                         "DevelopedBy::Contributor:rlaemmel"
                     ]
                }
            ]
        }

    def test_pages(self):
        run(self.env)
        self.env.write_dump.assert_called_with('programmingLanguagePerContribution', {'javaJson': ['Java']})

    def test_empgy(self):
        self.env.read_dump.return_value = {}
        run(self.env)
        self.env.write_dump.assert_called_with('programmingLanguagePerContribution', {})

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(ProgrammingLanguagePerContribution)
    unittest.TextTestRunner(verbosity=2).run(suite)
