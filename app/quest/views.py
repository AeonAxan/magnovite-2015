from django.shortcuts import render
from django.conf import settings


def index(req):
    if settings.DEBUG:
        template = 'magnovite/quest.html'
    else:
        template = 'magnovite/dist/quest.html'

    return render(req, template)
