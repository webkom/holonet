from abc import abstractclassmethod
from holonet.utils.types import assert_string, assert_list_of_strings, assert_datetime, \
    assert_type
from django.utils.timezone import now
from django.utils.importlib import import_module
from django.conf import settings

default_app_config = 'holonet.storage.apps.DataConfig'


def get_storage_backend():
    storage_module = import_module(settings.STORAGE_BACKEND)
    storage_backend = storage_module.Backend
    return storage_backend


class StorageBackend:

    MESSAGE_TYPES = (
        ('spam', 'spam'),
        ('blacklisted', 'blacklisted'),
        ('bounce', 'bounce'),
    )

    @abstractclassmethod
    def configure(cls):
        pass

    @abstractclassmethod
    def index_message(cls, message):
        assert_type(message, StoredEmail)

    @abstractclassmethod
    def retrieve_history(cls, from_time, to_time, filter=None, search_query=None):
        assert_datetime(from_time)
        assert_datetime(to_time)


class StoredEmail:

    def __init__(self, from_email, to, recipients, subject, raw, message_type, timestamp=None):

        assert_string(from_email)
        self.from_email = from_email

        assert_list_of_strings(to)
        self.to = to

        assert_list_of_strings(recipients)
        self.recipients = recipients

        assert_string(subject)
        self.subject = subject

        assert_string(raw)
        self.raw = raw

        assert_string(message_type)
        assert message_type in (element[0] for element in StorageBackend.MESSAGE_TYPES), \
            'Invalid message type %s' % message_type
        self.message_type = message_type

        if timestamp is None:
            timestamp = now()

        assert_datetime(timestamp)
        self.timestamp = timestamp
