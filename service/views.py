from django.conf import settings
from django.core.urlresolvers import reverse

from choiceNet.functions import render_with_user
from paypal.standard.forms import PayPalPaymentsForm


def ServicesList(request):

    post = request.POST
    try:
        searchValue = post["searchValue"]
    except:
        searchValue = " "
    searchValue = searchValue.strip()
    url = 'api/services?search=' + searchValue

    return render_with_user(request, 'services/index.html',
                            {'searchValue': searchValue, 'url': url})


def ServicesPayment(request, serviceId, csrf):

    from service.models import Service

    service = Service.objects.all().get(id=int(serviceId))

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": service.cost,
        "item_name": service.name,
        "invoice": "unique-invoice-id",
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": "/paypal/payment/succeeded/service/" + serviceId,
        "cancel_return": "/paypal/payment/failed/service/" + serviceId,
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox(), "service": service}
    return render_with_user(request, "paypal/payment.html", context)