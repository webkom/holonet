from django.test import TestCase

from holonet.members.models import Member
from holonet.members.utils import retrieve_member_by_email


class UtilsTestCase(TestCase):

    fixtures = ['members.yaml']

    def test_retrieve_member_by_email_non_member(self):
        self.assertIsNone(retrieve_member_by_email('non@member.com'))

    def test_retrieve_member_by_email_multiple_returns(self):
        self.assertIsNone(retrieve_member_by_email('equal@holonet.com'))

    def test_retrieve_member_by_email_success(self):
        user = Member.objects.get(pk=1)
        self.assertEquals(user, retrieve_member_by_email('holonet@holonet.com'))
