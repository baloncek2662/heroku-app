from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User

def index(request):
    users = User.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def register(request):
    return HttpResponse("You are at the registration page")

def login(request):
    return HttpResponse("You are at the login page")
