# -*- coding: utf8 -*-

from celery import task

from .elasticsearch import store_spam, store_blacklisted_mail
from .notify import notify_spam, notify_blacklisted


@task()
def index_spam(message):
    store_spam(message)


@task
def index_blacklisted_mail(message):
    store_blacklisted_mail(message)


@task()
def send_spam_notification(message):
    notify_spam(message)


@task()
def send_blacklist_notification(message):
    notify_blacklisted(message)
