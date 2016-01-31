import logging

from holonet.core.parser import EmailParser
from holonet.core.parser.exceptions import MessageIDNotExistException


class LMTPEmailParser(EmailParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = logging.getLogger('holonet.lmtp.parser')

    def parse(self):
        msg = super().parse()

        message_id = msg.get('message-id')
        if message_id is None:
            # Messages received with LMTP should contain a MESSAGE-ID header.
            raise MessageIDNotExistException

        return msg
