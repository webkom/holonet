from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import base_url, reverse


class BrowsableAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        url = base_url(request)

        urls = {
            'api:browse': reverse('api:browse', url),

            'api:status:list': reverse('api:status:list', url),
            'api:status:types': reverse('api:status:types', url),

            'api:storage:list': reverse('api:storage:list', url),
            'api:storage:types': reverse('api:storage:types', url),
        }

        return Response(sorted(urls.values()))
