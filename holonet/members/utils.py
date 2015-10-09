import logging

from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

log = logging.getLogger(__name__)


def retrieve_member_by_email(email):
    """
    This function tries to find a user based on an email address. If no user is found or multiple
    objects is returned the function returns None.
    """
    try:
        user = User.objects.get(email=email)
        return user
    except ObjectDoesNotExist:
        log.info('Lookup on member with email {} returned no results.'.format(email))
    except MultipleObjectsReturned:
        log.warning('Lookup on member with email {} returned multiple results. Holonet cannot '
                    'find correct member by email. This user may loose some of the functionality '
                    'in Holonet.'.format(email))
    return None
