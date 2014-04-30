from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json


@csrf_exempt
def login(request):

    username_tag = "Username (email)"
    password_tag = "Password"
    login = False

    if request.method == 'GET':

        # return render(request, 'accounts/auth_login.html',
        #               {"login": login, "username_tag": username_tag,
        #                "password_tag": password_tag, })
        return HttpResponse("GET")

    if request.method == 'POST':

        username = request.POST["username"]
        # password = hashlib.sha1(request.POST["password"]).hexdigest()
        password = request.POST["password"]
        success = False
        user = authenticate(username=username, password=password)
        login = True

        if user is not None:
            success = True

        # return render(request, 'accounts/auth_login.html',
        #               {"success": success, "login": login,
        #                "username_tag": username_tag,
        #                "password_tag": password_tag, })

        data = {"success": success, "login": login,
                "username_tag": username_tag, "password_tag": password_tag, }

        json_data = json.dumps(data)

        return HttpResponse(json_data)
