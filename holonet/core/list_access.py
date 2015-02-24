# -*- coding: utf8 -*-

from django.conf import settings

from holonet.mappings.helpers import clean_address, split_address

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist


def is_blacklisted(sender):
    sender = clean_address(sender)
    prefix, domain = split_address(sender)

    try:
        DomainBlacklist.objects.get(domain=domain)
        return True
    except DomainBlacklist.DoesNotExist:
        pass

    try:
        SenderBlacklist.objects.get(sender=sender)
        return True
    except SenderBlacklist.DoesNotExist:
        pass

    return False


def is_not_whitelisted(sender):
    sender = clean_address(sender)
    prefix, domain = split_address(sender)

    if settings.SENDER_WHITELIST_ENABLED:
        try:
            SenderWhitelist.objects.get(sender=sender)
            return False
        except SenderWhitelist.DoesNotExist:
            pass

    if settings.DOMAIN_WHITELIST_ENABLED:
        try:
            DomainWhitelist.objects.get(domain=domain)
            return False
        except DomainWhitelist.DoesNotExist:
            pass

    return bool(settings.SENDER_WHITELIST_ENABLED or settings.DOMAIN_WHITELIST_ENABLED)
