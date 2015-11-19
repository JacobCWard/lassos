from django.contrib import admin

from .models import Competition, Division, Team, Event, Participant

class ParticipantInline(admin.StackedInline):
    model = Participant
    radio_fields = {
        "gender": admin.HORIZONTAL
    }
    extra = 2

class TeamAdmin(admin.ModelAdmin):
    radio_fields = {
        "division": admin.HORIZONTAL
    }
    inlines = [ParticipantInline]

class DivisionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'competition']

class EventAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'division']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'number_of_members']

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'team']
    list_editable = ['team']
    filter_horizontal = ['events']


admin.site.register(Competition)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)

admin.sites.AdminSite.site_header = "LASSOS Admin"
admin.sites.AdminSite.site_title = "LASSOS"
