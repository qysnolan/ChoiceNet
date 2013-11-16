from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings

from paypal.standard.forms import PayPalPaymentsForm
from choiceNet.functions import render_with_user


def hello(request):
    return HttpResponse("Hello world")


def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "1.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "http://0.0.0.0:8008/hello/",
        "cancel_return": "http://0.0.0.0:8008/hello/",
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox(), "productID": request.POST["productID"]}
    return render_with_user(request, "paypal/payment.html", context)

