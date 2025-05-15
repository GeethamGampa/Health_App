from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def people(request):
    return HttpResponse("Hello World")

def python_first_app(request):
    return HttpResponse("Congratulations..!! You have created your first app")
