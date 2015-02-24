# -*- coding: utf8 -*-

import logging

from celery import task
from redis.exceptions import ConnectionError

from .elasticsearch import store_blacklisted_mail, store_bounce_mail, store_spam, store_statistics

log = logging.getLogger(__name__)


def call_task(task, *args, **kwargs):
    try:
        task.delay(*args, **kwargs)
    except (OSError, ConnectionError):
        log.error('Cannot connect to celery broker...')


@task()
def index_spam(message):
    store_spam(message)


@task()
def index_blacklisted_mail(message):
    store_blacklisted_mail(message)


@task()
def index_bounce_mail(message):
    store_bounce_mail(message)


@task()
def index_statistics(sender, list, recipients):
    store_statistics(sender, list, recipients)
