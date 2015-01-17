# -*- coding: utf8 -*-

from django.db import models


class SenderBlacklist(models.Model):
    sender = models.EmailField(unique=True)


class DomainBlacklist(models.Model):
    domain = models.CharField(max_length=100, unique=True)
