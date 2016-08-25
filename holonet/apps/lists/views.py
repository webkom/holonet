from rest_framework import filters, viewsets

from .models import Domain, List, ListMember, RestrictedList
from .serializers import (DomainSerializer, ListMemberSerializer, ListSerializer,
                          RestrictedListSerializer)


class DomainViewSet(viewsets.ModelViewSet):

    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('remote_identifier', )


class ListViewSet(viewsets.ModelViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('remote_identifier', )


class RestrictedListViewSet(viewsets.ModelViewSet):

    queryset = RestrictedList.objects.all()
    serializer_class = RestrictedListSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('remote_identifier', )


class ListMemberViewSet(viewsets.ModelViewSet):

    queryset = ListMember.objects.all()
    serializer_class = ListMemberSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('remote_identifier', )
