from django.db import models


class CustomManager(models.Manager):

    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)


class Service(CustomManager):

    process_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=False, null=False)
    service_type = models.ManyToManyField("services.ServiceType", blank=True,
                                          null=True, related_name='+')
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    service_input = models.CharField(blank=True, null=True)
    service_output = models.CharField(blank=True, null=True)
    pre_requirements = models.CharField(blank=True, null=True)
    max_bandwidth = models.DecimalField(max_digits=50, decimal_places=9)
    min_bandwidth = models.DecimalField(max_digits=50, decimal_places=9)
    delay = models.TimeField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_used = models.DateTimeField()

    class Meta:
        ordering = ["name", "process_id"]


class ServiceType(CustomManager):

    name = models.CharField(blank=False, null=False)
    category = models.CharField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)

