from choiceNet.functions import render_with_user


def ServicesList(request):

    post = request.POST
    try:
        searchValue = post["searchValue"]
    except:
        searchValue = ""

    return render_with_user(request, 'services/index.html',
                            {'searchValue': searchValue})