from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate

import datetime
import time
import json

from choiceNet.decorators import *
from choiceNet.models import *
from service.models import Service
from choiceNet.functions import *
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

    user = request.user

    if request.method == 'GET':

        balance = 0
        if len(Balance.objects.all().filter(user=user)) == 0:
            b = Balance.objects.create(user=user, balance=0, )
            b.save()
        else:
            b = Balance.objects.all().get(user=user)
            balance = b.balance

        return render_with_user(request, 'paypal/add_balance.html',
                                {'balance': balance, 'amount_valid': 1})

    if request.method == 'POST':

        import time
        try:
            amount = str(int(float(request.POST['amount']) * 100))
            csrf = request.POST['csrf']
            date_created = str(int(float(time.time()*1000)))

            redirect_to = "/paypal/payment/balance/" + amount + "/2/" + csrf \
                          + "/" + date_created
        except:
            b = Balance.objects.all().get(user=user)
            balance = b.balance
            return render_with_user(request, 'paypal/add_balance.html',
                                    {'balance': balance, 'amount_valid': 0})

        return redirect(redirect_to)


@csrf_exempt
def BalancePayment(request, amount, csrf, payStatus, date_created):

    service = Service.objects.all().get(id=56)
    user = request.user
    if date_created == "0":
        date_created = str(int(float(time.time()*1000)))
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
               "payStatus": payStatus, "price": str(float(int(amount)/100)),
               "invoice_number": invoice_number,
               "date_created": date_created, }

    return render_with_user(request, "paypal/balance_payment.html", context)


def user_help(request):

    return HttpResponse("We are working hard on this function now!")


@csrf_exempt
def KeyExchange(request):

    from django.utils.timezone import utc

    clientKey = long(request.POST["publicKey"])

    crypto = DiffieHellman()
    crypto.genKey(clientKey)
    crypto.getKey()

    key = hexlify(crypto.key)

    # Create new session
    session = 0
    start_time = datetime.datetime.utcnow().replace(tzinfo=utc)
    end_time = start_time + datetime.timedelta(0, 60)

    s = Session.objects.create(session=session, start_time=start_time,
                               end_time=end_time, key=key)
    s.save()

    data = {'session_id': s.id, 'publicKey': str(crypto.publicKey)}
    json_data = json.dumps(data)

    return HttpResponse(json_data)


@csrf_exempt
def NewSession(request):

    session_id = request.POST["session_id"]
    session = Session.objects.all().get(id=session_id)

    data = request.POST["data"]
    plain_text = decrypt(data, session.key)

    username = plain_text["username"]
    password = plain_text["password"]
    user = authenticate(username=username, password=password)

    success = False

    if user is not None:
        success = True
        session.user = user
        from random import randint
        session.session = randint(1, 99999999)
        session.is_login = True
        session.save()

    data = {"success": success, "session": session.session}

    return render_with_session(session_id, data)

