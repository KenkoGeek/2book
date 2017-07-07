from django.db import models
from places.fields import PlacesField

# Create your models here.
class Statuses(models.Model):
    """(Object's status)"""
    name = models.CharField(max_length=12)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    """(Object Location)"""
    name = models.CharField(max_length=30)
    location = PlacesField()

    def __unicode__(self):
        return self.name


class Object(models.Model):
    """(Object to book)"""
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    status = models.ForeignKey(Statuses,blank=False,default='s')
    capacity = models.IntegerField()
    remaining = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name
