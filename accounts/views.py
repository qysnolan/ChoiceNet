from django.views.generic import View
from django.shortcuts import redirect, HttpResponse

from choiceNet.functions import render_with_user
from choiceNet.decorators import *
from choiceNet.models import Income, Invoice

class LoginView(View):
    """
    *GET*
    Allows a user to go to login page.
    *POST*
    Allows a user to login.
    *TEMPLATES*
    'accounts/login.html'
    """

    def get(self, request):
        from django.contrib.auth import logout
        from .forms import AuthenticationForm

        form = AuthenticationForm(request)

        logout(request)
        request.User = None

        request.session.set_test_cookie()

        redirect_to = "/home/"

        if "next" in request.GET:
            redirect_to = request.GET["next"]

        return render_with_user(request, "accounts/login.html",
                                {"form": form, "redirect_to": redirect_to})

    def post(self, request):
        from django.contrib.auth import login
        from .forms import AuthenticationForm

        form = AuthenticationForm(request, request.POST)

        redirect_to = request.GET.get("next", "/home/")

        if form.is_valid():
            request.session.delete_test_cookie()

            login(request, form.get_user())
            request.session["uid"] = form.get_user_id()

            return redirect(redirect_to)

        return render_with_user(request, "accounts/login.html",
                                {"form": form, "redirect_to": redirect_to})


def logout(request):
    from django.contrib import auth

    auth.logout(request)
    if "next" in request.GET:
        redirect_to = request.GET["next"]
        return redirect(redirect_to)

    return redirect("/login/#loggedout")


@logout_required
def create_account(request):
    """
    *GET*
    Allows a user to create an account.
    *POST*
    Saves account with selected attributes
    *TEMPLATES*
    'accounts/sign_up.html'
    """

    from accounts.forms import UserForm

    if request.method == 'GET':

        form = UserForm()

        redirect_to = "/login/#create"

        if "next" in request.GET:
            redirect_to = request.GET["next"]

        return render_with_user(request, 'accounts/sign_up.html',
                                {"form": form, "redirect_to": redirect_to})

    if request.method == 'POST':

        form = UserForm(request.POST)
        form_valid = False

        redirect_to = request.GET.get("next", "/login/#create")

        if form.is_valid():
            # FORM IS VALID, CREATE USER

            form_valid = True
            form.save()

            return redirect(redirect_to)

        return render_with_user(request, 'accounts/sign_up.html',
                                {"form": form, "form_valid": form_valid,
                                "redirect_to": redirect_to})


@login_required
def account_settings(request):
    """
    *GET*
    Allows a user to change an account.
    *POST*
    Saves account with selected attributes
    *TEMPLATES*
    'accounts/settings.html'
    """

    from accounts.forms import SettingsForm

    if request.method == 'GET':

        form = SettingsForm(request.user)

        redirect_to = "/home/#settings"

        if "next" in request.GET:
            redirect_to = request.GET["next"]

        return render_with_user(request, 'accounts/settings.html',
                                {"form": form, "redirect_to": redirect_to})

    if request.method == 'POST':

        form = SettingsForm(request.user, request.POST)

        form_valid = False

        redirect_to = request.GET.get("next", "/home/#settings")

        if form.is_valid():
            # FORM IS VALID, CREATE USER

            form_valid = True
            form.save()

            return redirect(redirect_to)

        return render_with_user(request, 'accounts/settings.html',
                                {"form": form, "form_valid": form_valid,
                                "redirect_to": redirect_to})


def forget_password(request):

    return HttpResponse("We are working hard on this function now!")


@login_required
def orders(request):

    from choiceNet.models import Invoice
    isDeleted = 2

    if request.method == "POST":
        try:
            orderId = request.POST["orderId"]
            order = Invoice.objects.all().get(id=orderId)
            order.is_active = False
            order.save()
            isDeleted = 1
        except:
            isDeleted = 0

    orders = Invoice.objects.all().filter(buyer=request.user, is_active=True).\
        exclude(service_id=56)
    count = len(orders)
    context = {"orders": orders, "isDeleted": isDeleted, "count": count}

    return render_with_user(request, 'accounts/orders.html', context)


@login_required
def sales(request):

    from choiceNet.models import Invoice, Income

    refund_approved = 2

    if request.method == "POST":
        try:
            orderId = request.POST["orderId"]
            order = Invoice.objects.all().get(id=orderId)
            order.refund_status = "approved"
            order.save()
            refund_approved = 1
        except:
            refund_approved = 0

    orders = Invoice.objects.all().\
        filter(service__owner=request.user, is_active=True).\
        exclude(service_id=56)
    count = len(orders)
    paid_sales = 0
    unpaid_sales = 0

    for o in orders:
        if o.is_paid:
            paid_sales += o.amount*o.service.service_cost
        else:
            unpaid_sales += o.amount*o.service.service_cost

    incomes = Income.objects.all().filter(provider=request.user)
    if len(incomes) == 0:
        income = 0
    else:
        income = Income.objects.all().get(provider=request.user)

    context = {"orders": orders, "count": count, "paid_sales": paid_sales,
               "unpaid_sales": unpaid_sales, "income": income,
               "refund_approved": refund_approved}

    return render_with_user(request, 'accounts/sales.html', context)


@login_required
def products_list(request):

    from service.models import Service
    from choiceNet.models import Invoice

    user = request.user

    services = Service.objects.all().filter(owner=user)
    count = len(services)

    for s in services:
        invoices = Invoice.objects.all().filter(service=s, is_active=True,
                                                is_paid=True)
        s_count = len(invoices)
        s.count = s_count

    context = {"services": services, "count": count}

    return render_with_user(request, 'accounts/products.html', context)


@login_required
def withdraw_request(request):

    import datetime

    withdraw_status = 2

    if request.method == "POST":
        try:
            incomeId = request.POST["incomeId"]
            income = Income.objects.all().get(id=incomeId)
            income.withdraw_status = None
            income.income = 0
            income.withdraw_date = datetime.datetime.now()
            income.save()
            withdraw_status = 1
        except:
            withdraw_status = 0

    incomes = Income.objects.all().filter(withdraw_status="request")
    count = len(incomes)

    context = {"incomes": incomes, "withdraw_status": withdraw_status,
               "count": count}

    return render_with_user(request, 'accounts/withdraw_request.html', context)


@login_required
def request_withdraw(request, incomeId):

    incomes = Income.objects.all().filter(id=incomeId)

    if len(incomes) == 0:
        return HttpResponse("Something went wrong.")

    income = Income.objects.all().get(id=incomeId)
    income.withdraw_status = "request"
    income.save()

    return HttpResponse(
        "Request is successfully sent to Manager, please return.")


@login_required
def refund_request(request):

    refund_status = 2

    if request.method == "POST":
        try:
            orderId = request.POST["orderId"]
            order = Invoice.objects.all().get(id=orderId)
            order.refund_status = "refunded"
            order.is_paid = False
            order.save()
            refund_status = 1
        except:
            refund_status = 0

    orders = Invoice.objects.all().filter(refund_status="approved")
    count = len(orders)

    context = {"orders": orders, "refund_status": refund_status,
               "count": count}

    return render_with_user(request, 'accounts/refund_request.html', context)


@login_required
def request_refund(request, orderId):

    orders = Invoice.objects.all().filter(id=orderId)

    if len(orders) == 0:
        return HttpResponse("Something went wrong.")

    order = Invoice.objects.all().get(id=orderId)
    order.refund_status = "request"
    order.save()

    return HttpResponse(
        "Request is successfully sent to Provider, please return.")