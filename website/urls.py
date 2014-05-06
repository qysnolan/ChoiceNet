from django.conf.urls import patterns, include, url
from django.contrib import admin

from website.views import *
from accounts.views import *
from choiceNet.views import *
from service.views import *
from accounts.authViews import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

handler401 = 'choiceNet.views.error_401'
handler403 = 'choiceNet.views.error_403'
handler404 = 'choiceNet.views.error_404'
handler500 = 'choiceNet.views.error_500'
handler502 = 'choiceNet.views.error_502'
handler504 = 'choiceNet.views.error_504'

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
    url(r'^forget_password/$', forget_password, name="forget_password"),
    url(r'^settings/$', account_settings, name="settings"),
    url(r'^orders/$', orders, name="orders"),
    url(r'^products/$', products_list, name="products_list"),
    url(r'^edit/service/(?P<serviceId>\d+)/$', user_help, name="edit_service"),
    url(r'^add/service/$', AddService, name="add_service"),

    # Shopping part
    url(r'^services', ServicesList, name="services"),
    url(r'^paypal/payment/service/(?P<serviceId>\d+)/'
        r'(?P<payStatus>\d+)/(?P<csrf>\w+)/(?P<date_created>\w+)/$',
        ServicesPayment, name="service_payment"),
    url(r'^pay_with_balance/service/$', ServicePayWithBalance,
        name="pay_with_balance"),

    # Balance related
    url(r'^add_balance', AddBalance, name="add_balance"),
    url(r'^paypal/payment/balance/(?P<amount>\d+)/'
        r'(?P<payStatus>\d+)/(?P<csrf>\w+)/(?P<date_created>\w+)/$',
        BalancePayment, name="balance_payment"),

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

    # Error pages
    url(r'^401/$', error_401, name="error_401"),
    url(r'^403/$', error_403, name="error_403"),
    url(r'^404/$', error_404, name="error_404"),
    url(r'^500/$', error_500, name="error_500"),
    url(r"^502/$", error_502, name="error_502"),
    url(r"^504/$", error_504, name="error_504"),
    url(r"^maintenance/$", maintenance, name="maintenance"),

    # Interact with Client App
    url(r'^client/key/exchange', KeyExchange, name="key_exchange"),
    url(r'^client/request/new/session', NewSession,
        name="request_new_session"),
    url(r'^client/request/service', RequestService, name="request_service"),
    url(r'^client/pay/order', PayOrder, name="pay_order"),
    url(r'^client/request/refund', RequestRefund, name="request_refund"),
    url(r'^auth/login/$', login, name="auth_login"),
)
