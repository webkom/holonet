# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .validators import validate_local_part


class MailingList(models.Model):
    prefix = models.CharField(max_length=64, verbose_name=_('prefix'),
                              validators=[validate_local_part], unique=True)

    def __str__(self):
        return '%s@%s' % (self.prefix, settings.MASTER_DOMAINS[0])

    @property
    def recipients(self):
        return [member.address for member in self.members.all()]


class Member(models.Model):
    mailing_list = models.ForeignKey('mappings.MailingList', verbose_name=_('mailing list'),
                                     related_name='members')
    address = models.EmailField(verbose_name=_('address'))

    def __str__(self):
        return '%s :: %s' % (self.mailing_list.prefix, self.address)

    class Meta:
        unique_together = ('mailing_list', 'address')
