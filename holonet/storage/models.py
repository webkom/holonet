from django.contrib.postgres.fields import ArrayField
from django.db import models

from holonet.storage.base import StorageBackend


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
