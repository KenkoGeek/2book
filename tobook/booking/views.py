from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking, Person
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the booking index.")
