from choiceNet.functions import render_with_user
from django.shortcuts import HttpResponse
from choiceNet.decorators import *


@logout_required
def welcome(request):

    return render_with_user(request, "welcome.html")


def home(request):

    redirect_to = "/home/"
    if "next" in request.GET:
        redirect_to = request.GET["next"]

    return render_with_user(request, "home.html", {"redirect_to": redirect_to})


def user_help(request):

    return HttpResponse("We are working hard on this function now!")