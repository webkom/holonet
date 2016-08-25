from django.db import models
from django.utils import timezone


class RestrictedListManager(models.Manager):

    def inactive(self):
        return self.get_queryset().filter(timeout__lt=timezone.now())

    def active(self):
        return self.get_queryset().filter(timeout__gte=timezone.now())
