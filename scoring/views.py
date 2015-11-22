from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.http import HttpResponse

from django.http import JsonResponse
from django.core import serializers
from . import models
import json

@require_safe
def index(request):
    context = {'title': 'Home'}
    return render(request, 'index.jade', context)

@require_safe
def tech(request):
    context = {'title': 'Technology Used'}
    return render(request, 'tech.jade', context)

@require_safe
def json(request, param):
    if param == 'competitions':
        model = models.Competition
    elif param == 'events':
        model = models.Event
    elif param == 'participants':
        model = models.Event
    else:
        return HttpResponse('{}', content_type='application/json')

    data = model.objects.all()
    body = serializers.serialize('json', data)
    response = HttpResponse(body, content_type='application/json')
    return response

