from django.shortcuts import redirect


def login_required(function):

    def decorator(request, *args, **kwargs):
        if not request.user.is_active:
            return redirect("/login/?next=%s#mustlogin" %
                            (request.get_full_path(), ))

        return function(request, *args, **kwargs)
    return decorator


def logout_required(function):

    def decorator(request, *args, **kwargs):
        if request.user.is_active:
            return redirect("/home/?next=%s#mustlogout" %
                            (request.get_full_path(), ))
        return function(request, *args, **kwargs)
    return decorator