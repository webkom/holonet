from django.test import TestCase

from holonet.rules.no_subject import NoSubject


class NoSubjectTestCase(TestCase):

    def setUp(self):
        self.check = NoSubject()

    def test_check_empty_subject(self):
        self.assertTrue(self.check.check(None, {'subject': ''}, None))

    def test_check_not_exist(self):
        self.assertTrue(self.check.check(None, {}, None))

    def test_check_subject_exist(self):
        self.assertFalse(self.check.check(None, {'subject': 'Hello World'}, None))
