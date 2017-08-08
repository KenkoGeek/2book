from django.db import models
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.db.models import signals
from object2book.models import (
    Statuses,
    Location,
    Object,
)


# Create your models here.

class Person(models.Model):
    """(Person model)"""
    fullname = models.CharField(max_length=50)
    personId = models.CharField(max_length=12)
    phonenumber = models.CharField(max_length=18,null=True)
    email = models.EmailField()
    birthdate = models.DateField()

    def __str__(self):
        return self.fullname


class Booking(models.Model):
    """Random code generator function"""
    def pnr():
        pnr_code = get_random_string(length=6,allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return pnr_code

    """(Booking model)"""
    pnr = models.CharField(default=pnr, max_length=6, unique=True)
    person = models.ForeignKey(Person)
    objectToBook = models.ForeignKey(Object)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()


    # def notify(sender, instance, created, **kwargs):
    #     """Notify to user that a new booking has been added."""
    #     if created:
    #         subject = 'Booking created'
    #         message = 'Booking %s for %s was added booked from %s to %s' % instance.pnr, instance.objectToBook, instance.from_date, instance.to_date
    #         from_addr = 'no-reply@example.com'
    #         recipient_list = (Person.email())
    #         send_mail(subject, message, from_addr, recipient_list)
    #
    #     signals.post_save.connect(notify, sender=Booking)

    def __str__(self):
        return self.pnr
