from django.shortcuts import redirect
from django.contrib import auth


def login_required(function):

    def decorator(request, *args, **kwargs):
        if not request.user.is_active:
            return redirect("/login/?next=%s#mustlogin" %
                            (request.get_full_path(), ))

        return function(request, *args, **kwargs)
    return decorator


def logout_required(function):

    def decorator(request, *args, **kwargs):
        auth.logout(request)
        if not request.user.is_authenticated():
            return redirect("/sign_up#loggedout")

        return function(request, *args, **kwargs)
    return decorator