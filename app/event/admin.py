from django.contrib import admin

from app.main.models import Profile
from .models import Event, Registration


class EventHeadInline(admin.TabularInline):
    model = Profile
    extra = 0
    verbose_name = 'Event Head'
    verbose_name_plural = 'Event Heads'
    fields = ('name', 'active_email', 'mobile', 'is_internal')

    def has_add_permission(self, request):
        """
        We cant possibly add eventheadheads from here because
        an associated MUser must be present
        """
        return False

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
