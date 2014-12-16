from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from app.event.models import Registration

from .forms import ProfileForm
from .models import Profile
from .utils import AjaxableResponseMixin

def logout_view(req):
    if req.user.is_authenticated():
        logout(req)

    next_url = req.GET.get('next', '/')
    return HttpResponseRedirect(next_url)


def index(req):
    if settings.DEBUG:
        template = 'magnovite/home.html'
    else:
        template = 'magnovite/dist/home.html'

    return render(req, template)


@login_required
def profile(req):
    if settings.DEBUG:
        template = 'magnovite/profile.html'
    else:
        template = 'magnovite/dist/profile.html'


    profile_form = ProfileForm(instance=req.user.profile)

    registrations = Registration.objects.filter(profile=req.user.profile)
    day_one = map(lambda x: x.event, registrations.filter(event__date=21))
    day_two = map(lambda x: x.event, registrations.filter(event__date=22))

    # evaluate maps
    day_one = [x for x in day_one]
    day_two = [x for x in day_two]

    return render(req, template, {
        'profile_form': profile_form,
        'days': [day_one, day_two],
    })


class ProfileUpdate(AjaxableResponseMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    http_method_names = ['post']

profile_update_view = ProfileUpdate.as_view()
