import json

from django.views.decorators.http import require_POST
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.exceptions import PermissionDenied

from app.event.utils import generate_team_id
from app.event.models import Event, Registration
from app.main.models import MUser, Profile
from app.workshop.models import Workshop

from .forms import RegistrationForm
from app.main.utils import template_email


def recipt_view(req, rid=None):
    user = None

    # allow admins to access receipts using ids
    if rid is not None and req.user.is_authenticated() and req.user.is_staff:
        try:
            uid = int(rid)

            # guard the improbable case where hash is all numeric
            if uid < 999999:
                user = get_object_or_404(MUser, id=MUser.get_real_id(uid))
        except:
            pass

    if user is None:
        if rid is not None:
            user = get_object_or_404(Profile, receipt_id=rid).user
        else:
            if not req.user.is_authenticated():
                raise Http404

            user = req.user

    registrations = Registration.objects.filter(profile=user.profile)
    workshops = user.profile.registered_workshops.all()

    if settings.DEBUG:
        template = 'magnovite/recipt.html'
    else:
        template = 'magnovite/dist/recipt.html'

    return render(req, template, {
        'user': user,
        'profile': user.profile,
        'registrations': registrations,
        'workshops': workshops
    })


def private_view(req, type, slug):
    """
    Private view for private urls of events and workshops
    shows a table of registrations
    """
    if not type in ('workshop'):
        raise Http404

    workshop = None
    if type == 'workshop':
        workshop = get_object_or_404(Workshop, private_slug=slug)

    if settings.DEBUG:
        template = 'magnovite/private_view.html'
    else:
        template = 'magnovite/dist/private_view.html'

    return render(req, template, {
        'type': type,
        'workshop': workshop,
        'profiles': workshop.profile_set.all().prefetch_related('user').order_by('user__id')
    })

