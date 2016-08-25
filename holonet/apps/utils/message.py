import logging
from email.utils import formatdate

from django.core.mail import DNS_NAME, EmailMessage, make_msgid

log = logging.getLogger(__name__)


class HolonetEmailMessage(EmailMessage):

    original_message = None
    manage_headers = ['to', 'cc', 'bcc', 'from', 'reply-to', 'subject']

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

        extra_headers = {}
        for key in msg.keys():
            if key.lower() not in cls.manage_headers:
                extra_headers[key.lower()] = msg[key]

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
            result_message = super().message()
        else:

            msg = self._create_message(self.original_message)

            # Remove managed header from message
            for key in self.manage_headers:
                if key in msg:
                    del msg[key]

            msg['To'] = ', '.join(self.to) or self.extra_headers.get('to', '')
            msg['Cc'] = ', '.join(self.cc) or self.extra_headers.get('cc', '')
            msg['Bcc'] = ', '.join(self.bcc) or self.extra_headers.get('bcc', '')
            msg['From'] = self.from_email or self.extra_headers.get('from', '')
            msg['Reply-To'] = ', '.join(self.reply_to) or self.extra_headers.get('reply-to', '')
            msg['Subject'] = self.subject or self.extra_headers.get('subject', '*** No Subject ***')

            # Check for missing headers
            header_names = [key.lower() for key in self.extra_headers]
            if 'date' not in header_names:
                msg['Date'] = formatdate()
            if 'message-id' not in header_names:
                msg['Message-ID'] = make_msgid(domain=DNS_NAME)
            # Set extra headers
            for name, value in self.extra_headers.items():
                if name.lower() in self.manage_headers:
                    continue
                if name.lower() in msg:
                    del msg[name]
                msg[name] = value

            if self.body is not None:
                log.warning('The message method constructed a email.message.Message based on '
                            'original_message. The content of body is lost!')

            result_message = msg

        return result_message

    def set_header(self, key, value):
        """
        Set or override a header.
        """
        self.extra_headers[key] = str(value)
