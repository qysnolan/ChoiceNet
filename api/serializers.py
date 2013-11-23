from rest_framework import serializers
from rest_framework.fields import Field
from accounts.models import User
from service.models import Service
from . import fields


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User

        fields = ('url', 'id', 'username', 'first_name', 'last_name',
                  'is_active', 'last_login', 'date_joined')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Service

        fields = ('url', 'id', 'name', 'owner', 'process_id', 'cost',
                  'service_input', 'service_output', 'pre_requirements',
                  'description', 'max_bandwidth', 'min_bandwidth', 'delay',
                  'picture', 'date_created', 'date_used', 'date_modified', )