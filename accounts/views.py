from django.views.generic import View
from django.shortcuts import redirect, HttpResponse

from choiceNet.functions import render_with_user
from choiceNet.decorators import *


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

    orders = Invoice.objects.all().filter(buyer=request.user, is_active=True)
    count = len(orders)
    context = {"orders": orders, "isDeleted": isDeleted, "count": count}

    return render_with_user(request, 'accounts/orders.html', context)


@login_required
def products_list(request):

    return HttpResponse("We're working on that.")