import mock
from django.core.mail import EmailMessage
from django.test import TestCase

from holonet.backends.sendmail import EmailBackend

popen = mock.Mock()
popen.stdin = mock.Mock()
popen.stdin.write = mock.Mock()
popen.stdin.close = mock.Mock()


class SendmailTestCase(TestCase):

    @mock.patch('subprocess.Popen', return_value=popen)
    def test_sendmail(self, mock_popen):
        email = EmailMessage('Hello', 'Body goes here', 'from@example.com',
                             ['to@example.com'], [])

        backend = EmailBackend()
        backend.send_messages([email])

        mock_popen.assert_called_once_with(
            ['/usr/sbin/sendmail', '-G', '-i', '-f', 'from@example.com', 'to@example.com'],
            close_fds=True, stdin=-1)

        first_write_call = popen.stdin.write.call_args[0]
        message_bytes = first_write_call[0]
        self.assertTrue(isinstance(message_bytes, bytes))

        popen.stdin.close.assert_called_once_with()
