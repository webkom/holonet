# -*- coding: utf8 -*-

from django.conf import settings


def is_restricted(prefix):
    return prefix == settings.RESTRICTED_PREFIX


def lookup(msg):
    # Cache goes here

    return []


def reverse_lookup(token):
    # Cache goes here

    return []
