from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def render_with_user(request, template_name, context={}):
    from website.settings import DEBUG

    context["debugMode"] = DEBUG

    user = request.user

    if user.is_authenticated():
        context["name"] = user.fullname()

        context["user"] = request.user

        context.update(csrf(request))
        return render_to_response(template_name, context)

    else:

        context["name"] = "Login or sign up"
        return render_to_response(template_name, context)
