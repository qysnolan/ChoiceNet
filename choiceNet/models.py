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
    # "request": user request refund; "approved": service provider approved
    # refund; "refunded": manager refunded to user
    refund_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["date_created", "number"]

    def __unicode__(self):
        return u'%s' % self.number


class Comment(models.Model):

    service = models.ForeignKey("service.Service", blank=False, null=False,
                                related_name="comment_service")
    user = models.ForeignKey("accounts.User", blank=False, null=False,
                             related_name='comment_user')
    rate = models.IntegerField(blank=False, null=False, default=3)
    comment = models.CharField(max_length=4096, blank=True, default="0",
                               null=True)
    created_date = models.DateTimeField(blank=False, null=False)
    is_provider = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_date", "user"]

    def __unicode__(self):
        return u'%s' % self.user


class Balance(models.Model):

    user = models.ForeignKey("accounts.User", blank=False, null=False,
                             related_name='balance_user')
    balance = models.DecimalField(max_digits=64, decimal_places=12, default=0,
                                  blank=True, null=True)

    class Meta:
        ordering = ["user"]

    def __unicode__(self):
        return u'%s' % self.user


class Income(models.Model):

    provider = models.ForeignKey("accounts.User", blank=False, null=False,
                                 related_name='income_user')
    income = models.DecimalField(max_digits=64, decimal_places=12, default=0,
                                 blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    withdraw_status = models.CharField(max_length=128, blank=True,
                                       default=None, null=True)
    withdraw_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["provider"]

    def __unicode__(self):
        return u'%s' % self.provider


class Session(models.Model):

    session = models.IntegerField(blank=False, default=0, null=False)
    user = models.ForeignKey("accounts.User", blank=True, null=True,
                             related_name='session_user')
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField(blank=False, null=False)
    is_login = models.BooleanField(default=False, blank=False, null=False)
    a = models.IntegerField(blank=False, default=0, null=False)
    q = models.IntegerField(blank=False, default=0, null=False)
    key = models.CharField(max_length=128, blank=True, default="0", null=True)

    class Meta:
        ordering = ["start_time", "user"]

    def __unicode__(self):
        return u'%s' % self.user