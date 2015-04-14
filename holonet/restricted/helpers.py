# -*- coding: utf8 -*-

import logging

from django.conf import settings

from .models import RestrictedMapping

logger = logging.getLogger(__name__)


def is_restricted(prefix):
    return prefix == settings.RESTRICTED_PREFIX


def lookup(msg, mark_sent=False):

    token = get_payload_token(msg, remove_token=True)

    if not token:
        return []

    try:
        mapping = RestrictedMapping.get_token(token=token)

        if mark_sent:
            mapping.mark_sent()

        return mapping.recipients
    except RestrictedMapping.DoesNotExist:
        logging.warning('Received restricted email with invalid token.', extra={
            'token': token
        })
        pass

    return []


def extract_token(msg, index, delete_token_part):
    part = msg.get_payload(index).get_payload(decode=True)
    if part:
        part = part.decode().strip()

        settings_prefix = settings.RESTRICTED_TOKEN_PREFIX
        if len(part) > (len(settings_prefix) + 1):
            prefix = part[0:len(settings_prefix)]
            token = part[len(settings_prefix)+1:len(part)]

            if prefix.strip() == settings_prefix:
                if delete_token_part:
                    del msg.get_payload()[index]
                return token

    return None


def get_payload_token(msg, remove_token):
    if msg.is_multipart():
        for part_index in range(len(msg.get_payload())):
            if msg.get_payload(part_index).is_multipart():
                extract_result = get_payload_token(msg.get_payload(part_index), remove_token)
                if extract_result:
                    return extract_result
            else:
                extract_result = extract_token(msg, part_index, remove_token)
                if extract_result:
                    return extract_result

    logging.warning('Could not get token from a restricted email. The user may have '
                    'forgotten to add a token.')

    return None
