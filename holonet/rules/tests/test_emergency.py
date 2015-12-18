from unittest import mock

from django.test import TestCase

from holonet.rules.emergency import Emergency


class EmergencyTestCase(TestCase):

    def setUp(self):
        self.rule = Emergency()

    def test_emergency(self):

        message_list = mock.Mock()
        message_list.emergency = False

        self.assertFalse(self.rule.check(message_list, None, None))

        message_list.emergency = True
        self.assertTrue(self.rule.check(message_list, None, None))
