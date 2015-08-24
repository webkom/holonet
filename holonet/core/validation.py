import logging
import sys

from django.conf import settings
from django.core.validators import ValidationError, validate_email

from holonet.lists.helpers import clean_address, is_managed_domain, is_prefix_valid, split_address

logger = logging.getLogger(__name__)


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

        logging.info('Recipient validation result for %s: %s' % (recipient, result))

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

    recipient = clean_address(recipient)
    prefix, domain = split_address(recipient)

    try:
        validate_email(recipient)
    except ValidationError:
        return return_result('incomplete_address')

    if not is_managed_domain(domain):
        return return_result('unknown_domain')

    if not is_prefix_valid(prefix):
        return return_result('unknown_recipient')

    return return_result('valid_recipient')
