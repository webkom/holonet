# -*- coding: utf8 -*-

from django.conf import settings


def is_restricted(prefix):
    return prefix == settings.RESTRICTED_PREFIX


def lookup(msg):
    # Cache goes here
    # Lookup in mail attachment

    return []
