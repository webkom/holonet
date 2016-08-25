import logging

from holonet.apps.utils.parsers.email_parser import EmailParser
from holonet.apps.utils.parsers.exceptions import MessageIDNotExistException

log = logging.getLogger('holonet.lmtp.parser')


class LMTPEmailParser(EmailParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = log

    def parse(self):
        msg = super().parse()

        message_id = msg.get('message-id')
        if message_id is None:
            # Messages received with LMTP should contain a MESSAGE-ID header.
            raise MessageIDNotExistException

        return msg
