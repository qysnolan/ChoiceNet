from django.views.generic import View
from django.shortcuts import render_to_response

from choiceNet.functions import render_with_user


class LoginView(View):

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
        from django.shortcuts import redirect
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


def CreateAccount(request, school=None, department=None):
    """
    *GET*
    Allows a user to create an account.
    *POST*
    Saves account with selected attributes
    *TEMPLATES*
    'Accounts/AddAccount.html'
    """

    from accounts.forms import UserForm

    if request.method == 'GET':
        user = request.User

        initialData = {
            "departments": department,
            "schools": school,
        }

        form = UserForm(current_user=user, initial=initialData)

        return render_to_response('accounts/sign_up.html', {"form": form})

    if request.method == 'POST':
        user = request.User
        form = UserForm(request.POST, current_user=user)

        form_valid = False

        if form.is_valid():
            # FORM IS VALID, CREATE USER

            form_valid = True
            form.save()

            # GIVE USER A BLANK FORM IF VALID

            form = UserForm(current_user=user)

        return render_to_response('accounts/sign_up.html', {'created': form_valid, "form": form})