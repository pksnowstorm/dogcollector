from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Macy', 'chihuahua', 'good old dog', 8),
  Dog('Belle', 'chihuahua', 'fat and mean', 9),
  Dog('Django', 'minature poodle', 'noisy and stupid', 4)
]

def home(request):
  return HttpResponse('<h1>Hello ૮ ・ﻌ・ა</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })