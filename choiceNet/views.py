from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.utils.timezone import utc

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
        "amount": int(amount)/100,
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


def AddComment(request, serviceId, formType):

    from .forms import CommentForm, ProviderCommentForm

    is_submit = False
    service = Service.objects.all().get(id=serviceId)

    if formType == "0":
        if request.method == 'GET':

            form = ProviderCommentForm()

            return render_with_user(request,
                                    'choiceNet/provider_add_comment.html',
                                    {"form": form, "is_submit": is_submit,
                                     "service": service})

        if request.method == 'POST':

            form = ProviderCommentForm(request.POST)
            form_valid = False
            is_submit = True
            service = Service.objects.all().get(id=serviceId)

            if form.is_valid():
                form_valid = True
                form.save(request.user, service)

            return render_with_user(request,
                                    'choiceNet/provider_add_comment.html',
                                    {"form": form, "is_submit": is_submit,
                                     "form_valid": form_valid,
                                     "service": service})

    else:
        if request.method == 'GET':

            form = CommentForm()

            return render_with_user(request, 'choiceNet/add_comment.html',
                                    {"form": form, "is_submit": is_submit,
                                     "service": service})

        if request.method == 'POST':

            form = CommentForm(request.POST)
            form_valid = False
            is_submit = True
            service = Service.objects.all().get(id=serviceId)

            if form.is_valid():
                form_valid = True
                form.save(request.user, service)

            return render_with_user(request, 'choiceNet/add_comment.html',
                                    {"form": form, "is_submit": is_submit,
                                     "form_valid": form_valid,
                                     "service": service})


def GetComments(request, serviceId):

    service = Service.objects.all().get(id=serviceId)
    rate = 0
    comments = Comment.objects.all().filter(service=service).\
        order_by('created_date')
    data = []
    count = 0
    from django.utils.timezone import localtime
    for c in comments:
        data.append({"rate": c.rate, "comment": c.comment,
                     "date": str(localtime(c.created_date)),
                     "user": str(c.user), "is_provider": c.is_provider})
        if not c.is_provider:
            rate += c.rate
            count += 1

    if count > 0:
        total_rate = float(rate)/float(count)
    else:
        total_rate = 0

    jsonData = json.dumps({"rate": str(round(total_rate, 2)),
                           "count": len(data), "comments": data}, )

    return HttpResponse(jsonData)


def ProviderWithdraw(request):

    provider = request.user
    income = Income.objects.all().filter(provider=provider)

    if len(income) == 0:
        income = Income.objects.create(provider=provider, income=0,)
        income.save()
    else:
        income = Income.objects.all().get(provider=provider)

    if income.updated_time is None:
        from django.utils import timezone
        updated_date = datetime.datetime(1970, 1, 1, 20, 0, 0, 0, timezone.utc)
    else:
        updated_date = income.updated_time

    orders = Invoice.objects.all().\
        filter(service__owner=provider, is_active=True, ).\
        exclude(service_id=56)

    amount = 0
    count = 0

    for o in orders:
        if o.date_created > updated_date:
            amount += o.amount*o.service.service_cost
            count += 1

    income.updated_time = datetime.datetime.now()
    income.income += amount
    income.save()

    context = {"amount": amount, "new_income": income.income}

    return render_with_user(request, 'choiceNet/withdraw.html', context)


def user_help(request):

    return HttpResponse("We are working hard on this function now!")


@csrf_exempt
def KeyExchange(request):

    clientKey = long(request.POST["publicKey"])

    crypto = DiffieHellman()
    crypto.genKey(clientKey)
    crypto.getKey()

    key = hexlify(crypto.key)

    # Create new session
    session = 0
    start_time = datetime.datetime.utcnow().replace(tzinfo=utc)
    end_time = start_time + datetime.timedelta(0, 360)

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
    balance = 0

    if user is not None:
        success = True
        session.user = user
        from random import randint
        session.session = randint(1, 99999999)
        session.is_login = True
        session.save()
        balance = Balance.objects.all().get(user=user).balance

    data = {"success": success, "session": session.session,
            "balance": str(balance)}

    return render_with_session(session_id, data)


@csrf_exempt
def RequestService(request):

    session_id = request.POST["session_id"]
    s = Session.objects.all().get(id=session_id)

    data = request.POST["data"]
    plain_text = decrypt(data, s.key)

    session = plain_text["session"]
    check_session(session_id, session)

    service_id = plain_text["service_id"]
    amount = plain_text["amount"]
    user = Session.objects.all().get(id=session_id).user
    invoice_number = None
    is_service = False
    balance = -1
    sufficient_balance = False

    try:
        s = Service.objects.all().get(service_id=service_id)
        is_service = True
        i = create_invoice(s, amount, user)
        b = Balance.objects.all().get(user=user)
        invoice_number = i.number
        if s.service_cost * amount <= b.balance:
            sufficient_balance = True
            invoice_number = i.number
            i.is_paid = True
            i.save()
            b.balance = b.balance - s.service_cost * amount
            b.save()
            balance = b.balance
    except:
        pass

    data = {"balance": str(balance), "is_service": is_service,
            "invoice_number": invoice_number,
            "sufficient_balance": sufficient_balance}

    return render_with_session(session_id, data)


@csrf_exempt
def PayOrder(request):

    session_id = request.POST["session_id"]
    s = Session.objects.all().get(id=session_id)

    data = request.POST["data"]
    plain_text = decrypt(data, s.key)

    session = plain_text["session"]
    check_session(session_id, session)

    invoice_number = plain_text["invoice_number"]
    user = Session.objects.all().get(id=session_id).user
    is_invoice = False
    balance = -1
    sufficient_balance = False
    previous_paid = True

    try:
        i = Invoice.objects.all().get(number=invoice_number)
        print i.is_active
        if i.is_active:
            s = i.service
            is_invoice = True
            b = Balance.objects.all().get(user=user)
            invoice_number = i.number
            if s.service_cost * i.amount <= b.balance and not i.is_paid:
                sufficient_balance = True
                invoice_number = i.number
                i.is_paid = True
                i.save()
                b.balance = b.balance - s.service_cost * i.amount
                b.save()
                balance = b.balance
                previous_paid = False
    except:
        pass

    data = {"balance": str(balance), "is_invoice": is_invoice,
            "invoice_number": invoice_number, "previous_paid": previous_paid,
            "sufficient_balance": sufficient_balance}

    return render_with_session(session_id, data)

@csrf_exempt
def RequestRefund(request):

    session_id = request.POST["session_id"]
    s = Session.objects.all().get(id=session_id)

    data = request.POST["data"]
    plain_text = decrypt(data, s.key)

    session = plain_text["session"]
    check_session(session_id, session)

    invoice_number = plain_text["invoice_number"]
    user = Session.objects.all().get(id=session_id).user
    is_invoice = False
    balance = -1
    is_refund = False

    try:
        i = Invoice.objects.all().get(number=invoice_number)
        if i.is_active:
            s = i.service
            is_invoice = True
            b = Balance.objects.all().get(user=user)
            if s.service_cost * i.amount <= b.balance and i.is_paid:
                i.is_paid = False
                i.is_active = False
                i.save()
                b.balance = b.balance + s.service_cost * i.amount
                b.save()
                balance = b.balance
                is_refund = True
    except:
        pass

    data = {"balance": str(balance), "is_invoice": is_invoice,
            "is_refund": is_refund}

    return render_with_session(session_id, data)