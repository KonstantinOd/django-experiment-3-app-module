from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import datetime


def submode(request):
    return HttpResponse("Hello, I am submodule!")