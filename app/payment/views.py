from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings

from app.event.models import Event

from .utils import get_payu_form

def generate(req, invoice_type):
    if not req.user.is_authenticated():
        return HttpResponse(status=400)

    if invoice_type not in ('team', 'single', 'multiple'):
        return HttpResponse(status=400)

    # if team verify event is correct
    if invoice_type == 'team':
        event = get_object_or_404(Event, id=req.GET.get('id', None))

    return get_payu_form(req, '1000', '1000', 'Product Info')

def success(req):
    1/0

def failure(req):
    1/0

def notify(req):
    return HttpResponse()
