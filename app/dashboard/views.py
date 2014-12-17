from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponse

from .models import Analytics


def index(req):
    if not req.user.is_staff:
        raise Http404

    if settings.DEBUG:
        template = 'magnovite/dashboard.html'
    else:
        template = 'magnovite/dist/dashboard.html'

    return render(req, template)


def data(req):
    if not req.user.is_staff:
        raise Http404

@csrf_exempt
def capture(req):
    if settings.DEBUG:
        secret = req.GET.get('secret', '')
    else:
        secret = req.POST.get('secret', '')

    if secret != settings.ANALYTICS_SECRET:
        status = 400
    else:
        status = 200
        Analytics.capture()

    return HttpResponse(status=status)
