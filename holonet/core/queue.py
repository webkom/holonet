from django.conf import settings
from django.utils.module_loading import import_string


def queue_runner_cls():
    return import_string(settings.QUEUE_RUNNER)

queue_runner_instance = queue_runner_cls()()


def fetch_queue_runner():
    return queue_runner_instance
