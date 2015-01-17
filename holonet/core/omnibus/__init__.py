# -*- coding: utf8 -*-

from django.conf import settings

if not settings.TESTING:
    from omnibus.api import publish
else:
    def publish(channel, payload_type, payload=None, sender=None):
        pass
