from django.contrib.auth.models import BaseUserManager
from django.db.models.query import QuerySet
from teacher_evaluator.teacherEval.models import CustomManager


class UserManager(BaseUserManager, CustomManager):
    pass


class UserObjectManager(UserManager):

    def get_query_set(self):
        return UserQuerySet(self.model)


class UserQuerySet(QuerySet):

    def is_active(self):
        return self.filter(is_active=True)