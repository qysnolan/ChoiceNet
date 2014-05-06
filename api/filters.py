from accounts.models import User
from service.models import Service
from choiceNet.models import Invoice
from rest_framework import filters
import django_filters


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_type='icontains')
    last_name = django_filters.CharFilter(lookup_type='icontains')
    username = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', ]


class ServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')
    service_input = django_filters.CharFilter(lookup_type='icontains')
    service_output = django_filters.CharFilter(lookup_type='icontains')
    pre_requirements = django_filters.CharFilter(lookup_type='icontains')
    
    class Meta:
        model = Service
        fields = ['name', 'description', 'date_created', 'date_used',
                  'date_modified', 'service_id', 'service_type',
                  'service_bandwidth', 'service_latency', 'service_cost',
                  'service_listings']


class InvoiceFilter(django_filters.FilterSet):
    number = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Invoice
        fields = ['number', ]