import mock
from django.test import TestCase

from holonet.handlers.acknowledge import Acknowledge


class AcknowledgeTestCase(TestCase):

    valid_user_mock = mock.Mock()
    valid_user_mock.member.acknowledge_posts = True

    @mock.patch('holonet.members.utils.retrieve_member_by_email', return_value=None)
    def test_no_member_found(self, mock_retrieve_member_by_email):
        message_mock = mock.Mock()
        message_mock.sender = 'non@member.com'

        self.assertIsNone(Acknowledge.process(None, message_mock,
                                              {'original_sender': 'non@member.com'}))
        mock_retrieve_member_by_email.assert_called_once_with('non@member.com')

    @mock.patch('holonet.members.utils.retrieve_member_by_email', return_value=None)
    def test_no_member_found_no_metadata(self, mock_retrieve_member_by_email):
        message_mock = mock.Mock()
        message_mock.sender = 'non@member.com'

        self.assertIsNone(Acknowledge.process(None, message_mock, {}))
        mock_retrieve_member_by_email.assert_called_once_with('non@member.com')

    @mock.patch('holonet.members.utils.retrieve_member_by_email', return_value=valid_user_mock)
    def test_valid_user(self, mock_retrieve_member_by_email):
        message_mock = mock.Mock()
        message_mock.sender = 'non@member.com'

        self.assertTrue(Acknowledge.process(None, message_mock, {}))
        mock_retrieve_member_by_email.assert_called_once_with('non@member.com')
