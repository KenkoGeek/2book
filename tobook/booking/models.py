import os
from django.db import models
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
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
        return '{}, {}'.format(self.fullname, self.email)


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

    def __str__(self):
        return self.pnr

emailPnr = Booking()

@receiver(post_save, sender=Booking, dispatch_uid="send_booking_info")
def send_booking(sender, instance, **kwargs):

    """Declare enviroment variables first to set this, only testing purpose"""
    sender_email = os.environ.get('SENDER_EMAIL')
    receipt_email = os.environ.get('RECEIPT_EMAIL')

    email_text = '''Booking %s ''' % (emailPnr)
    send_mail("Booking created", email_text, sender_email, [receipt_email])
