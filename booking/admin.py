from django.contrib import admin
from booking.models import(
    Person,
    Booking,
)
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display('pnr','fullname','Object')


admin.site.register(Person)

admin.site.register(Booking,BookingAdmin)
