from holonet.interfaces.queue import Queue


class OutgoingQueue(Queue):
    """
    The outgoing queue handles outgoing messages.
    """

    def dispose(self, message_list, message, meta):
        pass
