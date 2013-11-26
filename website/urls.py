from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.views import *
from accounts.views import *
from choiceNet.views import *
from service.views import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',

    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # Home page
    url(r'^$', welcome, name="welcome"),
    url(r'^home/', home, name="home"),

    # For user login and related
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', logout),
    url(r'^sign_up/$', create_account, name="sign_up"),
    url(r'^forget_password/', forget_password, name="forget_password"),
    url(r'^settings/$', account_settings, name="settings"),
    url(r'^orders/$', orders, name="orders"),
    url(r'^products/$', products_list, name="products_list"),

    # Shopping part
    url(r'^services', ServicesList, name="services"),
    url(r'^paypal/payment/service/(?P<serviceId>\d+)/'
        r'(?P<payStatus>\d+)/(?P<csrf>\w+)/(?P<date_created>\w+)/$',
        ServicesPayment, name="service_payment"),

    # Just for testing
    url(r'^hello/', hello),

    # PayPal
    url(r'^you/cant/guess/this/url/', include('paypal.standard.ipn.urls')),

    # Help
    url(r'^help/', user_help, name="help"),

    # REST framework
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r"^api/", include("api.urls"), name="api_base"),

    #error pages
    url(r'^401/$', error_401, name="error_401"),
    url(r'^403/$', error_403, name="error_403"),
    url(r'^404/$', error_404, name="error_404"),
    url(r'^500/$', error_500, name="error_500"),
    url(r"^502/$", error_502, name="error_502"),
    url(r"^504/$", error_504, name="error_504"),
    url(r"^maintenance/$", maintenance, name="maintenance"),
)
