from django.contrib import admin

from app.subscribe.models import Subscription

@admin.register(Subscription)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email',)
