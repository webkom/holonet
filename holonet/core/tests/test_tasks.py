# -*- coding: utf8 -*-

import email
import os

from django.test import TestCase

from holonet.core.tasks import index_blacklisted_mail, send_blacklist_notification
from holonet.core.message import HolonetEmailMessage


class TaskTestCase(TestCase):
    def test_blacklist_functions(self):
        file_path = '%s/email_spam.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        raw_message = email.message_from_file(email_file)
        message = HolonetEmailMessage(raw_message, ['test@holonet.no'])

        index_blacklisted_mail.delay(message)
        send_blacklist_notification.delay(message)
