from datetime import datetime
from unittest import skip

from django.test import TestCase
from pytz import UTC

from holonet.storage.backends.elasticsearch import Backend
from holonet.storage.base import StoredEmail


class ElasticsearchStorageBackendTestCase(TestCase):

    def setUp(self):
        self.backend = Backend()
        self.backend.configure()

    @skip('No ES CI server.')
    def test_index_message(self):
        message = StoredEmail(
            blind_copy=['blind-copy@holonet.no', 'blind1-copy@holonet.no'],
            copy=['copy@holonet.no', 'copy1@holonet.no'],
            from_email='test@test.com',
            message_type='spam',
            raw='raw message content',
            recipients=['recipient@holonet.no', 'recipient1@holonet.no'],
            subject='test message',
            timestamp=datetime(2015, 6, 23, 1, 41, 28, tzinfo=UTC),
            to=['test@holonet.no', 'test1@holonet.no']
        )
        self.backend.index_message(message)
