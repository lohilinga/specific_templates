from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(requst):
    return HttpResponse('<h1>Hello my dear world<h1/>')
def second (requst):
    return HttpResponse('<h1>Hello good afternoon<h1/>')
