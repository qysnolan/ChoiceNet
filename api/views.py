from accounts.models import User
from service.models import Service
from serializers import UserSerializer, ServiceSerializer
from rest_framework import mixins, viewsets
from .filters import UserFilter, ServiceFilter


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.none()

    serializer_class = UserSerializer
    search_fields = ('username', 'first_name', 'last_name', 'accountType')
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
    search_fields = ('name', 'service_input', 'service_output',
                     'pre_requirements')
    filter_class = ServiceFilter

    def get_queryset(self):
        services = Service.objects.all()

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
            if column == 'cost':
                queryset = queryset.order_by('cost')
            if column == '-cost':
                queryset = queryset.order_by('-cost')

        return queryset