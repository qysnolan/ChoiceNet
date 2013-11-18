from accounts.models import User
from serializers import UserSerializer
from rest_framework import mixins, viewsets
from .filters import UserFilter


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.none()

    serializer_class = UserSerializer
    search_fields = ('username', "first_name", "last_name", 'accountType')
    filter_class = UserFilter

    def get_queryset(self):
        users = User.objects.all()

        return users.order_by("last_name", "first_name")

    def filter_queryset(self, queryset):
        queryset = super(UserViewSet, self).filter_queryset(queryset)

        params = self.request.GET

        if "ordering" in params:
            column = params["ordering"]
            if column == "name":
                queryset = queryset.order_by('last_name', 'first_name')
            if column == "-name":
                queryset = queryset.order_by('-last_name', 'first_name')
            if column == "last_login":
                queryset = queryset.order_by("last_login")
            if column == "-last_login":
                queryset = queryset.order_by("-last_login")

        return queryset

