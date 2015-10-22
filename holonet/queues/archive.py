from holonet.interfaces.queue import Queue


class ArchiveQueue(Queue):
    """
    The archive queues purpose is store the message in the archive.
    """

    def dispose(self, message_list, message, meta):
        print('Hei')
        return 'hei du'
