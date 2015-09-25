from holonet.interfaces.queue_runner import QueueRunner


class DirectQueueRunner(QueueRunner):

    def setup(self):
        pass

    def process_message(self, queue_instance, message_list, message, meta):
        try:
            queue_instance.dispose(message_list, message, meta)
        except Exception:
            self.log.exception('Could not process the message {} using the queue {}'.format(
                message.get('message-id', 'unknown-id'), queue_instance
            ))
