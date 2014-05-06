from accounts.models import User
from service.models import Service
from choiceNet.models import Invoice
from serializers import UserSerializer, ServiceSerializer, InvoiceSerializer
from rest_framework import mixins, viewsets
from .filters import UserFilter, ServiceFilter, InvoiceFilter


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.none()

    serializer_class = UserSerializer
    search_fields = ('username', 'owner', 'first_name', 'last_name',
                     'accountType')
    filter_class = UserFilter

    def get_queryset(self):
        users = User.objects.all()

        return users.order_by('last_name', 'first_name')

    def filter_queryset(self, queryset):
        queryset = super(UserViewSet, self).filter_queryset(queryset)

        params = self.request.GET

        if 'ordering' in params:
            column = params['ordering']
            if column == 'name':
                queryset = queryset.order_by('last_name', 'first_name')
            if column == '-name':
                queryset = queryset.order_by('-last_name', 'first_name')
            if column == 'last_login':
                queryset = queryset.order_by('last_login')
            if column == '-last_login':
                queryset = queryset.order_by('-last_login')

        return queryset


class ServiceViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.none()

    serializer_class = ServiceSerializer
    search_fields = ('name', 'description', )
    filter_class = ServiceFilter

    def get_queryset(self):
        services = Service.objects.all().exclude(id=56)

        return services.order_by('name', )

    def filter_queryset(self, queryset):
        queryset = super(ServiceViewSet, self).filter_queryset(queryset)

        params = self.request.GET

        if 'ordering' in params:
            column = params['ordering']
            if column == 'name':
                queryset = queryset.order_by('name', )
            if column == '-name':
                queryset = queryset.order_by('-name', )
            if column == 'service_cost':
                queryset = queryset.order_by('service_cost')
            if column == '-service_cost':
                queryset = queryset.order_by('-service_cost')
            if column == 'service_bandwidth':
                queryset = queryset.order_by('service_bandwidth')
            if column == '-service_bandwidth':
                queryset = queryset.order_by('-service_bandwidth')
            if column == 'service_latency':
                queryset = queryset.order_by('service_latency')
            if column == '-service_latency':
                queryset = queryset.order_by('-service_latency')

        return queryset


class InvoiceViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Invoice.objects.none()

    serializer_class = InvoiceSerializer
    search_fields = ('number', )
    filter_class = InvoiceFilter

    def get_queryset(self):
        invoices = Invoice.objects.all()

        return invoices.order_by('number', )

    def filter_queryset(self, queryset):
        queryset = super(InvoiceViewSet, self).filter_queryset(queryset)

        params = self.request.GET

        if 'ordering' in params:
            column = params['ordering']
            if column == 'number':
                queryset = queryset.order_by('number', )
            if column == '-number':
                queryset = queryset.order_by('-number', )
            if column == 'date_created':
                queryset = queryset.order_by('codate_createdst')
            if column == '-date_created':
                queryset = queryset.order_by('-date_created')

        return queryset