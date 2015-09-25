import email
from email.message import Message

from django.test import TestCase

from holonet.core.message import HolonetEmailMessage

from .utils import read_message_fixture


class EmailMessageTestCase(TestCase):

    def test_string_parse(self):
        message_name = 'spam_message.txt'
        message_string = read_message_fixture(message_name)
        msg = email.message_from_string(message_string)

        holonet_messsage = HolonetEmailMessage.parse_message(msg)

        self.assertListEqual(['holonet@abakus.no'], holonet_messsage.to)
        self.assertListEqual([], holonet_messsage.cc)
        self.assertListEqual([], holonet_messsage.bcc)
        self.assertListEqual([], holonet_messsage.reply_to)
        self.assertEqual('Tanya <erik49110@zviran.co.il>', holonet_messsage.from_email)

        self.assertIsNone(holonet_messsage.body)
        self.assertListEqual([], holonet_messsage.attachments)

    def test_message(self):
        message_name = 'spam_message.txt'
        message_string = read_message_fixture(message_name)
        msg = email.message_from_string(message_string)

        holonet_messsage = HolonetEmailMessage.parse_message(msg)
        holonet_messsage.to = ['holonet@holonet.com', 'holonet1@holonet.com']
        holonet_messsage.subject = ''

        del holonet_messsage.extra_headers['date']
        del holonet_messsage.extra_headers['message-id']
        holonet_messsage.extra_headers['to'] = 'ignore@holonet.com'
        holonet_messsage.body = 'ignore body'

        msg = holonet_messsage.message()
        self.assertTrue(isinstance(msg, Message))
        self.assertEqual(msg['to'], 'holonet@holonet.com, holonet1@holonet.com')
        self.assertEqual(msg['subject'], '*** No Subject ***')
        self.assertEqual(msg['reply-to'], '')

    def test_message_simple(self):
        holonet_message = HolonetEmailMessage(subject='test subject', body='message body',
                                              from_email='test@holonet.com',
                                              to=['holonet@holonet.com'])
        msg = holonet_message.message()
        self.assertEqual(msg['subject'], 'test subject')
        self.assertEqual(msg['from'], 'test@holonet.com')
        self.assertEqual(msg['to'], 'holonet@holonet.com')

    def test_set_header(self):
        message_name = 'spam_message.txt'
        message_string = read_message_fixture(message_name)
        msg = email.message_from_string(message_string)

        holonet_messsage = HolonetEmailMessage.parse_message(msg)
        holonet_messsage.set_header('x-test-header', 'test')

        msg = holonet_messsage.message()
        self.assertEqual(msg['x-test-header'], 'test')
