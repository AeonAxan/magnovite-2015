from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


def logout(req):
    if req.user.is_authenticated():
        req.user.logout()

    next = req.GET.get('next', '/')
    return HttpResponseRedirect(next)

def index(req):
    if settings.DEBUG:
        template = 'magnovite/home.html'
    else:
        template = 'magnovite/dist/home.html'

    return render(req, template)

@staff_member_required
def profile(req):
    if settings.DEBUG:
        template = 'magnovite/profile.html'
    else:
        template = 'magnovite/dist/profile.html'

    return render(req, template)
