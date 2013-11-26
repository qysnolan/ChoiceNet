from choiceNet.functions import render_with_user
from django.shortcuts import HttpResponse
from choiceNet.decorators import *
from service.models import Service


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


def user_help(request):

    return HttpResponse("We are working hard on this function now!")