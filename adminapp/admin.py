# admin.py

from django.contrib import admin
from .models import Bus, BusRoute

class BusAdmin(admin.ModelAdmin):
    list_display = ['bus_type', 'bus_name', 'bus_number', 'max_capacity']

admin.site.register(Bus, BusAdmin)

class BusRouteAdmin(admin.ModelAdmin):
    list_display = ['route_name', 'source', 'destination', 'date', 'timings', 'price']

admin.site.register(BusRoute, BusRouteAdmin)


