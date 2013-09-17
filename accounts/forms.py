from django.contrib.auth.forms import AuthenticationForm
from django.forms import forms
from django.forms import widgets


class AuthenticationForm(AuthenticationForm, forms.Form):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        self.error_messages["invalid_login"] = "Please enter a valid email and password."

        self.fields["username"].widget = widgets.TextInput()
        self.fields["password"].widget = widgets.PasswordInput()

    def clean_username(self):
        return self.cleaned_data["username"].lower()
