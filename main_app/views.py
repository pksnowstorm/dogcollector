from django.shortcuts import render
from .models import Dog
# Create your views here.
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello ૮ ・ﻌ・ა</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

