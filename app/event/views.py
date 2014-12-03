from django.shortcuts import render
from django.conf import settings

from .models import Event


def index(req):
    if settings.DEBUG:
        template = 'magnovite/events.html'
    else:
        template = 'magnovite/dist/events.html'

    events = Event.objects.all()

    return render(req, template, {
        'events': events
    })

def details(req):
 	return render(req, 'magnovite/eventDetails.html')
