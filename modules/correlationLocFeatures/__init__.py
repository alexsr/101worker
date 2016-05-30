config = {
	'wantdiff': False,
	'wantsfiles': False,
	'threadsafe': True
}

def run(context):
  locPerContribution = context.read_dump('locPerContribution')
  pages = context.read_dump('pages')


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
