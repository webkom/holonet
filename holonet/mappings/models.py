# -*- coding: utf8 -*-

from django.conf import settings
from django.db import IntegrityError, models

from .validators import validate_local_part


class MailingList(models.Model):
    prefix = models.CharField(max_length=64, validators=[validate_local_part], unique=True,
                              db_index=True)

    recipient_list = models.ManyToManyField('mappings.Recipient', blank=True,
                                            related_name='mailing_lists')
    tag = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return '%s@%s' % (self.prefix, settings.MASTER_DOMAIN)

    @property
    def recipients(self):
        return [recipient.address for recipient in self.recipient_list.all()]

    def save(self, *args, **kwargs):
        if self.tag == '':
            raise IntegrityError('The tag field cannot be a empty string.')
        return super(MailingList, self).save(*args, **kwargs)


class Recipient(models.Model):
    address = models.EmailField()
    tag = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return '%s' % (self.address, )

    @property
    def lists(self):
        return [mailing_list.prefix for mailing_list in self.mailing_lists.all()]

    def save(self, *args, **kwargs):
        if self.tag == '':
            raise IntegrityError('The tag field cannot be a empty string.')
        return super(Recipient, self).save(*args, **kwargs)
