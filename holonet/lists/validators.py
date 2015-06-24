from django.core.validators import ValidationError, validate_email


def validate_local_part(value):
    try:
        validate_email('%s@holonet.no' % value)
    except ValidationError:
        raise ValidationError('Invalid local part.')
