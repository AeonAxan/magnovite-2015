from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

from .models import Event


@staff_member_required
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
