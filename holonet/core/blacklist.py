# -*- coding: utf8 -*-

from holonet.mappings.helpers import clean_address, split_address

from .models import DomainBlacklist, SenderBlacklist


def is_blacklisted(sender):
    sender = clean_address(sender)
    prefix, domain = split_address(sender)

    try:
        SenderBlacklist.objects.get(sender=sender)
        return True
    except SenderBlacklist.DoesNotExist:
        pass

    try:
        DomainBlacklist.objects.get(domain=domain)
        return True
    except DomainBlacklist.DoesNotExist:
        pass

    return False
