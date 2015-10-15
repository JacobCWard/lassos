from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<title>LASSOS</title><p>Welcome! Go to the <a href='/admin'>Admin</a> part of the site.</p>")
