import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
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


def data(req, id):
    if not (req.user.is_staff and req.user.has_perm('event.change_event')):
        raise Http404

    id = int(id)
    event = get_object_or_404(Event, id=id)

    if req.user.has_perm('event.change_own'):
        if not event.heads.filter(id=req.user.profile.id).exists():
            return JsonResponse({
                'error': 'permission_denied',
            }, status=400)

    out = []
    for day in Analytics.objects.all():
        event = next(filter(lambda o: o['id'] == id, json.loads(day.data)))
        out.append({
            'id': id,
            'title': event['title'],
            'date': day.date.strftime('%d/%m'),
            'views': event['views'],
            'registrations': event['registrations']
        })

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
