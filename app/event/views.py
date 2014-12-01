from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings


@staff_member_required
def index(req):
    if settings.DEBUG:
        template = 'magnovite/events.html'
    else:
        template = 'magnovite/dist/events.html'

    return render(req, template)
