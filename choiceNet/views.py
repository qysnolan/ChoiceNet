from choiceNet.functions import render_with_user


def home(request):

    return render_with_user(request, "home.html")
