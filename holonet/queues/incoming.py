from holonet.interfaces.queue import Queue


class IncomingQueue(Queue):
    """
    The incoming queues sole purpose in life is to decide the disposition of the message.  It can
    either be accepted for delivery, rejected (i.e. bounced), held for moderator approval,
    or discarded.

    When accepted, the message is forwarded on to the `pipeline queue` where it is prepared for
    delivery.
    """

    def dispose(self, message_list, message, meta):
        pass
