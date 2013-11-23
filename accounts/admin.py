from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import models, ModelForm

from .models import User


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdmin(UserAdmin):
    form = models.ModelForm
    add_form = UserCreationForm

    fieldsets = ()
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('username', 'first_name', 'last_name', 'password',
                   'isSuper', 'accountType', 'is_active', 'date_joined',
                   'is_staff')}),
    )

    change_form_template = None
    add_form_template = None

    list_display = ("username", "first_name", "last_name", "accountType",
                    "date_joined", "last_login")
    list_filter = ("isSuper", "is_staff", "is_superuser", "is_active")
    search_fields = ("username", "first_name", "last_name", )


admin.site.register(User, UserAdmin)