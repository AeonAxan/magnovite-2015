from django.shortcuts import render
from django.http import JsonResponse

from .forms import SubscribeForm

def subscribe(req):
    if req.method != 'POST':
        return JsonResponse(
            {'error': 'Method not supported'},
            status=501
        )

    form = SubscribeForm(req.POST)
    if form.is_valid():
        form.save()
        return JsonResponse(
            {'status': 'Success'},
            status=201
        )
    else:
        return JsonResponse(
            {'errors': form.errors},
            status=400
        )
