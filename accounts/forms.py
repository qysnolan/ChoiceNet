from django.contrib.auth.forms import AuthenticationForm
from django import forms

from accounts.models import User
from choiceNet import widgets


class AuthenticationForm(AuthenticationForm, forms.forms.Form):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        self.error_messages["invalid_login"] = "Please enter a valid email " \
                                               "and password."

        self.fields["username"].widget = widgets.EmailInput()
        self.fields["password"].widget = widgets.PasswordInput()

    def clean_username(self):
        return self.cleaned_data["username"].lower()


class UserForm(forms.Form):

    email_address = forms.EmailField(required=True,
                                     label='Your e-mail address')
    confirm_email_address = \
        forms.EmailField(required=True, label='Confirm your e-mail address')
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),
                               required=True, label='Your password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(),
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

        if len(password) <= 6:
            raise forms.ValidationError("Passwords is too short! "
                                        "At least 6 characters")

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


class SettingsForm(forms.Form):

    password = forms.CharField(widget=forms.PasswordInput(),
                               required=True,
                               label='Your current password (Required field)')
    email_address = forms.EmailField(required=False,
                                     label='Your new e-mail address')
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False, )
    new_password = forms.CharField(widget=forms.PasswordInput(),
                                   required=False, label='Your new password')
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(),
                                           required=False,
                                           label='Confirm your new password')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SettingsForm, self).__init__(*args, **kwargs)

        self.fields["password"].initial = None
        self.fields["email_address"].initial = str(user.username)
        self.fields["first_name"].initial = str(user.first_name)
        self.fields["last_name"].initial = str(user.last_name)
        # self.fields["new_password"].initial = None
        # self.fields["confirm_new_password"].initial = None

    def clean_email_address(self):
        username = self.cleaned_data['email_address']

        if username != self.user.username:
            users = User.objects.all()
            for user in users:
                if user.username == username:
                    raise forms.ValidationError("Username has already exists!")

        return username

    def clean_new_password(self):
        password = self.cleaned_data['new_password']

        if len(password) <= 6 & len(password) > 0:
            raise forms.ValidationError("Passwords is too short! "
                                        "At least 6 characters")

        if password != self.data['confirm_new_password']:
            raise forms.ValidationError("Passwords are not same!")

        return password

    def clean_password(self):
        old_password = self.data['password']

        if not self.user.check_password(old_password):
            raise forms.ValidationError("Your current password is wrong!")

        return old_password

    def save(self):
        current_user = self.user

        if current_user.check_password(self.data['password']):

            current_user.username = self.cleaned_data['email_address']
            current_user.first_name = self.cleaned_data['first_name']
            current_user.last_name = self.cleaned_data['last_name']
            current_user.save()

            if self.data['new_password']:
                current_user.set_password(self.cleaned_data['new_password'])
                current_user.save()
