import logging

from celery import Task
from django.conf import settings

from holonet.interfaces.queue_runner import QueueRunner


class CeleryQueueRunner(QueueRunner):

    def setup(self):
        pass

    def process_message(self, queue_instance, message_list, message, meta):
        task = self.CeleryProcessTask()
        task.delay(queue_instance, message_list, message, meta)

    class CeleryProcessTask(Task):

        name = 'CeleryQueueRunner'
        max_retries = 2
        default_retry_delay = 5
        ignore_result = False
        send_error_emails = (not settings.DEBUG)
        track_started = True
        log = logging.getLogger(__name__)

        def run(self, queue_instance, message_list, message, meta):
            self.log.info('Processing message {} with the {} queue'.format(
                message.get('message-id', 'unknown-id'), queue_instance)
            )
            queue_instance.dispose(message_list, message, meta)

        def after_return(self, status, retval, task_id, args, kwargs, einfo):
            pass

        def on_success(self, retval, task_id, args, kwargs):
            pass

        def on_failure(self, exc, task_id, args, kwargs, einfo):
            self.retry(exc=exc)

        def on_retry(self, exc, task_id, args, kwargs, einfo):
            pass
