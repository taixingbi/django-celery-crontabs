from django.shortcuts import render

from django.http import HttpResponse

#from .celery import *

def index(request):

    return HttpResponse('hello world!!')
