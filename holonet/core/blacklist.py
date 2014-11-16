# -*- coding: utf8 -*-

from django.core.validators import validate_email, ValidationError

from .models import SenderBlacklist, DomainBlacklist


def is_blacklisted(sender):
    try:
        validate_email(sender)
        prefix, domain = sender.split('@')

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

    except ValidationError:
        pass
    except ValueError:
        pass

    try:
        DomainBlacklist.objects.get(domain=sender)
        return True
    except DomainBlacklist.DoesNotExist:
        pass

    return False
