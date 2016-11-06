from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def downloads_index(request):
    context = {}
    template = loader.get_template('downloads_index.html')
    return HttpResponse(template.render(context, request))