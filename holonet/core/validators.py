# -*- coding: utf8 -*-
from django.core.exceptions import ValidationError


def unique_or_blank(*args, **kwargs):
    raise ValidationError('Bad validator')

