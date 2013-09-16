from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from accounts.managers import UserObjectManager


# Users model
class User(AbstractBaseUser, PermissionsMixin):

    username = models.EmailField(
        "Email", max_length=70, unique=True,
        error_messages={"unique": "A user with this email already exists."})
    first_name = models.CharField("First Name", max_length=40)
    last_name = models.CharField("Last Name", max_length=40)
    # secretQuestion = models.OneToOneField("choiceNet.SecretQuestion",
    #                                       blank=True, null=True)
    isSuper = models.BooleanField(default=False)
    accountType = models.CharField("Account Type", max_length=255, blank=True,
                                   null=True)
    is_active = models.BooleanField(verbose_name="active", default=True)
    date_joined = models.DateTimeField()

    is_staff = models.BooleanField(
        "staff status", default=False,
        help_text="Designates whether the user can log into this admin site.")

    objects = UserObjectManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = (
        "first_name",
        "last_name",
    )

    class Meta:
        ordering = ["last_name", "first_name"]

    def __unicode__(self):
        return u'%s' % (self.fullname())

    def fullname(self):
        if not hasattr(self, "_fullname"):
            self._fullname = u'%s, %s' % (self.last_name, self.first_name)

        return self._fullname