from django.contrib import admin

from .models import Quest, QuestScore
from app.main.models import Profile


class QuestAdmin(admin.ModelAdmin):
    list_display = ['level', 'is_active']


admin.site.register(Quest, QuestAdmin)


class QuestScoreAdmin(admin.ModelAdmin):
    list_display = ['profile', 'max_level', 'max_time']

admin.site.register(QuestScore, QuestScoreAdmin)
