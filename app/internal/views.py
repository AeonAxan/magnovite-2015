import json

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.conf import settings

from app.event.utils import generate_team_id
from app.event.models import Event, Registration
from app.main.models import MUser

from .forms import RegistrationForm


def register_view(req):
    if not (req.user.is_staff and req.user.has_perm('main.on_spot_registration')):
        raise PermissionDenied

    if settings.DEBUG:
        template = 'magnovite/internalRegistration.html'
    else:
        template = 'magnovite/dist/internalRegistration.html'

    return render(req, template)


@csrf_exempt
@require_POST
def register_create(req):
    if not (req.user.is_staff and req.user.has_perm('main.on_spot_registration')):
        raise PermissionDenied

    # IN params
    # name, email, college, mobile, referred, pack, events [{id, teamid?}]
    try:
        data = json.loads(req.body.decode('utf-8'))
    except ValueError:
        return JsonResponse({
            'status': 'error',
            'errorMessage': 'Invalid JSON'
        }, status=400)

    f = RegistrationForm(data)
    if not f.is_valid():
        return JsonResponse({
            'status': 'error',
            'errors': f.errors
        }, status=400)

    try:
        MUser.objects.get(email=f.cleaned_data['email'])

        # duplicate user
        return JsonResponse({
            'status': 'error',
            'errors': {'email': 'This user is already registered'}
        }, status=400)
    except MUser.DoesNotExist:
        user = MUser.objects.create_user(email=f.cleaned_data['email'])

    profile = user.profile
    profile.name=f.cleaned_data['name']
    profile.college=f.cleaned_data['college']
    profile.mobile=f.cleaned_data['mobile']
    profile.referral=f.cleaned_data.get('referred', '')
    profile.pack=f.cleaned_data['pack']
    profile.auth_provider='on-spot'
    profile.save()

    events = data.get('events', [])
    for eventObj in events:
        if eventObj.get('id', '') == '':
            return JsonResponse({
                'status': 'error',
                'errors': {'form': 'Event ID not given'}
            }, status=400)

        try:
            event = Event.objects.get(id=eventObj['id'])
        except Event.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'errors': {'form': 'Invalid Event ID'}
            }, status=400)

        team_id = eventObj.get('teamid', '')
        is_owner = False
        if event.is_multiple():
            if team_id == '':
                team_id = generate_team_id(user.email, event)

                if event.is_group():
                    is_owner = True

            else:
                try:
                    Registration.objects.get(team_id=team_id)
                except Registration.DoesNotExist:
                    return JsonResponse({
                        'status': 'error',
                        'errors': {'tid-' + str(event.id): 'Invalid team id: ' + team_id}
                    }, status=400)

        Registration.objects.create(
            event=event,
            profile=profile,
            team_id=team_id,
            is_owner=is_owner
        )

    return JsonResponse({
        'status': 'success',
        'url': '/profile/'
    })
