from django.test import TestCase

from holonet.rules.truth import Truth


class TruthTestCase(TestCase):

    def setUp(self):
        self.check = Truth()

    def test_check(self):
        self.assertTrue(self.check.check(None, None, None))
