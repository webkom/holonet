from django.utils import timezone

from holonet.interfaces.handler import Handler


class AfterDeliveryHandler(Handler):

    @classmethod
    def process(cls, message_list, message, meta):
        """
        Update last post at datetime and increment the message counter.
        """
        message_list.last_post_at = timezone.now()
        message_list.processed_messages += 1
        message_list.save()
