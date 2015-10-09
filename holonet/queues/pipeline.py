from holonet.interfaces.queue import Queue


class PipelineQueue(Queue):
    """
    This pipeline queue purpose is to take messages that have been approved for posting through the
    'preparation pipeline'.  This pipeline adds, deletes and modifies headers, calculates message
    recipients, and more.
    """

    def dispose(self, message_list, message, meta):
        pass
