from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Hi(request):
    return HttpResponse("<h1>test function ! </h1>")