from django.db import models
from django.utils.crypto import get_random_string
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

    def __str__(self):
        return self.pnr
