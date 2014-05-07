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


class EditServiceForm(forms.Form):

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

    def __init__(self, service, *args, **kwargs):
        self.service = service
        super(EditServiceForm, self).__init__(*args, **kwargs)

        self.fields["name"].initial = str(service.name)
        self.fields["picture"].initial = str(service.picture)
        self.fields["description"].initial = str(service.description)
        self.fields["service_id"].initial = str(service.service_id)
        self.fields["service_type"].initial = str(service.service_type)
        self.fields["hosted_node_id"].initial = str(service.hosted_node_id)
        self.fields["end_point1_id"].initial = str(service.end_point1_id)
        self.fields["end_point1_ip"].initial = str(service.end_point1_ip)
        self.fields["end_point2_id"].initial = str(service.end_point2_id)
        self.fields["end_point2_ip"].initial = str(service.end_point2_ip)
        self.fields["service_bandwidth"].initial = \
            str(service.service_bandwidth)
        self.fields["service_latency"].initial = str(service.service_latency)
        self.fields["service_cost"].initial = str(service.service_cost)
        self.fields["controller_id"].initial = str(service.controller_id)
        self.fields["controller_ip"].initial = str(service.controller_ip)
        self.fields["service_listings"].initial = str(service.service_listings)

    def save(self):

        import datetime

        service = self.service

        service.name = self.cleaned_data['name']
        service.picture = self.cleaned_data['picture']
        service.description = self.cleaned_data['description']
        service.service_id = self.cleaned_data['service_id']
        service.service_type = self.cleaned_data['service_type']
        service.hosted_node_id = self.cleaned_data['hosted_node_id']
        service.end_point1_id = self.cleaned_data['end_point1_id']
        service.end_point1_ip = self.cleaned_data['end_point1_ip']
        service.end_point2_id = self.cleaned_data['end_point2_id']
        service.end_point2_ip = self.cleaned_data['end_point2_ip']
        service.service_bandwidth = self.cleaned_data['service_bandwidth']
        service.service_latency = self.cleaned_data['service_latency']
        service.service_cost = self.cleaned_data['service_cost']
        service.controller_id = self.cleaned_data['controller_id']
        service.controller_ip = self.cleaned_data['controller_ip']
        service.service_listings = self.cleaned_data['service_listings']
        service.date_modified = datetime.datetime.now()

        service.save()
