from django.contrib import admin
from main.models import SeaManagerCruiseUser, Cruise, Reservation, Captain, CruiseLocation
# Register your models here.

admin.site.register(SeaManagerCruiseUser)
admin.site.register(Cruise)
admin.site.register(Reservation)
admin.site.register(Captain)
admin.site.register(CruiseLocation)

