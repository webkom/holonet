# -*- coding: utf8 -*-

import subprocess
from copy import copy

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import sanitize_address


class EmailBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        if not email_messages:
            return

        num_sent = 0
        for message in email_messages:
            sent = self._send(message)
            if sent:
                num_sent += 1
        return num_sent

    def _send(self, email_message):
        if not email_message.recipients():
            return False
        recipients = [sanitize_address(addr, email_message.encoding)
                      for addr in email_message.recipients()]
        message = email_message.message()

        try:
            common_arguments = \
                [
                    settings.SENDMAIL_EXECUTABLE,
                    '-G',
                    '-i',
                    '-f',
                    settings.SERVER_EMAIL
                ]
            for i in range(0, len(recipients), settings.SENDMAIL_BATCH_LENGTH):

                current_addresses = recipients[i:i+settings.SENDMAIL_BATCH_LENGTH]
                current_arguments = copy(common_arguments)
                current_arguments.extend(current_addresses)
                self._sendmail(current_arguments, message)

            return True
        except OSError:
            return False

    def _sendmail(self, args, msg):
        if not settings.TESTING:
            process = subprocess.Popen(args, stdin=subprocess.PIPE, close_fds=True)
            process.stdin.write(msg.as_bytes(linesep='\r\n'))
            process.stdin.close()
        else:
            from django.core import mail
            mail.outbox.append({'message': msg, 'args': args})
