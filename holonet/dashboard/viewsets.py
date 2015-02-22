# -*- coding: utf8 -*-

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .elasticsearch_query import graph_query, processed_query
from .serializers import GraphRequestSerializer, ProcessedRequestSerializer


class GraphViewSet(ViewSet):

    @list_route(methods=['get', 'post'])
    def load(self, request, *args, **kwargs):

        serializer = GraphRequestSerializer(data=request.data, many=False)
        serializer.is_valid()

        types = []

        if serializer.data['spam']:
            types.append('spam')
        if serializer.data['blacklisted']:
            types.append('blacklisted')
        if serializer.data['bounce']:
            types.append('bounce')

        elasticsearch_data = graph_query(types, serializer.data['time_from'],
                                         serializer.data['time_to'], serializer.data['query'])

        return Response(elasticsearch_data)


class ProcessedViewSet(ViewSet):

    @list_route(methods=['get', 'post'])
    def load(self, request, *args, **kwargs):

        serializer = ProcessedRequestSerializer(data=request.data, many=False)
        serializer.is_valid()

        elasticsearch_data = processed_query(serializer.data['time_from'],
                                             serializer.data['time_to'])

        return Response(elasticsearch_data)
