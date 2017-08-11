from django.contrib import admin
from booking.models import Person, Booking
from django.core.mail import send_mail

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('pnr','person','objectToBook','from_date','to_date')

class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('fullname','phonenumber','email')

admin.site.register(Person, PersonAdmin)

admin.site.register(Booking, BookingAdmin)
