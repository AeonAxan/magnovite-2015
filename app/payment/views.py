import hashlib

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings

from app.main.models import Profile
from app.event.models import Event, Registration

from .utils import get_payu_form, test_checksum
from .models import create_invoice, Invoice

def generate(req, invoice_type):
    if not req.user.is_authenticated():
        return HttpResponse(status=400)

    if invoice_type not in ('team', 'single', 'multiple', 'upgrade'):
        return HttpResponse(status=400)

    # if team verify event is correct
    if invoice_type == 'team':
        event = get_object_or_404(Event, id=req.GET.get('id', None))
        invoice = create_invoice(invoice_type, req.user.profile, event)
        return get_payu_form(req, invoice)

    elif invoice_type in ('single', 'multiple'):
        invoice = create_invoice(invoice_type, req.user.profile)
        return get_payu_form(req, invoice)

    elif invoice_type == 'upgrade':
        # upgrade only valid if user is in single pack
        if req.user.profile.pack != 'single':
            return HttpResponse(status=403)

        invoice = create_invoice(invoice_type, req.user.profile)
        return get_payu_form(req, invoice)

    # unrecognized invoice_type
    return HttpResponse(status=400)


@csrf_exempt
@require_POST
def success(req):
    if not test_checksum(req.POST):
        messages.error(req, 'Invalid Transaction, please contact support (Error: ES01)')
        return redirect('/profile/#help')

    invoice_id = int(req.POST.get('txnid', '').split('-')[1])
    invoice = get_object_or_404(Invoice, id=invoice_id)

    # if already processed skip
    if invoice.pending == False:
        return redirect('/profile/#pack')

    return_val = process_invoice(req, invoice)

    # invalid invoice
    if return_val == None:
        messages.error(req, 'Transaction could not be completed, please contact support (Error: ES02)')
        return redirect('/profile/#help')
    else:
        return return_val

@csrf_exempt
@require_POST
def failure(req):
    messages.error(req, 'Could not complete transaction, please try again or contact support (Error: EF01)')

    invoice_id = int(req.POST.get('txnid', '').split('-')[1])
    try:
        invoice = Invoice.objects.get(id=invoice_id)
        invoice.pending = False
        invoice.post_data = str(req.POST)
        invoice.success = False
        invoice.save()
    except Invoice.DoesNotExist:
        pass

    return redirect('/profile/#help')

@csrf_exempt
@require_POST
def notify(req):
    if not test_checksum(req.POST):
        # TODO: log
        print('ERROR: Invalid checksum in notify()')
        return HttpResponse()

    invoice_id = int(req.POST.get('txnid', '').split('-')[1])
    invoice = get_object_or_404(Invoice, id=invoice_id)

    # if already processed skip
    if invoice.pending == False:
        print('INFO: Skipping invoice already processed')
        return HttpResponse()

    return_val = process_invoice(req, invoice)

    # invalid invoice
    if return_val == None:
        messages.error(req, 'Invalid Transaction, please contact support (Error: EN01)')

    return HttpResponse()


def process_invoice(req, invoice):
    """
    This is not a view, rather a helper function which processes the invoices
    """
    invoice.status = req.POST.get('status', '')
    invoice.success = True
    invoice.pending = False

    invoice.post_data = str(req.POST)
    invoice.save()

    if invoice.invoice_type in ('single', 'multiple', 'upgrade'):
        new_pack = invoice.invoice_type
        if new_pack == 'upgrade':
            new_pack = 'multiple'

        invoice.profile.pack = new_pack
        invoice.profile.save()

        messages.success(req, invoice.profile.get_pack_display() + ' has successfully been activated!')
        return redirect('/profile/#pack')

    elif invoice.invoice_type == 'team':
        corpus = req.user.email + invoice.event.slug + settings.SECRET_KEY[:10]
        team_id = hashlib.sha1(corpus.encode('utf-8')).hexdigest()[:5]

        r = Registration()
        r.event = invoice.event
        r.profile = req.user.profile
        r.team_id = team_id
        r.is_owner = True
        r.save()

        return redirect(r.event.get_absolute_url() + '#view-team')

    # invalid invoice
    return None
