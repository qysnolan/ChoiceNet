from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import models
from .models import User


class UserAdmin(UserAdmin):
    form = models.ModelForm
    add_form = models.ModelForm

    fieldsets = ()
    add_fieldsets = ()

    change_form_template = None
    add_form_template = None

    list_display = ("username", "first_name", "last_name", "isSuper")
    list_filter = ("isSuper", "is_staff", "is_superuser", "is_active")

    search_fields = ("username", "first_name", "last_name", )


admin.site.register(User, UserAdmin)

# from django.contrib import admin
# from accounts.models import User
#
# admin.site.register(User)