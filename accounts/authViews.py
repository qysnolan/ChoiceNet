from django.shortcuts import render
from django.contrib.auth import authenticate
import hashlib


def login(request):

    username_tag = "Username (email)"
    password_tag = "Password"
    login = False

    if request.method == 'GET':

        return render(request, 'accounts/auth_login.html',
                      {"login": login, "username_tag": username_tag,
                       "password_tag": password_tag, })

    if request.method == 'POST':

        username = request.POST["username"]
        password = hashlib.sha1(request.POST["password"]).hexdigest()
        success = False
        user = authenticate(username=username, password=password)
        login = True

        if user is not None:
            success = True

        return render(request, 'accounts/auth_login.html',
                      {"success": success, "login": login,
                       "username_tag": username_tag,
                       "password_tag": password_tag, })
