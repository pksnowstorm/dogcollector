from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello ૮ ・ﻌ・ა</h1>')

def about(request):
    return HttpResponse('<h1>About the DogCollector</h1>')