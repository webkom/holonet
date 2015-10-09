from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):

    user = models.OneToOneField(User, related_name='member')

    acknowledge_posts = models.BooleanField(default=False)
