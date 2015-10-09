from holonet.interfaces.queue import Queue


class RetryQueue(Queue):
    """
    The retry queue handles retries for messages.
    """

    def dispose(self, message_list, message, meta):
        pass
