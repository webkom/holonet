from holonet.interfaces.queue import Queue


class DigestQueue(Queue):
    """
    The digest queues purpose is to handle digests for list with digests enabled.
    """

    def dispose(self, message_list, message, meta):
        pass
