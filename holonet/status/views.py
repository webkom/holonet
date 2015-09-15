from rest_framework.response import Response
from rest_framework.views import APIView

from holonet.interfaces.status_check import StatusCheck
from holonet.status import manager
from holonet.status.serializers import StatusSerializer


class StatusView(APIView):
    def get(self, request):
        status_classes = manager.keys()
        statuses = []
        for status_class in status_classes:
            status_instance = manager.get(status_class)()
            statuses.append(status_instance)

        serializer = StatusSerializer(data=statuses, many=True)
        serializer.is_valid()

        return Response(serializer.data)


class StatusTypesView(APIView):
    def get(self, request):
        return Response(StatusCheck.STATUSES)
