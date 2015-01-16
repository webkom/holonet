# -*- coding: utf8 -*-

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import list_route

from django.conf import settings
from django.utils.module_loading import import_string
from django.shortcuts import Http404

from holonet.status.serializers import StatusSerializer
from holonet.status import BaseStatusClass


class StatusViewSet(ViewSet):

    @list_route(methods=['get'])
    def types(self, request):
        return Response(BaseStatusClass.STATUSES)

    def list(self, request, *args, **kwargs):
        status_classes = settings.STATUS_CLASSES
        statuses = []
        for status_class in status_classes:
            class_instance = import_string(status_class)()
            statuses.append(class_instance)

        serializer = StatusSerializer(data=statuses, many=True)
        serializer.is_valid()

        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        status_classes = settings.STATUS_CLASSES
        for status_class in status_classes:
            class_instance = import_string(status_class)()
            if class_instance.name == pk:
                serializer = StatusSerializer(class_instance)
                return Response(serializer.data)

        raise Http404('Could not find a status named %s' % pk)
