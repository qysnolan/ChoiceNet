from choiceNet.functions import render_with_user


def ServicesList(request):
    return render_with_user(request, 'services/index.html', {})