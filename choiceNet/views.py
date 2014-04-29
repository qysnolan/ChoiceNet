from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.urlresolvers import reverse

from choiceNet.decorators import *
from choiceNet.models import Balance
from service.models import Service
from choiceNet.functions import render_with_user
from paypal.standard.forms import PayPalPaymentsForm


def error_401(request):
    return render_with_user(request, "error_pages/401.html")


def error_403(request):
    return render_with_user(request, "error_pages/403.html")


def error_404(request):
    return render_with_user(request, "error_pages/404.html")


def error_500(request):
    return render_with_user(request, "error_pages/500.html")


def error_502(request):
    return render_with_user(request, "error_pages/502.html")


def error_504(request):
    return render_with_user(request, "error_pages/504.html")


def maintenance(request):
    return render_with_user(request, "error_pages/maintenance.html")


@logout_required
def welcome(request):

    return render_with_user(request, "welcome.html")


def home(request):

    redirect_to = "/home/"
    if "next" in request.GET:
        redirect_to = request.GET["next"]

    # import random
    # for i in range(0, 20):
    #     products.append(random.randrange(1, 1000))
    products = Service.objects.all()

    return render_with_user(request, "home.html", {"redirect_to": redirect_to,
                                                   "products": products})


def AddBalance(request):

    if request.method == 'GET':

        return render_with_user(request, 'paypal/add_balance.html',)

    if request.method == 'POST':

        import time

        amount = str(int(float(request.POST['amount']) * 100))
        csrf = request.POST['csrf']
        date_created = str(int(float(time.time()*1000)))

        redirect_to = "/paypal/payment/balance/" + amount + "/2/" + csrf \
                      + "/" + date_created

        return redirect(redirect_to)


@csrf_exempt
def BalancePayment(request, amount, csrf, payStatus, date_created):

    from service.models import Service
    from choiceNet.models import Invoice
    import datetime
    import time

    service = Service.objects.all().get(id=56)
    user = request.user
    if date_created == "0":
        date_created = str(time.time())
    invoice_number = date_created + '-service-56-' + str(user.id)

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": service.cost,
        "item_name": service.name,
        "invoice": invoice_number,
        "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
        "return_url": settings.SITE_NAME + "/paypal/payment/balance/"
                      + amount + "/1/" + csrf + "/" + date_created + "/",
        "cancel_return": settings.SITE_NAME + "/paypal/payment/balance/"
                         + amount + "/0/" + csrf + "/" + date_created + "/",
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
            from decimal import Decimal
            if len(Balance.objects.all().filter(user=user)) == 0:
                b = Balance.objects.create(user=user,
                                           balance=Decimal(float(amount)/100))
                b.save()
            else:
                b = Balance.objects.all().get(user=user)
                total = b.balance + Decimal(float(amount)/100)
                b.balance = total
                b.save()
    if payStatus == "0":
        if len(Invoice.objects.all().filter(number=invoice_number)) == 0:
            payStatus = "3"
        else:
            i = Invoice.objects.all().get(number=invoice_number)
            i.is_paid = False
            i.save()

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox(), "service": service,
               "payStatus": payStatus, "price": str(float(int(amount)/100))}
    return render_with_user(request, "paypal/balance_payment.html", context)


def user_help(request):

    return HttpResponse("We are working hard on this function now!")