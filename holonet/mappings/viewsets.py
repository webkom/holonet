# -*- coding: utf8 -*-

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from .serializers import MailingListSerializer, MailingListRetriveSerializer,\
    MailingListRecipientSerializer, RecipientSerializer
from .models import MailingList, Recipient


class MailingListViewSet(viewsets.ModelViewSet):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = MailingList.objects.all()
        mailing_list = get_object_or_404(queryset, pk=pk)
        serializer = MailingListRetriveSerializer(mailing_list)
        return Response(serializer.data)

    @detail_route(methods=['patch'])
    def recipients(self, request, *args, **kwargs):
        mailing_list = self.get_object()
        serializer = MailingListRecipientSerializer(mailing_list, data=request.DATA,
                                                    files=request.FILES, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            self.pre_save(serializer.object)
        except ValidationError as err:
            return Response(err.message_dict, status=status.HTTP_400_BAD_REQUEST)

        self.object = serializer.save(force_update=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    permission_classes = (IsAuthenticated, )
