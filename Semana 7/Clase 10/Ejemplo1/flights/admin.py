from django.contrib import admin
from .models import Airport, Flight, Passenger, FlightAdmin

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger)

