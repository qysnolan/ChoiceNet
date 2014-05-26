from django.db import models


# class CustomManager(models.Manager):
#
#     def __getattr__(self, name):
#         return getattr(self.get_query_set(), name)


class Service(models.Model):

    # process_id = models.IntegerField(blank=True, null=True)
    # service_type = models.ManyToManyField("service.ServiceType", blank=True,
    #                                       null=True, related_name='+')
    # cost = models.DecimalField(max_digits=20, decimal_places=2)
    # service_input = models.CharField(max_length=200, blank=True, null=True)
    # service_output = models.CharField(max_length=200, blank=True, null=True)
    # pre_requirements = models.CharField(max_length=200, blank=True,
    #                                     null=True)
    # max_bandwidth = models.DecimalField(max_digits=50, decimal_places=9,
    #                                     blank=True, null=True)
    # min_bandwidth = models.DecimalField(max_digits=50, decimal_places=9,
    #                                     blank=True, null=True)
    # delay = models.DecimalField(max_digits=50, decimal_places=3, blank=True,
    #                             null=True)

    name = models.CharField(max_length=200, blank=False, null=False)
    owner = models.ForeignKey("accounts.User", blank=True, null=True,
                              related_name='service_owner')
    description = models.CharField(max_length=3000, blank=True, null=True)
    picture = models.FileField(upload_to='pictures/%Y/%m/%d',
                               blank=True, null=True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)
    date_used = models.DateTimeField(blank=True, null=True)

    service_id = models.CharField(max_length=255, blank=False, null=False,
                                  default='0')
    service_type = models.CharField(max_length=255, blank=True, null=True)
    hosted_node_id = models.CharField(max_length=255, blank=True, null=True)
    end_point1_id = models.CharField(max_length=255, blank=True, null=True)
    end_point1_ip = models.CharField(max_length=255, blank=True, null=True)
    end_point2_id = models.CharField(max_length=255, blank=True, null=True)
    end_point2_ip = models.CharField(max_length=255, blank=True, null=True)
    service_bandwidth = models.DecimalField(max_digits=64, decimal_places=12,
                                            default=0.0)
    service_latency = models.DecimalField(max_digits=64, decimal_places=12,
                                          default=0.0)
    service_cost = models.DecimalField(max_digits=64, decimal_places=12,
                                       blank=False, null=False, default=0.0)
    controller_id = models.CharField(max_length=255, blank=True, null=True)
    controller_ip = models.CharField(max_length=255, blank=True, null=True)
    service_listings = models.CharField(max_length=1024, blank=True, null=True)
    # "request": user request refund; "approved": service provider approved
    # refund; "refunded": manager refunded to user
    refund_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["name", "service_id"]

    def __unicode__(self):
        return u'%s' % self.name


class ServiceType(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False)
    category = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return u'%s' % self.name


class ServiceOwner(models.Model):

    owner = models.ForeignKey("accounts.User", blank=True, null=True,
                              related_name='service_owner_owner')
    service = models.ForeignKey("service.Service", blank=True, null=True,
                                related_name='service_owner_service')
    share_cost = models.DecimalField(max_digits=64, decimal_places=12,
                                     blank=False, null=False, default=0.0)

    class Meta:
        ordering = ["owner"]

    def __unicode__(self):
        return u'%s' % self.owner