import logging

from django.contrib.postgres.fields import ArrayField
from django.db import models

from holonet.interfaces.storage_backend import StorageBackend
from holonet.interfaces.storage_email import StorageEmail

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
        return StorageEmail(**model_instance.as_dict())


class EmailStorage(models.Model):

    timestamp = models.DateTimeField()
    from_email = models.CharField(max_length=200)
    to = ArrayField(models.CharField(max_length=200))
    copy = ArrayField(models.CharField(max_length=200), default=[])
    blind_copy = ArrayField(models.CharField(max_length=200), default=[])
    recipients = ArrayField(models.CharField(max_length=200))
    subject = models.CharField(max_length=300)
    raw = models.TextField()
    message_type = models.CharField(max_length=20, choices=StorageBackend.MESSAGE_TYPES)

    def __str__(self):
        return '{} From: {}'.format(str(self.timestamp), self.from_email)

    class Meta:
        app_label = 'storage'

    def as_dict(self):
        return {
            'from_email': self.from_email,
            'to': self.to,
            'copy': self.copy,
            'blind_copy': self.blind_copy,
            'recipients': self.recipients,
            'subject': self.subject,
            'raw': self.raw,
            'message_type': self.message_type,
            'timestamp': self.timestamp
        }
