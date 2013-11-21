from choiceNet.functions import render_with_user
from django.shortcuts import redirect


def ServicesList(request):

    post = request.POST
    try:
        searchValue = post["searchValue"]
    except:
        searchValue = ""
    searchValue = searchValue.strip()
    url = 'api/services?search=' + searchValue

    return render_with_user(request, 'services/index.html',
                            {'searchValue': searchValue, 'url': url})