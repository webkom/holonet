from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import StoredEmailFilterSerializer

from.backend import retrieve_history


class EmailStoreViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        emails = retrieve_history(None, None)
        return Response(map(lambda message: message.as_dict(), emails))

    def create(self, request, *args, **kwargs):
        serializer = StoredEmailFilterSerializer(data=request.data)
        if serializer.is_valid():
            emails = retrieve_history(
                serializer.validated_data['time_from'],
                serializer.validated_data['time_to'],
                serializer.validated_data['filter'],
                serializer.validated_data['search_query'],
            )
            return Response(map(lambda message: message.as_dict(), emails))
        return Response([])
