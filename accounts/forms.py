# from django import forms
# from django.forms import fields as django_fields
#
#
# class ActivateAccountForm(Form):
#
#     error_messages = {
#         "invalid_token": "The token you entered was not valid.",
#         "expired_token": "The token you entered has expired and is no longer valid.",
#     }
#
#     activation_token = django_fields.CharField(label="Activation token", widget=widgets.TextInput)
#
#     def clean_activation_token(self):
#         from django.utils import timezone
#         from teacher_evaluator.teacherEval.models import AccountActivationToken
#
#         value = self.cleaned_data.get("activation_token")
#
#         try:
#             token = AccountActivationToken.objects.get(token=value)
#         except AccountActivationToken.DoesNotExist:
#             raise forms.ValidationError(self.error_messages["invalid_token"])
#
#         if token.expires_on < timezone.now().date():
#             raise forms.ValidationError(self.error_messages["expired_token"])
#
#         return value
#
#     def get_token(self):
#         from teacher_evaluator.teacherEval.models import AccountActivationToken
#
#         value = self.cleaned_data.get("activation_token")
#
#         token = AccountActivationToken.objects.get(token=value)
#
#         return token
