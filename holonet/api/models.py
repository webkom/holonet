# -*- coding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .exceptions import TokenDoesNotExistException


class Application(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))

    def has_perm(self, *args, **kwargs):
        return True

    def has_perms(self, *args, **kwargs):
        return True

    def is_authenticated(self):
        return True


class Token(models.Model):
    application = models.ForeignKey('api.Application', verbose_name=_('application'))
    token = models.CharField(max_length=64, unique=True)

    valid_from = models.DateTimeField(auto_now_add=True, blank=True, null=True,
                                      verbose_name=_('valid from'))
    valid_to = models.DateTimeField(blank=True, null=True, verbose_name=_('valid to'))

    @classmethod
    def get_token(cls, token):
        try:
            now = timezone.now()
            token_object = cls.objects.get(token=token)

            def check_valid_to(date):
                if date is None:
                    return token_object
                elif date > now:
                    return token_object
                raise TokenDoesNotExistException('The token %s does not exist.' % token)

            if token_object.valid_from is not None:
                if token_object.valid_from < now:
                    return check_valid_to(token_object.valid_to)
            else:
                    return check_valid_to(token_object.valid_to)

        except cls.DoesNotExist:
            pass

        raise TokenDoesNotExistException('The token %s does not exist.' % token)
