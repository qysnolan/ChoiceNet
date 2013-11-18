from rest_framework import serializers
from rest_framework.fields import Field
from accounts.models import User
from . import fields


class UserSerializer(serializers.HyperlinkedModelSerializer):
    schools = fields.HyperlinkedRelatedField(
        source="schools", many=True, view_name="school-detail")
    schools_names = serializers.RelatedField(source="schools", many=True)
    departments = serializers.HyperlinkedRelatedField(
        source="departments", many=True, view_name="department-detail")
    departments_names = serializers.RelatedField(
        source="departments", many=True)
    super = serializers.HyperlinkedRelatedField(
        source="super", view_name="user-detail")

    class Meta:
        model = User

        fields = ("url", "id", "username", "first_name", "last_name",
                  "departments",  "departments_names", "schools",
                  "schools_names", "is_active", "last_login", "date_joined")
