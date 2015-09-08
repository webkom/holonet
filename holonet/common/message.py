import logging
from email.utils import formatdate

from django.core.mail import DNS_NAME, EmailMessage, make_msgid

log = logging.getLogger(__name__)


class HolonetEmailMessage(EmailMessage):

    original_message = None

    @classmethod
    def parse_message(cls, msg):
        """
        Takes a email.message.Message and read the headers. Stores the original message as a
        original_message attribute on the class.
        """
        def parse_email_list(email_list):
            if email_list is None:
                return []
            else:
                return list(map(str.strip, email_list.split(',')))

        to = parse_email_list(msg.get('to'))
        cc = parse_email_list(msg.get('cc'))
        bcc = parse_email_list(msg.get('bcc'))
        reply_to = parse_email_list(msg.get('reply-to'))
        from_email = msg.get('from', '')
        subject = msg.get('subject', '')

        standard_headers = ['to', 'cc', 'bcc', 'from', 'reply-to', 'subject']
        extra_headers = {}
        for key in msg.keys():
            if key.lower() not in standard_headers:
                extra_headers[key] = msg[key]

        message = cls(to=to, cc=cc, bcc=bcc, from_email=from_email, subject=subject,
                      reply_to=reply_to, headers=extra_headers, body=None)

        message.original_message = msg

        return message

    def message(self):
        """
        Returns a email.message.Message object. The object is based on original_message if
        original_message is not None.
        """
        if self.original_message is None:
            return super().message()

        msg = self._create_message(self.original_message)
        msg['Subject'] = self.subject
        msg['From'] = self.extra_headers.get('From', self.from_email)
        msg['To'] = self.extra_headers.get('To', ', '.join(self.to))
        if self.cc:
            msg['Cc'] = ', '.join(self.cc)
        if self.reply_to:
            msg['Reply-To'] = self.extra_headers.get('Reply-To', ', '.join(self.reply_to))
        header_names = [key.lower() for key in self.extra_headers]
        if 'date' not in header_names:
            msg['Date'] = formatdate()
        if 'message-id' not in header_names:
            msg['Message-ID'] = make_msgid(domain=DNS_NAME)
        for name, value in self.extra_headers.items():
            if name.lower() in ('from', 'to'):
                continue
            if name.lower() in msg:
                del msg[name]
            msg[name] = value

        if self.body is not None:
            log.warning('The message method constructed a email.message.Message based on '
                        'original_message. The content of body is lost!')

        return msg

    def set_header(self, key, value):
        """
        Set or override a header.
        """
        self.extra_headers[key] = str(value)
