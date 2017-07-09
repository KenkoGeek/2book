from django.db import models
from django.utils.crypto import get_random_string

from tobook.models import (
    Statuses,
    Location,
    Object,
)

# Create your models here.

class Person(models.Model):
    """(Person model)"""
    fullname = models.CharField(text_length=50)
    personId = models.CharField(text_length=12)
    phonenumber = models.PhoneNumberField(blank=True)
    email = models.EmailField()
    birthday = models.DateTimeField()

    def __unicode__(self):
        return self.fullname


class Booking(models.Model):
    """(Booking model)"""
    pnr = get_random_string(length=6,allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    person = ForeignKey(Person)
    objectToBook = ForeignKey(Object)






    def __str__(self):
        return self.name
