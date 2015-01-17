# -*- coding: utf8 -*-

from django.conf import settings

from .models import MailingList
from holonet.restricted.helpers import is_restricted, lookup as restricted_lookup


def is_prefix_valid(prefix):
    # Needs to accept mappings

    if is_bounce(prefix):
        return True

    if is_restricted(prefix):
        return True

    if is_server_alias(prefix):
        return True

    return len(lookup(prefix)) > 0


def lookup(prefix, msg=None):

    if is_server_alias(prefix):
        return [address[1] for address in settings.ADMINS]

    if is_restricted(prefix) and msg:
        return restricted_lookup(msg)

    try:
        # Cache goes here

        mapping = MailingList.objects.get(prefix=prefix)
        return mapping.recipients

    except MailingList.DoesNotExist:
        pass

    return []


def reverse_lookup(prefix):
    # only mapings, for safety
    return []


def clean_address(address):
    # Make the address lowercase and remove whitespaces.
    # Always return something like xxx@xxx
    address = address.lower().strip()
    domain = settings.MASTER_DOMAIN

    splitted_address = address.split('@')

    if len(splitted_address) == 1:
        splitted_address.append(domain)
        return '@'.join(splitted_address).lower()
    elif len(splitted_address) == 2:
        return '@'.join(splitted_address).lower()
    else:
        return '@'.join(splitted_address[:2]).lower()


def split_address(address):
    spitted_address = address.split('@')
    prefix, domain = spitted_address
    return prefix, domain


def is_bounce(prefix):
    return prefix.lower().strip() == settings.SERVER_EMAIL.split('@')[0].lower().strip()


def is_server_alias(prefix):
    return prefix in settings.SYSTEM_ALIASES


def is_managed_domain(domain):
    return domain in settings.MASTER_DOMAINS


class LookupAddress(object):

    def __init__(self, address):
        self.email = address
