from rest_framework import viewsets

from holonet.restricted.models import RestrictedMapping
from holonet.restricted.serializers import (RestrictedMappingCreateAndUpdateSerializer,
                                            RestrictedMappingSerializer)


class RestrictedMappingViewSet(viewsets.ModelViewSet):
    lookup_field = 'tag'
    queryset = RestrictedMapping.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return RestrictedMappingCreateAndUpdateSerializer
        return RestrictedMappingSerializer
