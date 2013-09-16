from django.conf.urls import *
from website.views import *

urlpatterns = patterns('paypal.standard.ipn.views',            
    url(r'^$', 'ipn', name="paypal-ipn"),
    url(r'^pay/', view_that_asks_for_money),
)