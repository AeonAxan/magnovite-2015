import hashlib

from django.conf import settings
from django.shortcuts import render

def get_payu_form(req, txnid, amount, productinfo):
    profile = req.user.profile

    obj = {
        'key': settings.PAYU_MERCHANT_KEY,
        'txnid': txnid,
        'amount': amount,
        'productinfo': productinfo,
        'firstname': profile.first_name(),
        'email': profile.active_email,
        'phone': profile.mobile,
        'surl': settings.PAYU_SUCCESS_URL,
        'furl': settings.PAYU_FAILURE_URL,
        'service_provider': 'payu_paisa',
    }

    obj['hash'] = generate_checksum(obj)
    return render(req, 'magnovite/paymentForm.html', {
        'fields': obj.items(),
        'url': settings.PAYU_URL
    })

def generate_checksum(obj):
    fields = ['key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
              'udf1', 'udf2', 'udf3', 'udf4', 'udf5', 'udf6', 'udf7', 'udf8',
              'udf9', 'udf10']

    text = '|'.join(map(lambda key: obj.get(key, ''), fields)) + '|' + settings.PAYU_MERCHANT_SALT
    return hashlib.sha512(text.encode('utf-8')).hexdigest()
