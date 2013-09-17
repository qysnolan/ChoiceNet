from django.shortcuts import render_to_response
from choiceNet.functions import render_with_user


def home(request):

    return render_to_response("home.html")