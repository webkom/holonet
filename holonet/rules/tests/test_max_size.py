from unittest.mock import Mock

from django.test import TestCase

from holonet.rules.max_size import MaxSizeRule


class MaxSizeTestCase(TestCase):

    def setUp(self):
        self.rule = MaxSizeRule()

    def test_check(self):
        message = Mock()
        message_list = Mock()
        message_list.max_message_size = 0

        self.assertFalse(self.rule.check(message_list, message, {}))

        message_list.max_message_size = 10
        self.assertRaises(AssertionError, self.rule.check, message_list, None, {})

        message.original_size = 512
        self.assertFalse(self.rule.check(message_list, message, {}))

        message.original_size = 51200000
        self.assertTrue(self.rule.check(message_list, message, {}))
