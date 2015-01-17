# -*- coding: utf8 -*-

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from django.conf import settings


class InformationViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        return Response({
            'Master Domains': settings.MASTER_DOMAINS,
            'Server Email': settings.SERVER_EMAIL,
            'Restricted Email': '%s@%s' % (settings.RESTRICTED_PREFIX, settings.MASTER_DOMAIN),
            'System Aliases': settings.SYSTEM_ALIASES,
            'Admins': settings.ADMINS,
            'System Owner': settings.SYSTEM_OWNER
        })
