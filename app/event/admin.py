from django.contrib import admin
from django.core.exceptions import ValidationError

from app.main.models import Profile
from .models import Event, Registration


class EventHeadInline(admin.TabularInline):
    model = Profile.events.through
    extra = 0
    verbose_name = 'Event Head'
    verbose_name_plural = 'Event Heads'

class RegistrationsInline(admin.TabularInline):
    model = Registration
    fields = ('profile', 'team_id')
    extra = 0

    def get_readonly_fields(self, req, obj=None):
        fields = super(RegistrationsInline, self).get_readonly_fields(req, obj)

        if not req.user.is_superuser and req.user.has_perm('event.own_event_registrations'):
            return self.fields

        return fields

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'technical', 'is_complete', 'registrations', 'views']
    ordering = ['-views']
    list_filter = ['technical',]
    inlines = [EventHeadInline, RegistrationsInline]

    def get_queryset(self, req):
        qs = super(EventAdmin, self).get_queryset(req)
        if req.user.is_superuser:
            return qs

        if req.user.has_perm('event.change_own'):
            qs = qs.filter(heads=req.user.profile)

        return qs

admin.site.register(Event, EventAdmin)


class RegistrationAdmin(admin.ModelAdmin):
    fields = ('event', 'profile', 'team_id')
    list_display = ['event', 'profile', 'team_id']
    ordering = ['team_id']
    search_fields = ('team_id',)
    list_filter = ['event']

    def get_readonly_fields(self, req, obj=None):
        fields = super(RegistrationAdmin, self).get_readonly_fields(req, obj)

        if not req.user.is_superuser and req.user.has_perm('event.own_event_registrations'):
            return self.fields

        return fields


    def get_queryset(self, req):
        qs = super(RegistrationAdmin, self).get_queryset(req)
        if req.user.is_superuser:
            return qs

        if req.user.has_perm('event.own_event_registrations'):
            qs = qs.filter(event__heads=req.user.profile)

        return qs

admin.site.register(Registration, RegistrationAdmin)
