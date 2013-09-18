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

    email_address = old_form.EmailField(required=True,
                                        label='Your e-mail address')
    confirm_email_address = \
        old_form.EmailField(required=True, label='Confirm your e-mail address')
    first_name = old_form.CharField(required=True)
    last_name = old_form.CharField(required=True)
    password = old_form.CharField(widget=old_form.PasswordInput(),
                                  required=True, label='Your password')
    confirm_password = old_form.CharField(widget=old_form.PasswordInput(),
                                          required=True,
                                          label='Confirm your password')

    def clean_email_address(self):
        username = self.cleaned_data['email_address']
        users = User.objects.all()

        if username != self.data['confirm_email_address']:
            raise forms.ValidationError("Emails are not same!")

        for user in users:
            if user.username == username:
                raise forms.ValidationError("Username has already exists!")

        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        if password != self.data['confirm_password']:
            raise forms.ValidationError("Passwords are not same!")

        return password

    def save(self):
        from accounts.models import User
        import datetime

        User.objects.create(username=self.cleaned_data['email_address'],
                            first_name=self.cleaned_data['first_name'],
                            last_name=self.cleaned_data['last_name'],
                            isSuper=False,
                            accountType="user",
                            is_active=True,
                            date_joined=datetime.datetime.now(),
                            is_staff=False)

        user = User.objects.get(username=self.cleaned_data['email_address'])
        user.set_password(self.cleaned_data['password'])
        user.save()
