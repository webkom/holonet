from django.test import TestCase

from holonet.core.utils import split_address


class UtilsTestCase(TestCase):

    def test_split_email_no_domain(self):
        self.assertEquals(split_address('holonet'), ('holonet', None))

    def test_split_email(self):
        self.assertEquals(split_address('test@holonet.com'), ('test', 'holonet.com'))

    def test_verp_address(self):
        self.assertEquals(split_address('owner-listname+user=domain@origin.com'),
                          ('owner-listname+user=domain', 'origin.com'))
