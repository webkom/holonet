from django.test import TestCase

from holonet.core.utils import split_email


class UtilsTestCase(TestCase):

    def test_split_email_no_domain(self):
        self.assertEquals(split_email('holonet'), ('holonet', None))

    def test_split_email(self):
        self.assertEquals(split_email('test@holonet.com'), ('test', 'holonet.com'))
