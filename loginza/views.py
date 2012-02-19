from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from mongoengine.django.auth import User


@csrf_exempt
def loginza_complete(request):

    if request.method == 'POST':
        user = authenticate(token=str(request.POST['token']))

        if isinstance(user, User):
            login(request, user)

    else:
        return HttpResponseForbidden()

    return redirect(settings.LOGIN_REDIRECT_URL)


def loginza_logout(request):

    if request.method == 'POST':
        logout(request)
        return redirect(settings.LOGOUT_URL)
    else:
        return HttpResponseForbidden()
