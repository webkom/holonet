# -*- coding: utf8 -*-

import email
import os

from django.test import TestCase

from holonet.core.message import HolonetEmailMessage
from holonet.core.tasks import call_task, index_blacklisted_mail, send_blacklist_notification


class TaskTestCase(TestCase):
    def test_blacklist_functions(self):
        file_path = '%s/email_spam.txt' % os.path.dirname(__file__)
        email_file = open(file_path, 'r')
        raw_message = email.message_from_file(email_file)
        message = HolonetEmailMessage(raw_message, ['test@holonet.no'])

        call_task(index_blacklisted_mail, message)
        call_task(send_blacklist_notification, message)
