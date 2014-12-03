import hashlib

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST

from .models import Event, Registration


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

    heads = event.heads.all()
    head_one = None
    head_two = None
    if len(heads) == 1:
        head_one = heads[0]
    elif len(heads) >= 2:
        head_one = heads[0]
        head_two = heads[1]
        # we will show only two event heads

    return render(req, 'magnovite/eventDetails.html', {
        'event': event,
        'is_registered': is_registered,
        'head_one': head_one,
        'head_two': head_two
    })


@require_POST
def register(req, id, team_id=None):
    if not req.user.is_authenticated():
        return JsonResponse({
            'error_code': 'login',
            'error_message': 'Please login first'
        }, status=400)

    # you can only register if profile is complete
    if not req.user.profile.is_complete():
        return JsonResponse({
            'error_code': 'profile_incomplete',
            'error_message': 'You need to complete your profile first'
        }, status=400)

    event = get_object_or_404(Event, id=id)

    r = Registration()
    r.event = event
    r.profile = req.user.profile

    if event.is_team():
        # team registrations
        # If team id is not given, a new create will be crated for this
        # user/event combo and the user will be registered in that team
        if team_id == None:
            corpus = req.user.email + event.slug + settings.SECRET_KEY[:10]
            team_id = hashlib.sha1(corpus).hexdigest()[:5]
        else:
            # make sure team_id is valid, if user has given a team_id
            # then if it is valid, it must be in our registration table

            num = Registration.objects.filter(team_id=team_id).count()

            if num == 0:
                return JsonResponse({
                    'error_code': 'invalid_team_id',
                    'error_message': 'The Team ID you gave is invalid'
                }, status=400)

            # make sure this team is not full
            if num == event.team_max:
                return JsonResponse({
                    'error_code': 'team_full',
                    'error_message': 'The team is full!'
                })

        r.team_id = team_id

    r.save()

    if event.is_team():
        registrations = Registration.objects.filter(team_id=team_id)
        names = [r.profile.name for r in registrations]

        return JsonResponse({
            'team_id': team_id,
            'names': names
        })

    return HttpResponse(status=200)


@require_POST
def unregister(req, id):
    if not req.user.is_authenticated():
        return HttpResponse(status=400)

    event = get_object_or_404(Event, id=id)

    try:
        reg = Registration.objects.get(event=event, profile=req.user.profile)
        reg.delete()
    except Registration.DoesNotExist:
        pass

    # we return 200, even if the user was previously
    # not registered to the event
    return HttpResponse(status=200)



