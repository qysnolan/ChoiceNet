from django import forms
from choiceNet import widgets


class CommentForm(forms.Form):

    rate = forms.IntegerField(required=True, widget=widgets.IntegerInput())
    comment = forms.CharField(required=False, widget=widgets.TextInput())

    def clean_rate(self):

        rate = self.cleaned_data['rate']
        if rate > 5 or rate < 0:
            raise forms.ValidationError("Rate 0 to 5!")

        return int(rate)

    def save(self, user, service):
        from .models import Comment
        import datetime

        c = Comment.objects.create(rate=self.cleaned_data['rate'],
                                   user=user,
                                   service=service,
                                   comment=self.cleaned_data['comment'],
                                   created_date=datetime.datetime.now(),
                                   is_provider=user.is_staff, )
        c.save()
