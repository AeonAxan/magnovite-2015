from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .models import QuestScore, Quest

def index(req):
    if settings.DEBUG:
        template = 'magnovite/quest.html'
    else:
        template = 'magnovite/dist/quest.html'

    return render(req, template)


@require_http_methods(['POST'])
def guess(req):
    if not req.user.is_authenticated():
        return JsonResponse({
            'status': 'login',
            'messsage': 'Please login to play the game'
        }, status=401)


    if not req.POST.get('answer', ''):
        return JsonResponse({
            'status': 'invalid_answer',
            'message': 'Please provide an answer'
        }, status=400)

    profile = req.user.profile
    answer = req.POST.get('answer', '')

    score, created = QuestScore.objects.get_or_create(profile=profile)
    if created:
        score.max_level = 1

    try:
        quest = Quest.objects.get(level=score.max_level)
    except Quest.DoesNotExist:
        # user has finished all levels
        return JsonResponse({
            'status': 'invalid_level',
            'message': 'User has finished all levels'
        }, status=400)

    # check answer, maybe use fuzzy matching
    if answer.lower() == quest.answer.lower():
        score.next_level()
        score.save()

        messages.success(req, 'Congratulations! That is correct')

        return JsonResponse({
            'status': 'success',
            'message': 'Congratulations! That is correct'
        }, status=200)
    else:
        return JsonResponse({
            'status': 'invalid_answer',
            'message': 'Sorry! That is not correct'
        }, status=400)

