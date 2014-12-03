from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404

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


def details(req, slug):
    event = get_object_or_404(Event, slug=slug)

    is_registered = False
    if req.user.is_authenticated():
        is_registered = req.user.profile.is_registered_to_event(event)

    return render(req, 'magnovite/eventDetails.html', {
        'event': event,
        'is_registered': is_registered
    })
