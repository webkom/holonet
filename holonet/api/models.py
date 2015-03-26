# -*- coding: utf8 -*-

import uuid

from django.db import models

from holonet.core.models import TokenModel


class Application(models.Model):
    name = models.CharField(max_length=200)

    def has_perm(self, *args, **kwargs):
        return True

    def has_perms(self, *args, **kwargs):
        return True

    def is_authenticated(self):
        return True

    @property
    def is_staff(self):
        return True

    @property
    def is_superuser(self):
        return False

    def is_active(self):
        tokens = self.tokens.all()
        for token in tokens:
            if Token.is_valid(token):
                return True
        return False

    def __str__(self):
        return self.name


class Token(TokenModel):
    application = models.ForeignKey('api.Application', related_name='tokens')

    def __str__(self):
        return '%s - %s' % (self.application, self.token)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4()
        super(Token, self).save(*args, **kwargs)
