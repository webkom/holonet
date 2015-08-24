import logging

from django.conf import settings

log = logging.getLogger(__name__)

"""
Storage backend singleton
Initialized by the app config
"""
storage_backend = None


def index_message(message):
    log.info('Indexing message from {} using the {} backend.'.format(
        message.from_email,
        settings.STORAGE_BACKEND
    ))
    return storage_backend.index_message(message)


def retrieve_history(from_time, to_time, filter=None, search_query=None):
    log.info('Retrieving message from the {} backend with filter {} and query {}'.format(
        settings.STORAGE_BACKEND,
        str(filter),
        str(search_query)
    ))
    return storage_backend.retrieve_history(from_time, to_time, filter, search_query)
