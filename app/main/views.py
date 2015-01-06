from ipware.ip import get_real_ip

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from app.event.models import Registration
from app.message.models import Thread, Message

from .forms import ProfileForm
from .models import Profile
from .utils import AjaxableResponseMixin

def logout_view(req):
    if req.user.is_authenticated():
        logout(req)

    next_url = req.GET.get('next', '/')
    return HttpResponseRedirect(next_url)


def redirect_view(req):
    ip = get_real_ip(req)
    if ip and (ip.startswith('173.252.88') or ip.startswith('173.252.81')):
        return HttpResponse('<h1>Magnovite 2015</h1><p>Christ University presents its annual tech fest</p>')

    return redirect('https://magnovite.org/')


def index(req):
    if settings.DEBUG:
        template = 'magnovite/home.html'
    else:
        template = 'magnovite/dist/home.html'

    return render(req, template)


@require_POST
@login_required
def add_message(req):
    content = req.POST.get('text', '')
    if content == '':
        return HttpResponse(status=400)

    thread, created = Thread.objects.get_or_create(profile=req.user.profile)
    thread.is_pending = True
    thread.save()

    message = Message(thread=thread, content=content)
    message.save()

    return HttpResponse(status=200)


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

    messages = []
    try:
        messages = req.user.profile.thread.messages.all()
    except:
        pass

    return render(req, template, {
        'profile_form': profile_form,
        'days': [day_one, day_two],
        'help_messages': messages,
    })


class ProfileUpdate(AjaxableResponseMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    http_method_names = ['post']

profile_update_view = ProfileUpdate.as_view()
