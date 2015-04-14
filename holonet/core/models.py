# -*- coding: utf8 -*-

import uuid

from django.db import models
from django.utils import timezone


class SenderList(models.Model):
    sender = models.EmailField(unique=True)

    def __str__(self):
        return self.sender

    class Meta:
        abstract = True


class DomainList(models.Model):
    domain = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.domain

    class Meta:
        abstract = True


class SenderBlacklist(SenderList):
    pass


class DomainBlacklist(DomainList):
    pass


class SenderWhitelist(SenderList):
    pass


class DomainWhitelist(DomainList):
    pass


class TokenModel(models.Model):
    token = models.CharField(max_length=64, unique=True, default='')

    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    @classmethod
    def get_token(cls, token):
        token_object = cls.objects.get(token=token)

        if cls.is_valid(token_object):
            return token_object

        raise cls.DoesNotExist()

    @classmethod
    def is_valid(cls, token):
        now = timezone.now()

        def check_valid_to(date):
            if date is None:
                return True
            elif date > now:
                return True
            return False

        if token.valid_from is not None:
            if token.valid_from < now:
                return check_valid_to(token.valid_to)
        else:
                return check_valid_to(token.valid_to)

        return False

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4()
        super(TokenModel, self).save(*args, **kwargs)
