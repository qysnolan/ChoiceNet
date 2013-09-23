from choiceNet.functions import render_with_user
from django.shortcuts import HttpResponse


def home(request):

    return render_with_user(request, "home.html")


def user_help(request):

    return HttpResponse("We are working hard on this function now!")