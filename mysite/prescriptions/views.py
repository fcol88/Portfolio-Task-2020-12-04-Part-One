from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is where you'll be asked "
    "to enter drugs.")

def confirm(request):
    return HttpResponse("This is where you'll be asked "
    "to confirm your responses.")
