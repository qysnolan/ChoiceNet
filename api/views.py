from accounts.models import User
from serializers import UserSerializer
from rest_framework import mixins, viewsets
from .filters import UserFilter


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.none()

    serializer_class = UserSerializer
    search_fields = ("first_name", "last_name", "departments__name")
    filter_class = UserFilter

    def get_queryset(self):
        users = User.objects.none()

        user = self.request.user

        if user.isSuper:
            users = User.objects.has_super(user)
        elif user.hasPermission('teacher.all.delete'):
            users = User.objects.in_schools(user.schools.all()). \
                has_no_permissions("teacher.all.create", "teacher.all.delete",
                "reports", "forms").is_not_super()
        elif user.hasPermission('teacher.department.delete'):
            users = User.teachers.in_schools(user.schools.all()). \
                in_departments(user.departments.all()).is_active().\
                has_no_permissions("teacher.all.create", "teacher.all.delete",
                "reports", "forms").is_not_super()

        users = users | User.active.filter(id=user.id)

        return users.distinct().order_by("last_name", "first_name")

    def filter_queryset(self, queryset):
        queryset = super(UserViewSet, self).filter_queryset(queryset)

        params = self.request.GET

        if "ordering" in params:
            column = params["ordering"]
            if column == "name":
                queryset = queryset.order_by('last_name', 'first_name')
            if column == "-name":
                queryset = queryset.order_by('-last_name', 'first_name')
            if column == "department_name":
                queryset = queryset.order_by("departments__name", "username").distinct("departments__name", "username")
            if column == "-department_name":
                queryset = queryset.order_by("-departments__name", "-username").distinct("departments__name", "username")
            if column == "last_login":
                queryset = queryset.order_by("last_login")
            if column == "-last_login":
                queryset = queryset.order_by("-last_login")

        if "department" in params:
            queryset = queryset.filter(departments__name__icontains=params["department"])

        if "school" in params:
            queryset = queryset.filter(schools__name__icontains=params["school"])

        return queryset

