import logging
from abc import abstractmethod

from holonet.core.manager import ServiceManager
from holonet.queues import archive, bounce, digest, incoming, outgoing, pipeline, retry, virgin


class QueueRunner:

    log = logging.getLogger(__name__)

    def __init__(self):
        self.log.info('Initializing queues')
        self.manager = ServiceManager()
        self.manager.add('archive', archive.ArchiveQueue())
        self.manager.add('bounce', bounce.BounceQueue())
        self.manager.add('digest', digest.DigestQueue())
        self.manager.add('in', incoming.IncomingQueue())
        self.manager.add('out', outgoing.OutgoingQueue())
        self.manager.add('pipeline', pipeline.PipelineQueue())
        self.manager.add('retry', retry.RetryQueue())
        self.manager.add('virgin', virgin.ViriginQueue())

    @abstractmethod
    def setup(self):
        pass

    def enqueue(self, queue, message_list, message, meta):
        queue_instance = self.manager.get(queue)
        assert (queue_instance is not None), '{} is not a valid queue name.'.format(queue)
        self.log.info('Processing message {} with the {} queue'.format(
            message.get('message-id', 'unknown-id'), queue)
        )
        self.process_message(queue_instance, message_list, message, meta)

    @abstractmethod
    def process_message(self, queue_instance, message_list, message, meta):
        pass
