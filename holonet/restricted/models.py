# -*- coding: utf8 -*-

import uuid

from django.db import models

from .managers import RestrictedMappingManager
from holonet.core.models import TokenModel


class RestrictedMapping(TokenModel):

    from_address = models.EmailField()
    is_used = models.BooleanField(default=False)

    objects = RestrictedMappingManager()

    @property
    def recipients(self):
        return []

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4()
        super(RestrictedMapping, self).save(*args, **kwargs)

    def regenerate_token(self):
        self.token = uuid.uuid4()



