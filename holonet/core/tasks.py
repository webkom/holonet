# -*- coding: utf8 -*-

from celery import task

from .elasticsearch import store_spam
from .notify import notify_spam


@task()
def index_spam(message):
    store_spam(message)


@task()
def send_spam_notification(message):
    notify_spam(message)
