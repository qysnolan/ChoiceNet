from django.views.generic import View
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

        return render_with_user(request, "accounts/login.html", {"form": form, "redirect_to": redirect_to})

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

        return render_with_user(request, "accounts/login.html", {"form": form, "redirect_to": redirect_to})