import datetime

from django.shortcuts import render
from django.http import HttpResponse
import datetime

def show(request):
    return HttpResponse('<h1>New View From Demo2</h1>')

def showDate(request):
    dt=datetime.datetime.now()
    s='Date : '+str(dt)
    return HttpResponse(s)

