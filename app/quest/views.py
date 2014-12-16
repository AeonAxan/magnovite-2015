from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .models import QuestScore, Quest

def index(req):
    if settings.DEBUG:
        template = 'magnovite/quest.html'
    else:
        template = 'magnovite/dist/quest.html'

    if not req.user.is_authenticated():
        messages.error(req, 'Please login to play the game')
        current_level = 1
    else:
        quest_score, created = QuestScore.objects.get_or_create(profile=req.user.profile)
        if created:
            quest_score.max_level = 1
            quest_score.save()

        current_level = quest_score.max_level


    quests = Quest.objects.all()

    try:
        current_quest = quests.get(level=current_level)
        completed = False
    except Quest.DoesNotExist:
        completed = True
        current_quest = None

    return render(req, template, {
        'quests': quests,
        'cquest': current_quest,
        'completed': completed
    })


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

