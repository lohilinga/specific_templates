from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>fire is the fire</h1>')
def second(request):
    return HttpResponse('<h1>All Is Well</h1>')