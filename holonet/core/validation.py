# -*- coding: utf8 -*-

import sys

from django.conf import settings

from holonet.mappings.helpers import is_prefix_valid


def validate_recipient(params=None, recipient='', sys_exit=False):
    exit_options = {
        'unknown_recipient': {
            'exit_code': settings.EXITCODE_UNKNOWN_RECIPIENT,
            'action': {'action': '%s Address does not exist' % settings.REJECT_ACTION}
        },
        'no_recipient': {
            'exit_code': settings.EXITCODE_UNKNOWN_RECIPIENT,
            'action': {'action': '%s No recipient listed' % settings.REJECT_ACTION}
        },
        'incomplete_address': {
            'exit_code': settings.EXITCODE_UNKNOWN_RECIPIENT,
            'action': {'action': '%s Address incomplete' % settings.REJECT_ACTION}
        },
        'unknown_domain': {
            'exit_code': settings.EXITCODE_UNKNOWN_DOMAIN,
            'action': {'action': '%s Domain is not handled by holonet' % settings.REJECT_ACTION}
        },
        'valid_recipient': {
            'exit_code': 0,
            'action': {'action': '%s' % settings.ACCEPT_ACTION}
        }
    }

    def return_result(result):
        if sys_exit is False:
            return exit_options[result]['action']
        else:
            if result != 'valid_recipient':
                sys.exit(exit_options[result]['exit_code'])
            else:
                return True

    if params:
        if 'recipient' not in params:
            return return_result('no_recipient')

        recipient = params["recipient"]

    if not recipient:
        return return_result('no_recipient')

    splitted = recipient.split('@')

    if len(splitted) == 1:
        prefix = splitted[0]
        if prefix in settings.SYSTEM_ALIASES:
            return return_result('valid_recipient')

    if len(splitted) < 2:
        return return_result('incomplete_address')

    prefix, domain = splitted

    if domain in settings.MASTER_DOMAINS:

        if is_prefix_valid(prefix):
            return return_result('valid_recipient')
        else:
            return return_result('unknown_recipient')

    else:
        return return_result('unknown_domain')
