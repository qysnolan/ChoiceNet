from django.contrib.auth.forms import AuthenticationForm
from django.forms import forms
from django import forms as old_form

from accounts.models import User
from choiceNet import widgets


class AuthenticationForm(AuthenticationForm, forms.Form):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        self.error_messages["invalid_login"] = "Please enter a valid email " \
                                               "and password."

        self.fields["username"].widget = widgets.EmailInput()
        self.fields["password"].widget = widgets.PasswordInput()

    def clean_username(self):
        return self.cleaned_data["username"].lower()


class UserForm(old_form.Form):

    username = old_form.EmailField(required=True)
    first_name = old_form.CharField(required=True)
    last_name = old_form.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.all()

        for user in users:
            if user.username == username:
                raise forms.ValidationError("Username has already exists!")

        return username
