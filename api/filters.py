from accounts.models import User
from rest_framework import filters
import django_filters


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_type="icontains")
    last_name = django_filters.CharFilter(lookup_type="icontains")
    username = django_filters.CharFilter(lookup_type="icontains")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", ]



