import os.path
import subprocess
import threading
from copy import copy

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import sanitize_address


class EmailBackend(BaseEmailBackend):

    def __init__(self, fail_silently=False, sendmail_executable=None, sendmail_batch_length=None,
                 **kwargs):
        super(EmailBackend, self).__init__(fail_silently=fail_silently)
        self.sendmail_executable = sendmail_executable or settings.SENDMAIL_EXECUTABLE
        self.sendmail_batch_length = sendmail_batch_length or settings.SENDMAIL_BATCH_LENGTH
        self._lock = threading.RLock()

    def open(self):
        """
        Ensures we have access to sendmail.
        """
        try:
            sendmail_exist = os.path.isfile(self.sendmail_executable)
            if sendmail_exist:
                return True
            raise ValueError('Could not locate sendmail executable.')
        except IOError or ValueError:
            if not self.fail_silently:
                raise

    def close(self):
        pass

    def send_messages(self, email_messages):
        """
        Sends one or more EmailMessage objects and returns the number of email
        messages sent.
        """
        if not email_messages:
            return
        with self._lock:
            new_conn_created = self.open()
            num_sent = 0
            for message in email_messages:
                sent = self._send(message)
                if sent:
                    num_sent += 1
            if new_conn_created:
                self.close()
        return num_sent

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        if not email_message.recipients():
            return False
        from_email = sanitize_address(email_message.from_email, email_message.encoding)
        recipients = [sanitize_address(addr, email_message.encoding)
                      for addr in email_message.recipients()]
        message = email_message.message()

        sendmail_arguments = [self.sendmail_executable, '-G', '-i', '-f', from_email]
        for i in range(0, len(recipients), self.sendmail_batch_length):
            current_addresses = recipients[i:i+self.sendmail_batch_length]
            current_arguments = copy(sendmail_arguments)
            current_arguments.extend(current_addresses)

            result = self._sendmail(current_arguments, message)
            if not result:
                return False

        return True

    def _sendmail(self, args, msg):
        try:
            process = subprocess.Popen(args, stdin=subprocess.PIPE, close_fds=True)
            stream = msg.as_bytes(linesep='\r\n')
            process.stdin.write(stream)
            process.stdin.close()
        except OSError or IOError:
            if not self.fail_silently:
                raise
            return False
        return True
