# -*- coding: utf8 -*-

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


class Token(TokenModel):
    application = models.ForeignKey('api.Application')
