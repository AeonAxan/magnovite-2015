import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, JsonResponse, HttpResponse

from app.event.models import Event
from .models import Analytics


def index(req):
    if not (req.user.is_staff and req.user.has_perm('event.change_event')):
        raise Http404

    if settings.DEBUG:
        template = 'magnovite/dashboard.html'
    else:
        template = 'magnovite/dist/dashboard.html'

    qs = Event.objects.all()
    if not req.user.is_superuser and req.user.has_perm('event.change_own'):
        qs = qs.filter(heads=req.user.profile)

    return render(req, template, {
        'events': qs
    })


def data(req):
    if not (req.user.is_staff and req.user.has_perm('event.change_event')):
        raise HttpResponse(status=401)

    if req.GET.get('ids', '') == '':
        return HttpResponse(status=400)

    ids = list(map(int, req.GET['ids'].split(',')))
    events = Event.objects.filter(id__in=ids)

    if req.user.has_perm('event.change_own'):
        acceptable = Event.objects.filter(heads=req.user.profile)
        if events.exclude(id__in=acceptable).exists():
            return HttpResponse(status=401)

    out = []
    for day in Analytics.objects.all():
        events_a = list(filter(lambda o: o['id'] in ids, json.loads(day.data)))
        obj = {
            'date': day.date.strftime('%d/%m'),
            'events': [],
        }

        for event in events_a:
            obj['events'].append({
                'id': event['id'],
                'title': event['title'],
                'views': event['views'],
                'registrations': event['registrations'],
            })

        out.append(obj)

    return JsonResponse(out, safe=False)


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
