from django.contrib import admin
from main.models import AppUser, Cruise, Reservations
# Register your models here.

admin.site.register(AppUser)
admin.site.register(Cruise)
admin.site.register(Reservations)
