from django.shortcuts import render
from django.template import loader

def user(request):
  template = loader.get_template('')
  return HttpResponse(template.render())