from holonet.interfaces.queue import Queue


class BounceQueue(Queue):
    """
    The bounce queues purpose is to create bounces for a message.
    """

    def dispose(self, message_list, message, meta):
        pass
