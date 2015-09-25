from holonet.interfaces.queue import Queue


class ViriginQueue(Queue):
    """
    The virgin queue handles messages Holonet has given birth to.
    E.g. acknowledgment responses to user posts or replybot messages.  They need to go through
    some minimal processing before they can be sent out to the recipient.
    """

    def dispose(self, message_list, message, meta):
        pass
