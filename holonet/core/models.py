# -*- coding: utf8 -*-

from django.db import models
from django.utils import timezone


class SenderBlacklist(models.Model):
    sender = models.EmailField(unique=True)


class DomainBlacklist(models.Model):
    domain = models.CharField(max_length=100, unique=True)


class TokenModel(models.Model):
    token = models.CharField(max_length=64, unique=True)

    valid_from = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)

    @classmethod
    def get_token(cls, token):
        now = timezone.now()
        token_object = cls.objects.get(token=token)

        def check_valid_to(date):
            if date is None:
                return token_object
            elif date > now:
                return token_object
            raise cls.DoesNotExist()

        if token_object.valid_from is not None:
            if token_object.valid_from < now:
                return check_valid_to(token_object.valid_to)
        else:
                return check_valid_to(token_object.valid_to)

        raise cls.DoesNotExist()

    class Meta:
        abstract = True
