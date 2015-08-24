from django.test import TestCase
from mock import Mock

from holonet.storage import backend


class BackendTestCase(TestCase):

    def test_index_message(self):
        backend.storage_backend.index_message = Mock()
        message_mock = Mock()
        message_mock.from_email = 'test@holonet.no'

        backend.index_message(message_mock)
        backend.storage_backend.index_message.assert_called_once_with(message_mock)

    def test_retrieve_history(self):
        backend.storage_backend.retrieve_history = Mock()

        backend.retrieve_history('from', 'to', ['filter'], 'query')
        backend.storage_backend.retrieve_history.assert_called_once_with(
            'from', 'to', ['filter'], 'query')
