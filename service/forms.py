from django import forms
from choiceNet import widgets


class ServiceForm(forms.Form):

    name = forms.CharField(required=False, widget=widgets.TextInput())
    picture = forms.FileField(required=False)
    description = forms.CharField(required=False, widget=widgets.TextInput())
    service_id = forms.CharField(required=True, widget=widgets.TextInput())
    service_type = forms.CharField(required=False, widget=widgets.TextInput())
    hosted_node_id = forms.CharField(required=False,
                                     widget=widgets.TextInput())
    end_point1_id = forms.CharField(required=False, widget=widgets.TextInput())
    end_point1_ip = forms.CharField(required=False, widget=widgets.TextInput())
    end_point2_id = forms.CharField(required=False, widget=widgets.TextInput())
    end_point2_ip = forms.CharField(required=False, widget=widgets.TextInput())
    service_bandwidth = forms.DecimalField(widget=widgets.NumberInput())
    service_latency = forms.DecimalField(widget=widgets.NumberInput())
    service_cost = forms.DecimalField(required=True,
                                      widget=widgets.NumberInput())
    controller_id = forms.CharField(required=False, widget=widgets.TextInput())
    controller_ip = forms.CharField(required=False, widget=widgets.TextInput())
    service_listings = forms.CharField(required=False,
                                       widget=widgets.TextInput())

    def save(self, user):
        from .models import Service
        import datetime

        s = Service.objects.create(name=self.cleaned_data['name'],
                                   owner=user,
                                   picture=self.cleaned_data['picture'],
                                   description=self.cleaned_data['description'],
                                   service_id=self.cleaned_data['service_id'],
                                   service_type=self.cleaned_data['service_type'],
                                   hosted_node_id=self.cleaned_data['hosted_node_id'],
                                   end_point1_id=self.cleaned_data['end_point1_id'],
                                   end_point1_ip=self.cleaned_data['end_point1_ip'],
                                   end_point2_id=self.cleaned_data['end_point2_id'],
                                   end_point2_ip=self.cleaned_data['end_point2_ip'],
                                   service_bandwidth=self.cleaned_data['service_bandwidth'],
                                   service_latency=self.cleaned_data['service_latency'],
                                   service_cost=self.cleaned_data['service_cost'],
                                   controller_id=self.cleaned_data['controller_id'],
                                   controller_ip=self.cleaned_data['controller_ip'],
                                   service_listings=self.cleaned_data['service_listings'],
                                   date_created=datetime.datetime.now(),
                                   date_modified=datetime.datetime.now(),
                                   date_used=datetime.datetime.now(), )
        s.save()
