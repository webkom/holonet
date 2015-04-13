# -*- coding: utf8 -*-

import uuid

from django.db import IntegrityError, models

from holonet.core.models import TokenModel

from .managers import RestrictedMappingManager


class RestrictedMapping(TokenModel):

    from_address = models.EmailField()
    is_used = models.BooleanField(default=False)

    recipient_list = models.ManyToManyField('mappings.Recipient', blank=True,
                                            related_name='restricted_lists')
    tag = models.CharField(max_length=100, unique=True, null=True)

    objects = RestrictedMappingManager()

    @property
    def recipients(self):
        return [recipient.address for recipient in self.recipient_list.all()]

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4()

        if self.tag == '':
            raise IntegrityError('The tag field cannot be a empty string.')

        return super(RestrictedMapping, self).save(*args, **kwargs)

    def regenerate_token(self):
        self.token = uuid.uuid4()

    def mark_sent(self):
        self.is_used = True
        self.save()

    @classmethod
    def get_token(cls, token):
        object_instance = super(RestrictedMapping, cls).get_token(token=token)
        if not object_instance.is_used:
            return object_instance
        else:
            raise cls.DoesNotExist()

    def __str__(self):
        return '%s - %s' % (self.from_address, self.token)
