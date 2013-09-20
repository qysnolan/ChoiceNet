from django.views.generic import View
from django.shortcuts import redirect

from choiceNet.functions import render_with_user


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

    return redirect("/login/#loggedout")


def CreateAccount(request):
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