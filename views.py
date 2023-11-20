from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import datetime


def SubmoduleView(request):
    return HttpResponse("I am submodule")