from django.shortcuts import Http404
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from holonet.status import manager
from holonet.status.base import StatusCheck
from holonet.status.serializers import StatusSerializer


class StatusViewSet(ViewSet):

    @list_route(methods=['get'])
    def types(self, request):
        return Response(StatusCheck.STATUSES)

    def list(self, request, *args, **kwargs):
        status_classes = manager.keys()
        statuses = []
        for status_class in status_classes:
            status_instance = manager.get(status_class)()
            statuses.append(status_instance)

        serializer = StatusSerializer(data=statuses, many=True)
        serializer.is_valid()

        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        if pk in manager.keys():
            class_instance = manager.get(pk)()
            serializer = StatusSerializer(class_instance)
            return Response(serializer.data)

        raise Http404('Could not find a status named %s' % pk)
