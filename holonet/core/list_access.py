# -*- coding: utf8 -*-

from django.conf import settings

from holonet.lists.helpers import clean_address, split_address

from .models import DomainBlacklist, DomainWhitelist, SenderBlacklist, SenderWhitelist


def is_blacklisted(sender):
    sender = clean_address(sender)
    prefix, domain = split_address(sender)

    if DomainBlacklist.objects.filter(domain=domain).exists():
        return True

    if SenderBlacklist.objects.filter(sender=sender).exists():
        return True

    return False


def is_not_whitelisted(sender):
    sender = clean_address(sender)
    prefix, domain = split_address(sender)

    if settings.SENDER_WHITELIST_ENABLED:
        if SenderWhitelist.objects.filter(sender=sender).exists():
            return False

    if settings.DOMAIN_WHITELIST_ENABLED:
        if DomainWhitelist.objects.filter(domain=domain).exists():
            return False

    return bool(settings.SENDER_WHITELIST_ENABLED or settings.DOMAIN_WHITELIST_ENABLED)
