from django.conf import settings
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

def index(req):
    if settings.DEBUG:
        template = 'magnovite/home.html'
    else:
        template = 'magnovite/dist/home.html'

    return render(req, template)


@staff_member_required
def events(req):
    return render(req, 'magnovite/events.html')

@staff_member_required
def profile(req):
    return render(req, 'magnovite/profile.html')
