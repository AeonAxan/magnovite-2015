from django.contrib import admin

from app.main.models import Profile
from .models import Event, Registration


class EventHeadInline(admin.TabularInline):
    model = Profile.events.through
    extra = 0
    verbose_name = 'Event Head'
    verbose_name_plural = 'Event Heads'

class RegistrationsInline(admin.TabularInline):
    model = Registration
    extra = 0

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_complete']
    inlines = [EventHeadInline, RegistrationsInline]

admin.site.register(Event, EventAdmin)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['event', 'profile', 'team_id']

admin.site.register(Registration, RegistrationAdmin)
