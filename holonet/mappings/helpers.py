# -*- coding: utf8 -*-

from django.conf import settings

from .models import MailingList


def is_prefix_valid(prefix):
    try:
        if prefix.lower() in [settings.RESTRICTED_PREFIX, settings.SERVER_EMAIL.split('@')[0]]:
            return True

        mailing_list = MailingList.objects.get(prefix=prefix.lower)
        if len(mailing_list.recipients) > 0:
            return True
    except MailingList.DoesNotExist:
        pass
    return False