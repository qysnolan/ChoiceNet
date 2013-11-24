from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def ServicesPayment(request, serviceId, csrf, payStatus, date_created):

    from service.models import Service
    from choiceNet.models import Invoice
    import datetime
    import time

    service = Service.objects.all().get(id=int(serviceId))
    user = request.user
    if date_created == "0":
        date_created = str(time.time())
    invoice_number = date_created + '-service-' + str(serviceId) + "-" \
                     + str(user.id)

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": service.cost,
        "item_name": service.name,
        "invoice": invoice_number,
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": settings.SITE_NAME + "/paypal/payment/service/"
                      + serviceId + "/1/" + csrf + "/" + date_created + "/",
        "cancel_return": settings.SITE_NAME + "/paypal/payment/service/"
                         + serviceId + "/0/" + csrf + "/" + date_created + "/",
    }

    if payStatus == "2":
        if len(Invoice.objects.all().filter(number=invoice_number)) > 0:
            payStatus = "3"
        else:
            dateTime = datetime.datetime.\
                fromtimestamp(float(date_created)/1000)
            i = Invoice.objects.create(date_created=dateTime, service=service,
                                       buyer=user, amount=service.cost,
                                       paid=False, number=invoice_number)
            i.save()
    if payStatus == "1":
        if len(Invoice.objects.all().filter(number=invoice_number)) == 0:
            payStatus = "3"
        else:
            i = Invoice.objects.all().get(number=invoice_number)
            i.paid = True
            i.save()
    if payStatus == "0":
        if len(Invoice.objects.all().filter(number=invoice_number)) == 0:
            payStatus = "3"
        else:
            i = Invoice.objects.all().get(number=invoice_number)
            i.paid = False
            i.save()

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox(), "service": service,
               "payStatus": payStatus}
    return render_with_user(request, "paypal/payment.html", context)