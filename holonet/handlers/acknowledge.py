import logging

from holonet.interfaces.handler import Handler
from holonet.members import utils

log = logging.getLogger('handler.acknowledge')


class Acknowledge(Handler):
    """
    Send an acknowledgment of the successful post to the sender.

    This only happens if the sender has set their acknowledge_posts attribute.
    """

    @classmethod
    def process(cls, message_list, message, meta):
        sender = meta.get('original_sender', message.sender)
        user = utils.retrieve_member_by_email(sender)
        if user is None or user.member.acknowledge_posts is False:
            return

        # We found the member that wants to receive an acknowledgement
        # TODO: Construct a message and send it to the user.
        return True  # Return True, just for testing
