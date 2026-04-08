from django.shortcuts import render

# INPUT
from django.http import HttpResponse, HttpRequest

# Create your views here.


def myfunction(request: HttpRequest):
    return HttpResponse("New Page")
