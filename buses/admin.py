
# Register your models here.
from django.contrib import admin

from .models import Bus,Seat,Seat_details
# Register your models here.

from .models import*
# Register your models here.
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['id','bus_name','bus_type','date','time','available_seats','destination_from','destination_to']
 
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['id','seat_no']

@admin.register(Seat_details)
class Seat_detailsAdmin(admin.ModelAdmin):
    list_display = ['id','seat_no','seat_available']