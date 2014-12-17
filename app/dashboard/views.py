from django.shortcuts import render
from django.conf import settings
from django.http import Http404

def index(req):
    if not req.user.is_staff:
        raise Http404()

    if settings.DEBUG:
        template = 'magnovite/dashboard.html'
    else:
        template = 'magnovite/dist/dashboard.html'

    return render(req, template)
