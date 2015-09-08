import email

from django.test import TestCase

from holonet.common.message import HolonetEmailMessage

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
