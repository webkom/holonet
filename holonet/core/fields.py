from django.db import models
from django.utils.translation import ugettext_lazy as _

from holonet.core import validators


class EmailField(models.EmailField):
    pass


class DomainField(models.CharField):
    """
    This class represents a model field that stores a domain. Domains are case insensitive.
    """
    description = _('Domain name')
    default_validators = [validators.domain_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 254)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'error_messages': {
                'invalid': _('Enter a valid domain name.'),
            }
        }
        defaults.update(kwargs)
        return super(DomainField, self).formfield(**defaults)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        value = value.lower()
        return value


class LocalPartField(models.CharField):
    """
    This class represents a model field that stores the local part of an email address. The local
    part is case insensitive.
    """
    description = _('Local part of an email address')
    default_validators = [validators.local_validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 254)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'error_messages': {
                'invalid': _('Enter a valid local_part.'),
            }
        }
        defaults.update(kwargs)
        return super(LocalPartField, self).formfield(**defaults)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        value = value.lower()
        return value
