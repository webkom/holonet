from django.conf import settings
from django.utils.module_loading import import_string


def queue_cls():
    return import_string(settings.MAIL_QUEUE)

queue_instance = queue_cls()()


def fetch_queue():
    return queue_instance
