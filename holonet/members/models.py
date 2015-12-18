from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Member(AbstractUser):

    acknowledge_posts = models.BooleanField(default=False, help_text=_('When this member posts to '
                                                                       'a list, receive a '
                                                                       'acknowledgement.'))
