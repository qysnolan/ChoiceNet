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

    products = []
    import random
    for i in range(0, 20):
        products.append(random.randrange(1, 1000))

    return render_with_user(request, "home.html", {"redirect_to": redirect_to,
                                                   "products": products})


def user_help(request):

    return HttpResponse("We are working hard on this function now!")