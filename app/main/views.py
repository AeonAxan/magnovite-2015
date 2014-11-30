from django.conf import settings
from django.shortcuts import render

def index(req):
    if settings.DEBUG:
        template = 'magnovite/home.html'
    else:
        template = 'magnovite/dist/home.html'

    return render(req, template)


def events(req):
    return render(req, 'magnovite/events.html')

def profile(req):
    return render(req, 'magnovite/profile.html')
