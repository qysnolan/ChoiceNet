from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from choiceNet.functions import render_with_user
from choiceNet.models import *
from service.models import Service
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


def AddService(request):

    from .forms import ServiceForm

    is_submit = False

    if request.method == 'GET':

        form = ServiceForm()

        return render_with_user(request, 'services/add_service.html',
                                {"form": form, "is_submit": is_submit})

    if request.method == 'POST':

        form = ServiceForm(request.POST)
        form_valid = False
        is_submit = True

        if form.is_valid():
            form_valid = True
            form.save(request.user)

        return render_with_user(request, 'services/add_service.html',
                                {"form": form, "is_submit": is_submit,
                                 "form_valid": form_valid, })


def EditService(request, serviceId):

    from .forms import EditServiceForm

    service = Service.objects.all().get(id=serviceId)

    if request.method == 'GET':

        form = EditServiceForm(service)

        return render_with_user(request, 'services/edit_service.html',
                                {"form": form, "serviceId": serviceId})

    if request.method == 'POST':

        form = EditServiceForm(service, request.POST)

        form_valid = False

        if form.is_valid():
            form_valid = True
            form.save()

        return render_with_user(request, 'services/edit_service.html',
                                {"form": form, "form_valid": form_valid,
                                 "serviceId": serviceId})


def ServicePayWithBalance(request):

    post = request.POST
    user = request.user

    invoice_number = post["invoice_number"]
    date_created = post["date_created"]
    csrf = post["csrf"]
    serviceId = post["serviceId"]
    print csrf

    if len(Invoice.objects.all().filter(number=invoice_number)) == 0:
        url = "/paypal/payment/service/" + serviceId + "/3/" + csrf + "/" \
              + date_created + "/"
        return redirect(url)

    if len(Balance.objects.all().filter(user=user)) == 0:
        url = "/paypal/payment/service/" + serviceId + "/4/" + csrf + "/" \
              + date_created + "/"
        return redirect(url)

    b = Balance.objects.all().get(user=user)
    s = Service.objects.all().get(id=serviceId)

    if b.balance < s.service_cost:
        url = "/paypal/payment/service/" + serviceId + "/4/" + csrf + "/" \
              + date_created + "/"
        return redirect(url)

    b.balance = b.balance - s.service_cost
    b.save()

    url = "/paypal/payment/service/" + serviceId + "/1/" + csrf + "/" \
          + date_created + "/"

    return redirect(url)


@csrf_exempt
def ServicesPayment(request, serviceId, csrf, payStatus, date_created):

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
        "amount": service.service_cost,
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
                                       buyer=user, amount=1, is_paid=False,
                                       number=invoice_number)
            i.save()
    if payStatus == "1":
        if len(Invoice.objects.all().filter(number=invoice_number)) == 0:
            payStatus = "3"
        else:
            i = Invoice.objects.all().get(number=invoice_number)
            i.is_paid = True
            i.save()
    if payStatus == "0":
        if len(Invoice.objects.all().filter(number=invoice_number)) == 0:
            payStatus = "3"
        else:
            i = Invoice.objects.all().get(number=invoice_number)
            i.is_paid = False
            i.save()

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox(), "service": service,
               "payStatus": payStatus, "invoice_number": invoice_number,
               "date_created": date_created, "serviceId": serviceId, }

    return render_with_user(request, "paypal/payment.html", context)