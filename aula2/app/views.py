from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def coisa(request):
    return HttpResponse("Coisa coisa coisa")