from holonet.queue.queue import HolonetQueue


class SyncQueue(HolonetQueue):
    """
    The sync queue processes messages when the system receives them. Use AsyncQueue for
    high-volume setups.
    """
    pass
