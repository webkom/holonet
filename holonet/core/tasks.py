import email

from celery import Task
from celery.utils.log import get_task_logger
from django.core.exceptions import ObjectDoesNotExist

from holonet import queues
from holonet.lists.models import List


class ProcessQueueTask(Task):

    log = get_task_logger(__name__)

    def run(self, queue, message_list_pk, message_raw, meta):
        """
        Process a message in a queue. Initial parsing is done here.
        """
        queue_instance = queues.get(queue)

        if queue_instance is None:
            self.log.error('Received invalid queue {}'.format(queue))
            return

        try:
            message_list = List.objects.get(pk=message_list_pk)
        except ObjectDoesNotExist:
            message_list = None
            self.log.warning('Received message_list_pk {}, could not find this list.')

        message = email.message_from_string(message_raw)

        self.log.info('Processing message {} with queue {}'.format(message.get('Message-ID', 'N/A'),
                                                                   queue))
        return queue_instance.dispose(message_list, message, meta)
