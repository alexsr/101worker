config = {
    'wantdiff': False,
    'wantsfiles': False,
    'threadsafe': True,
    'behavior': {
        'creates': [['dump', 'featuresPerContribution']],
        'uses': [['dump', 'wiki-links']]
    }

}


def run(context):
    pages = context.read_dump('wiki-links')

    if pages is not None and "wiki" in pages.keys():
        pages = pages["wiki"]
        if pages is not None and "pages" in pages.keys():
            pages = pages["pages"]
    else:
        pages = []


    features = []
    for item in pages:
        if "p" in item.keys() and item["p"] == "Feature":
           if "n" in item.keys():
                title = item["n"]
                features += [title]


    contributions = {}
    for item in pages:
        if "p" in item.keys() and item["p"] == "Contribution":
            if "n" in item.keys() and "internal_links" in item.keys():
                title = item["n"]
                contributions[title] = []
                for f in features:
                    contributions[title] += [f] if "Implements::Feature:"+f in item["internal_links"] else []
    context.write_dump('featuresPerContribution', contributions)


import unittest
from unittest.mock import Mock, patch

class FeaturesPerContribution(unittest.TestCase):

    def setUp(self):
      self.env=Mock()
      self.env.read_dump.return_value = {
          "wiki": {
              "pages":[
                  {
                      "p": "Feature",
                      "n": "Hierarchical company",
                  },
                  {
                      "p": "Feature",
                      "n": "Mapping"
                  },
                  {
                      "p": "Feature",
                      "n": "Parsing",
                  },
                  {
                      "p": "Feature",
                      "n": "Total",
                  },
                  {
                      "p": "Feature",
                      "n": "Cut",
                  },
                  {
                      "p": "Contribution",
                      "n": "javaJson",
                      "internal_links": [
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
              ],
          }
      }

    def test_pages(self):
        run(self.env)
        self.env.write_dump.assert_called_with('featuresPerContribution', {'javaJson': ['Hierarchical company', 'Mapping', 'Parsing', 'Total', 'Cut']})

    def test_empty(self):
        self.env.read_dump.return_value = {}
        run(self.env)
        self.env.write_dump.assert_called_with('featuresPerContribution', {})



def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(FeaturesPerContribution)
    unittest.TextTestRunner(verbosity=2).run(suite)
