from django.shortcuts import render_to_response, redirect, HttpResponse
from choiceNet.functions import render_with_user


def home(request):

    return render_with_user(request, "home.html")


def logout(request):

    return redirect("/login/#loggedout")