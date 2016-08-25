from __future__ import absolute_import

import os

import celery
from django.conf import settings


class Celery(celery.Celery):
    def on_configure(self):

        import raven
        from raven.contrib.celery import register_signal, register_logger_signal

        client = raven.Client()

        # register a custom filter to filter out duplicate logs
        register_logger_signal(client)

        # hook into the Celery error handler
        register_signal(client)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holonet.settings')

app = celery.Celery('holonet')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_RESULT_BACKEND=None,
    CELERY_TRACK_STARTED=True,
    CELERY_SEND_EVENTS=True,
    CELERY_TASK_SERIALIZER='pickle',
    CELERY_ENABLE_UTC=True,
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERY_IGNORE_RESULT=True,
    CELERY_ACKS_LATE=True,
    CELERY_PREFETCH_MULTIPLIER=5,
    CELERY_ACCEPT_CONTENT=['pickle', 'json'],
)
