from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.views import *
from accounts.views import *
from choiceNet.views import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',

    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # For user login and related
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', logout),
    url(r'^sign_up/$', create_account, name="sign_up"),
    url(r'^forget_password/', forget_password, name="forget_password"),
    url(r'^settings/$', account_settings, name="settings"),
    url(r'^orders/', orders, name="orders"),

    # Shopping part
    url(r'^$', home),
    url(r'^home/', home, name="home"),

    # Just for testing
    url(r'^hello/', hello),

    # PayPal
    url(r'^you/cant/guess/this/url/', include('paypal.standard.ipn.urls')),

    # Help
    url(r'^help/', user_help, name="help"),
)
