from rest_framework import serializers
from rest_framework.fields import Field
from accounts.models import User
from . import fields


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User

        fields = ("url", "id", "username", "first_name", "last_name",
                  "is_active", "last_login", "date_joined")
