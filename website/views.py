from django.http import HttpResponse
from django.shortcuts import render_to_response
from paypal.standard.forms import PayPalPaymentsForm
from django.core.urlresolvers import reverse
from django.conf import settings


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
        "return_url": "http://localhost:8000/hello/",
        "cancel_return": "http://localhost:8000/hello/",
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox()}
    return render_to_response("payment.html", context)

