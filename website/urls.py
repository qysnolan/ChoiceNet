from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.views import *
from accounts.views import *
from choiceNet.views import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # For user login and related
    url(r'^$', home),
    url(r'^login/$', LoginView.as_view(), name="login"),

    # Shopping part
    url(r'^home/', home, name="home"),

    # Just for testing
    url(r'^hello/', hello),

    # PayPal
    url(r'^you/cant/guess/this/url/', include('paypal.standard.ipn.urls')),
)
