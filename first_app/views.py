# first_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index(request):
  return HttpResponse('<h1>Welcome to our campus! /ᐠ｡‸｡ᐟ\ﾉ</h1>')