from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout


def logout_view(req):
    if req.user.is_authenticated():
        logout(req)

    next = req.GET.get('next', '/')
    return HttpResponseRedirect(next)


def index(req):
    if settings.DEBUG:
        template = 'magnovite/home.html'
    else:
        template = 'magnovite/dist/home.html'

    return render(req, template)


def profile(req):
    if settings.DEBUG:
        template = 'magnovite/profile.html'
    else:
        template = 'magnovite/dist/profile.html'

    return render(req, template)
