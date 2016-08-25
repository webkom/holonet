from rest_framework import serializers

from .models import Domain, List, ListMember, RestrictedList


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = ('pk', 'remote_identifier', 'domain', 'base_url', 'description')


class SimpleDomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = ('domain', )


class ListSerializer(serializers.ModelSerializer):

    domains = SimpleDomainSerializer(many=True)

    class Meta:
        model = List
        fields = ('pk', 'remote_identifier', 'list_name', 'description', 'domains')


class RestrictedListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestrictedList
        fields = ('pk', 'remote_identifier', 'token', 'from_address', 'timeout')


class ListMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListMember
        fields = ('pk', 'remote_identifier', 'user', 'email', 'active')
