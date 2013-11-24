from django.db import models


class CustomManager(models.Manager):

    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)


class Invoice(models.Model):

    date_created = models.DateTimeField()
    buyer = models.ForeignKey("accounts.User", blank=False, null=False,
                              related_name='invoice_buyer')
    service = models.ForeignKey("service.Service", blank=False, null=False,
                                related_name='invoice_service')
    number = models.CharField(max_length=255, unique=True, blank=False,
                              null=False)
    amount = models.IntegerField(max_length=1000, blank=True, null=True)
    is_paid = models.BooleanField(default=False, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["date_created", "number"]

    def __unicode__(self):
        return u'%s' % self.number