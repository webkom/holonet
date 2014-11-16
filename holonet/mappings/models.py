# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .validators import validate_local_part


class MailingList(models.Model):
    prefix = models.CharField(max_length=64, verbose_name=_('prefix'),
                              validators=[validate_local_part], unique=True, db_index=True)

    recipient_list = models.ManyToManyField('mappings.Recipient', verbose_name=_('recipients'),
                                            blank=True)

    def __str__(self):
        return '%s@%s' % (self.prefix, settings.MASTER_DOMAINS[0])

    @property
    def recipients(self):
        return [recipient.address for recipient in self.recipient_list.all()]


class Recipient(models.Model):
    address = models.EmailField(verbose_name=_('address'))
    tag = models.CharField(max_length=100, verbose_name=_('tag'), unique=True)

    def __str__(self):
        return '%s' % (self.address, )
