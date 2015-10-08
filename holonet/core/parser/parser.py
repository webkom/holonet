import email
import logging
from email.message import Message

from .exceptions import DefectMessageException, ParseEmailException


class EmailParser:

    def __init__(self, raw_message, mail_from, message_type):
        self.raw_message = raw_message
        self.mail_from = mail_from
        self.message_type = message_type
        self.log = logging.getLogger('holonet.parser')

    def parse(self):
        try:
            if self.message_type == 'string':
                msg = email.message_from_string(self.raw_message, Message)
            elif self.message_type == 'bytes':
                msg = email.message_from_bytes(self.raw_message, Message)
            elif self.message_type == 'binary_file':
                msg = email.message_from_binary_file(self.raw_message, Message)
            else:
                raise ValueError('Invalid message_type, could not parse message.')
        except Exception:
            raise ParseEmailException

        # Do basic post-processing of the message, checking it for defects or
        # other missing information.
        if msg.defects:
            raise DefectMessageException

        # Add headers used in Holonet
        msg.original_size = len(self.raw_message)
        msg['X-MailFrom'] = self.mail_from

        return msg
