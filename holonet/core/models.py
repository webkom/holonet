# -*- coding: utf8 -*-

import random
import string

from django.contrib.auth.models import AbstractUser
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


class User(AbstractUser):

    SASL_TOKEN_LENGTH = 32

    sasl_token = models.CharField('SASL Token', max_length=SASL_TOKEN_LENGTH, unique=True)

    def get_sasl_token(self):
        if not self.valid_sasl_token():
            self.sasl_token = self.generate_sasl_token()
            self.save()
        return self.sasl_token

    def valid_sasl_token(self):
        return bool(self.sasl_token is not None and len(self.sasl_token) == self.SASL_TOKEN_LENGTH)

    def generate_sasl_token(self):
        sasl_token = ''.join(random.SystemRandom().choice
                             (string.ascii_uppercase + string.digits)
                             for _ in range(self.SASL_TOKEN_LENGTH))
        return sasl_token
