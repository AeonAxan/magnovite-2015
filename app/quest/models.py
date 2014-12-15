from django.db import models

from app.main.models import Profile


class Quest(models.Model):
    is_active = models.BooleanField(
        default=False,
        help_text='If unchecked level wont be shown'
    )

    level = models.IntegerField(unique=True)
    img1 = models.URLField()
    img2 = models.URLField()

    answer = models.CharField(
        max_length=50,
        help_text='Answer is case insensitive'
    )


class QuestScore(models.Model):
    profile = models.OneToOneField(Profile, related_name='quest_score')
    max_level = models.IntegerField(default=0)
    max_time = models.DateTimeField()

    class Meta:
        ordering = ['-max_level', 'max_time']
