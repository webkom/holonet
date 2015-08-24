from datetime import datetime

from django.test import TestCase
from pytz import UTC

from holonet.storage.backends.database import Backend
from holonet.storage.base import StoredEmail
from holonet.storage.models import EmailStorage


class DatabaseStorageBackendTestCase(TestCase):

    fixtures = ['stored_emails.yaml']

    def setUp(self):
        self.backend = Backend()
        self.backend.configure()

    def test_retrieve_with_time(self):
        emails = self.backend.retrieve_history(datetime(year=2015, month=1, day=1),
                                               datetime(year=2016, month=1, day=1))
        self.assertEqual(len(emails), 1)

    def test_retrieve_with_time_and_filter(self):
        emails = self.backend.retrieve_history(
            datetime(year=2015, month=1, day=1),
            datetime(year=2016, month=1, day=1),
            filter=['spam']
        )
        self.assertEqual(len(emails), 1)

        emails_none = self.backend.retrieve_history(
            datetime(year=2015, month=1, day=1),
            datetime(year=2016, month=1, day=1),
            filter=['blacklisted']
        )
        self.assertEqual(len(emails_none), 0)

    def test_retrieve_with_time_and_query(self):
        emails = self.backend.retrieve_history(
            datetime(year=2015, month=1, day=1),
            datetime(year=2016, month=1, day=1),
            filter=['spam'],
            search_query='This should make no change to the result'
        )
        self.assertEqual(len(emails), 1)

    def test_equal_instances(self):
        email = EmailStorage.objects.get(pk=1)
        message = StoredEmail(
            blind_copy=['blind-copy@holonet.no'],
            copy=['copy@holonet.no'],
            from_email='test@test.com',
            message_type='spam',
            raw='raw message content',
            recipients=['recipient@holonet.no'],
            subject='test message',
            timestamp=datetime(2015, 6, 23, 1, 41, 28, tzinfo=UTC),
            to=['test@holonet.no']
        )
        self.assertDictEqual(email.as_dict(), message.as_dict())

    def test_store_email(self):
        message = StoredEmail(
            blind_copy=['blind-copy@holonet.no'],
            copy=['copy@holonet.no'],
            from_email='test@test.com',
            message_type='spam',
            raw='raw message content',
            recipients=['recipient@holonet.no'],
            subject='test message',
            timestamp=datetime(2015, 6, 23, 1, 41, 28, tzinfo=UTC),
            to=['test@holonet.no']
        )
        self.backend.index_message(message)
        self.assertEqual(EmailStorage.objects.count(), 2)
