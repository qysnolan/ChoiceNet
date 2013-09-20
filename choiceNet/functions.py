from django.shortcuts import render
from django.core.context_processors import csrf


def render_with_user(request, template_name, context={}):
    from website.settings import DEBUG

    context["debugMode"] = DEBUG

    user = request.user

    if user.is_authenticated():
        context["name"] = user.fullname()

        context["user"] = request.user

        context.update(csrf(request))
        return render(request, template_name, context)

    else:

        context["name"] = "Login or sign up"
        return render(request, template_name, context)