def register_view(req):
    if not (req.user.is_staff and req.user.has_perm('main.on_spot_registration')):
        raise PermissionDenied

    if settings.DEBUG:
        template = 'magnovite/internalRegistration.html'
    else:
        template = 'magnovite/dist/internalRegistration.html'

    events = Event.objects.all()
    workshops = Workshop.objects.all()

    obj = {
        'technical': [],
        'cultural': [],
        'group': [],
        'workshop': []
    }

    for event in events:
        _o = {
            'id': event.id,
            'title': event.title
        }

        if event.is_multiple():
            _o['is_team'] = True
            _o['team_min'] = event.team_min
            _o['team_max'] = event.team_max

        if event.team_type == 'group':
            obj['group'].append(_o)
        elif event.technical:
            obj['technical'].append(_o)
        else:
            obj['cultural'].append(_o)

    for workshop in workshops:
        obj['workshop'].append({
            'id': workshop.id,
            'title': workshop.title,
            'price': workshop.price
        })

    return render(req, template, {
        'jsonobj': json.dumps(obj)
    })


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

    workshops_objs = data.get('workshops', [])
    events_objs = data.get('events', [])

    events = []
    workshops = []

    # validate events passed in
    for event_obj in events_objs:
        if event_obj.get('id', '') == '':
            return JsonResponse({
                'status': 'error',
                'errors': {'form': ['Event ID not given']}
            }, status=400)

        try:
            event = Event.objects.get(id=event_obj['id'])
            events.append(event)
        except Event.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'errors': {'form': ['Invalid Event ID']}
            }, status=400)

        # validate teamids
        team_id = event_obj.get('teamid', '')
        if team_id != '':
            regs = Registration.objects.filter(team_id=team_id, event=event).count()
            if regs == 0:
                return JsonResponse({
                    'status': 'error',
                    'errors': {'tid-' + str(event.id): ['Invalid team id: ' + team_id]}
                }, status=400)

            elif regs == event.team_max:
                return JsonResponse({
                    'status': 'error',
                    'errors': {'tid-' + str(event.id): ['Team (' + team_id + ') is full']}
                }, status=400)

    # validate workshops passed in
    for workshop_obj in workshops_objs:
        if not workshop_obj.get('id', ''):
            return JsonResponse({
                'status': 'error',
                'errrors': {'form': ['Invalid Workshop ID']}
            }, status=400)

        try:
            workshop = Workshop.objects.get(id=workshop_obj['id'])
            workshops.append(workshop)
        except Workshop.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'errors': {'form': ['Invalid Workshop ID']}
            }, status=400)

    # validate pack/event combination
    num_quota_events = 0
    for event in events:
        if event.team_type in ('individual', 'team'):
            num_quota_events += 1

    if f.cleaned_data['pack'] == 'single' and num_quota_events > 1:
        return JsonResponse({
            'status': 'error',
            'errors': {'pack': ['Cant register to more than one individual/team event on single pack']}
        }, status=400)

    elif f.cleaned_data['pack'] == 'none' and num_quota_events > 0:
        return JsonResponse({
            'status': 'error',
            'errors': {'pack': ['Cant register to individual/team events on No Pack']}
        }, status=400)

    try:
        MUser.objects.get(email=f.cleaned_data['email'])

        # duplicate user
        return JsonResponse({
            'status': 'error',
            'errors': {'email': ['This user is already registered']}
        }, status=400)
    except MUser.DoesNotExist:
        user = MUser.objects.create_user(email=f.cleaned_data['email'])

    # calculate payment due
    if f.cleaned_data['pack'] == 'single':
        payment = 100
    elif f.cleaned_data['pack'] == 'multiple':
        payment = 200
    else:
        payment = 0

    # setup profile
    profile = user.profile
    profile.name=f.cleaned_data['name']
    profile.college=f.cleaned_data['college']
    profile.mobile=f.cleaned_data['mobile']
    profile.referral=f.cleaned_data.get('referred', '')
    profile.pack=f.cleaned_data['pack']
    profile.auth_provider='on-spot'

    profile.on_spot = True
    profile.on_spot_registerer = req.user.profile.name
    # profile saved at the end

    success_obj = {
        'name': profile.name,
        'multipleEvents': []
    }

    # do event registrations
    for i, event in enumerate(events):
        team_id = events_objs[i].get('teamid', '')
        is_owner = False

        if event.is_multiple():
            # if team_id given it would already be validated above
            if team_id == '':
                team_id = generate_team_id(user.email, event)

                if event.is_group():
                    is_owner = True

                    # creating group team, cost 500
                    payment += 500

            success_obj['multipleEvents'].append({
                'id': event.id,
                'title': event.title,
                'teamid': team_id
            })

        Registration.objects.create(
            event=event,
            profile=profile,
            team_id=team_id,
            is_owner=is_owner,
            on_spot=True
        )

    # do workshop registrations
    for workshopObj in workshops:
        payment += workshop.price
        profile.registered_workshops.add(workshop)

    profile.total_payment = payment
    profile.save()

    template_email(
        'server@magnovite.net',
        (user.email,),
        'Welcome to Magnovite 2015',
        'on_spot_receipt',
        {'profile': profile}
    )

    success_obj['status'] = 'success'
    success_obj['reciptURL'] = '/receipt/' + profile.receipt_id + '/'

    return JsonResponse(success_obj)


def api_items(req):
    out = {
        'events': {
            'technical': [],
            'cultural': [],
            'group': []
        },
        'workshops': []
    }

    for event in Event.objects.all():
        _o = {
            'id': event.id,
            'title': event.title,
            'slug': event.slug
        }

        if event.is_multiple():
            _o['is_team'] = True
            _o['team_min'] = event.team_min
            _o['team_max'] = event.team_max

        if event.team_type == 'group':
            out['events']['group'].append(_o)
        elif event.technical:
            out['events']['technical'].append(_o)
        else:
            out['events']['cultural'].append(_o)

    for workshop in Workshop.objects.all():
        out['workshops'].append({
            'id': workshop.id,
            'title': workshop.title,
        })

    return JsonResponse(out)
