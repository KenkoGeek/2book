from django.contrib import admin
from booking.models import Person, Booking
from django.core.mail import send_mail

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('pnr','person','objectToBook','from_date','to_date')

    actions = ('email_book')

    def email_book(self, request, queryset):
        for booking in queryset:
            if booking.pnr:
                subject = 'Booking created'
                message = 'Booking %s for %s was added booked from %s to %s' % instance.pnr, instance.objectToBook, instance.from_date, instance.to_date
                from_addr = 'no-reply@example.com'
                recipient_list = (person.email)
                send_mail(subject, message, from_addr, recipient_list)


class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ('fullname','phonenumber','email')

admin.site.register(Person, PersonAdmin)

admin.site.register(Booking, BookingAdmin)
