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

    def is_staff(self):
        return True

    def is_superuser(self):
        return False

    def __str__(self):
        return self.name


class Token(TokenModel):
    application = models.ForeignKey('api.Application')

    def __str__(self):
        return '%s - %s' % (self.application, self.token)
