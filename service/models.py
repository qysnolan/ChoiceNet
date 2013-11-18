from django.db import models


# class CustomManager(models.Manager):
#
#     def __getattr__(self, name):
#         return getattr(self.get_query_set(), name)


class Service(models.Model):

    process_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    service_type = models.ManyToManyField("service.ServiceType", blank=True,
                                          null=True, related_name='+')
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    service_input = models.CharField(max_length=200, blank=True, null=True)
    service_output = models.CharField(max_length=200, blank=True, null=True)
    pre_requirements = models.CharField(max_length=200, blank=True, null=True)
    max_bandwidth = models.DecimalField(max_digits=50, decimal_places=9)
    min_bandwidth = models.DecimalField(max_digits=50, decimal_places=9)
    delay = models.TimeField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_used = models.DateTimeField()

    class Meta:
        ordering = ["name", "process_id"]


class ServiceType(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False)
    category = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["name"]