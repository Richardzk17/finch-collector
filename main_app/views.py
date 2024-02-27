from django.shortcuts import render
from django.http import HttpResponse

class Finch:
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

finches = [
  Finch('Tweetie', 'zebra finch', 'Chirps melodiously.', 2),
  Finch('Pico', 'java sparrow', 'Has beautiful plumage.', 1),
  Finch('Chirpy', 'canary', 'Loves to sing.', 3),
  Finch('Pepper', 'society finch', 'Very sociable.', 1)
]


def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })