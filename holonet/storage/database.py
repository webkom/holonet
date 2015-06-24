import logging

from django.contrib.postgres.fields import ArrayField
from django.db import models

from holonet.utils.types import assert_string

from . import StorageBackend, StoredEmail

log = logging.getLogger(__name__)


class Backend(StorageBackend):

    @classmethod
    def configure(cls):
        pass

    @classmethod
    def index_message(cls, message):
        super().index_message(message)
        mail = EmailStorage(timestamp=message.timestamp, from_email=message.from_email,
                            to=message.to, recipients=message.recipients,
                            subject=message.subject, raw=message.raw,
                            message_type=message.message_type)
        mail.save()

    @classmethod
    def retrieve_history(cls, from_time, to_time, filter=None, search_query=None):
        super().retrieve_history(from_time, to_time, filter, search_query)

        if filter is None:
            filter = StorageBackend.MESSAGE_TYPES

        emails = EmailStorage.objects.filter(message_type__in=filter, timestamp__gte=from_time,
                                             timestamp__lte=to_time)

        if search_query is not None and search_query != '':
            assert_string(search_query)
            log.warning("The database storage backend does not support text search.")

        return list(map(cls.model_to_stored_email, emails))

    @classmethod
    def model_to_stored_email(cls, model_instance):
        return StoredEmail(model_instance.from_email, list(model_instance.to),
                           list(model_instance.recipients), model_instance.subject,
                           model_instance.raw, model_instance.message_type,
                           model_instance.timestamp)


class EmailStorage(models.Model):

    timestamp = models.DateTimeField()
    from_email = models.CharField(max_length=200)
    to = ArrayField(models.CharField(max_length=200))
    recipients = ArrayField(models.CharField(max_length=200))
    subject = models.CharField(max_length=300)
    raw = models.TextField()
    message_type = models.CharField(max_length=20, choices=StorageBackend.MESSAGE_TYPES)

    def __str__(self):
        return self.subject
