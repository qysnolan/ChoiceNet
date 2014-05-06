from rest_framework import serializers
from rest_framework.fields import Field
from accounts.models import User
from service.models import Service
from choiceNet.models import Invoice
from . import fields


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User

        fields = ('url', 'id', 'username', 'first_name', 'last_name',
                  'is_active', 'last_login', 'date_joined')


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Service

        fields = ('url', 'id', 'name', 'owner', 'description', 'picture',
                  'date_created', 'date_used', 'date_modified', 'service_id',
                  'service_type', 'hosted_node_id', 'end_point1_id',
                  'end_point1_ip', 'end_point2_id', 'end_point2_ip',
                  'service_bandwidth', 'service_latency', 'service_cost',
                  'controller_id', 'controller_ip', 'service_listings')


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Invoice

        fields = ('url', 'id', 'date_created', 'service', 'buyer', 'amount',
                  'is_paid', 'is_active', 'number', )