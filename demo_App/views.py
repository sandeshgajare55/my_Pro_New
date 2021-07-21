from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    return HttpResponse('<h1>New View</h1>')

