# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class SenderBlacklist(models.Model):
    sender = models.EmailField(verbose_name=_('sender'), unique=True)


class DomainBlacklist(models.Model):
    domain = models.CharField(verbose_name=_('domain'), max_length=100)
