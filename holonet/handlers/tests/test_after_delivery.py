import email

import mock
from django.test import TestCase
from django.utils.timezone import now

from holonet.core.tests.utils import read_message_fixture
from holonet.handlers.after_delivery import AfterDeliveryHandler
from holonet.lists.models import List

test_date = now()


class AfterDeliveryTestCase(TestCase):

    fixtures = ['list.yaml']

    @mock.patch('django.utils.timezone.now', return_value=test_date)
    def test_process(self, mock_now):
        message_list = List.objects.get(pk=1)
        message = email.message_from_string(read_message_fixture('simple_message.txt'))
        meta = {}

        self.assertIsNone(message_list.last_post_at)
        self.assertEqual(message_list.processed_messages, 0)

        AfterDeliveryHandler.process(message_list, message, meta)

        message_list.refresh_from_db()
        self.assertEqual(message_list.last_post_at, test_date)
        self.assertEqual(message_list.processed_messages, 1)
