from django.conf import settings
from django.shortcuts import render

def index(req):
    if settings.DEBUG:
        template = 'home.html'
    else:
        template = 'dist/home.html'

    return render(req, template)


def events(req):
    return render(req, 'events.html')
