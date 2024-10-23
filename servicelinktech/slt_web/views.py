from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def master(request):
    template = loader.get_template("slt_web/content/slt_dashboard.html")
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template("slt_web/index.html")
    return HttpResponse(template.render())