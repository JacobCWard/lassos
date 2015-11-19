from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'title': 'Home'}
    return render(request, 'index.jade', context)

def tech(request):
    context = {'title': 'Technology Used'}
    return render(request, 'tech.jade', context)
