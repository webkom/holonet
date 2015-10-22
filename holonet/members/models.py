from django.contrib.auth.hashers import check_password, is_password_usable, make_password
from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Member(models.Model):

    username = models.CharField(_('username'), max_length=30, unique=True, validators=[
        validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username. This value may '
                                                    'contain only letters, numbers '
                                                    'and @/./+/-/_ characters.'), 'invalid'),
        ])
    first_name = models.CharField(_('first name'), max_length=40, blank=True)
    last_name = models.CharField(_('last name'), max_length=40, blank=True)
    email = models.EmailField(_('email address'))
    password = models.CharField(_('password'), max_length=128, blank=True)
    is_active = models.BooleanField(_('active'), default=True)

    acknowledge_posts = models.BooleanField(default=False, help_text=_('When this member posts to '
                                                                       'a list, receive a '
                                                                       'acknowledgement.'))

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        self.password = make_password(None)

    def has_usable_password(self):
        return is_password_usable(self.password)
