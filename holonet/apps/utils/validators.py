from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _


class DomainValidator:

    def __init__(self):
        self.email_validator = EmailValidator()

    def __call__(self, domain):
        if not self.email_validator.validate_domain_part(domain):
            raise ValidationError(_('Enter a valid domain name.'), code='invalid')

domain_validator = DomainValidator()


class LocalValidator:
    def __init__(self):
        self.email_validator = EmailValidator()

    def __call__(self, local_part):
        try:
            self.email_validator('{}@domain.com'.format(local_part))
        except ValidationError:
            raise ValidationError(_('Enter a valid local part.'), code='invalid')

local_validator = LocalValidator()
