from django.conf import settings
from django.core.urlresolvers import reverse

from choiceNet.functions import render_with_user
from paypal.standard.forms import PayPalPaymentsForm


def ServicesList(request):

    post = request.POST
    try:
        searchValue = post["searchValue"]
    except:
        searchValue = ""
    searchValue = searchValue.strip()
    url = 'api/services?search=' + searchValue

    return render_with_user(request, 'services/index.html',
                            {'searchValue': searchValue, 'url': url})


def ServicesPayment(request):

    from service.models import Service

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "1.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "/services/",
        "cancel_return": "/services/",
    }

    service = Service.objects.get(id=request.POST["serviceId"])
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox(), "service": service}
    return render_with_user(request, "paypal/payment.html", context)