# -*- coding: utf8 -*-

from celery import task

from .elasticsearch import store_blacklisted_mail, store_bounce_mail, store_spam
from .notify import notify_blacklisted, notify_bounce, notify_spam


@task()
def index_spam(message):
    store_spam(message)


@task
def index_blacklisted_mail(message):
    store_blacklisted_mail(message)


@task
def index_bounce_mail(message):
    store_bounce_mail(message)


@task()
def send_spam_notification(message):
    notify_spam(message)


@task()
def send_blacklist_notification(message):
    notify_blacklisted(message)


@task()
def send_bounce_notification(message):
    notify_bounce(message)
