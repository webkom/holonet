from holonet.interfaces.queue import Queue


class AsyncQueue(Queue):
    """
    The async queue processes messages using Celery workers.
    """
    pass
