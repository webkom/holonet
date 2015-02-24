# -*- coding: utf8 -*-

from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class InformationViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        return Response({
            'Master Domains': settings.MASTER_DOMAINS,
            'Server Email': settings.SERVER_EMAIL,
            'Restricted Email': '%s@%s' % (settings.RESTRICTED_PREFIX, settings.MASTER_DOMAIN),
            'System Aliases': settings.SYSTEM_ALIASES,
            'Admins': settings.ADMINS,
            'System Owner': settings.SYSTEM_OWNER,
            'Sender Whitelist': str(settings.SENDER_WHITELIST_ENABLED),
            'Domain Whitelist': str(settings.DOMAIN_WHITELIST_ENABLED),
        })
