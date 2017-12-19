# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# import the Trip model
from trips.models import Trip
from trips.models import Service


class TripsAdmin(admin.ModelAdmin):
    # display the trips list by the title
    list_display = ("title",)
    # allow for trips to be searched by the title, duration in days and cost
    search_fields = ["title","duration_days","cost"]
    # allow adding and removing services
    filter_horizontal = ('service',)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["type"]

admin.site.register(Trip,TripsAdmin)
admin.site.register(Service,ServicesAdmin)


