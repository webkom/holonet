from rest_framework.response import Response
from rest_framework.views import APIView

from holonet.interfaces.storage_backend import StorageBackend
from holonet.storage.backend import retrieve_history


class EmailStorageView(APIView):

    def get(self, request):
        emails = retrieve_history(None, None)
        return Response(map(lambda message: message.as_dict(), emails))


class EmailStorageTypesView(APIView):

    def get(self, request):
        return Response(StorageBackend.MESSAGE_TYPES_LIST)
