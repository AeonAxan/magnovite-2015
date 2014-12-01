from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from .models import Profile
from .utils import AjaxableResponseMixin

def logout_view(req):
    if req.user.is_authenticated():
        logout(req)

    next = req.GET.get('next', '/')
    return HttpResponseRedirect(next)


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

    return render(req, template, {
        'profile_form': profile_form
    })


class ProfileUpdate(AjaxableResponseMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    http_method_names = ['post']

profile_update_view = ProfileUpdate.as_view()
