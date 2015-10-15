from django.contrib import admin

from .models import Competition, Division, Team, Event, Participant

class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 2

class TeamAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]

admin.site.register(Competition)
admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Participant)

admin.sites.AdminSite.site_header = "LASSOS Admin"
admin.sites.AdminSite.site_title = "LASSOS"
