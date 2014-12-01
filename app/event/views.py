from django.shortcuts import render
from django.conf import settings


def index(req):
    if settings.DEBUG:
        template = 'magnovite/events.html'
    else:
        template = 'magnovite/dist/events.html'

    return render(req, template)

def details(req):
 	return render(req, 'magnovite/eventDetails.html')
