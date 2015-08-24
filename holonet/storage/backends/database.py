import logging

from holonet.storage.base import StorageBackend, StoredEmail
from holonet.storage.models import EmailStorage

log = logging.getLogger(__name__)


class Backend(StorageBackend):

    def configure(self):
        pass

    def index_message(self, message):
        mail = EmailStorage(**message.as_dict())
        mail.save()

    def retrieve_history(self, from_time=None, to_time=None, filter=None, search_query=None):
        if filter is None:
            filter = StorageBackend.MESSAGE_TYPES_LIST

        query_dict = {'message_type__in': filter}

        if from_time is not None:
            query_dict.update({'timestamp__gte': from_time})

        if to_time is not None:
            query_dict.update({'timestamp__lte': to_time})

        emails = EmailStorage.objects.filter(**query_dict)

        if search_query is not None and search_query != '':
            log.warning("The database storage backend does not support text search.")

        return list(map(self.model_to_stored_email, emails))

    def model_to_stored_email(self, model_instance):
        return StoredEmail(**model_instance.as_dict())
