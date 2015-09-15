from holonet.interfaces.queue import Queue


class SyncQueue(Queue):
    """
    The sync queue processes messages when the system receives them. Use AsyncQueue for
    high-volume setups.
    """
    pass
