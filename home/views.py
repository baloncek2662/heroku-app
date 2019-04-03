from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User

def index(request):
    users = User.objects.all()
    context = { 'users': users }
    return render(request, 'home/index.html', context)

def register(request):
    return render(request, 'home/register.html')

def login(request):
    return HttpResponse("You are at the login page")

def register_form(request):
    return_message = { 'error_message': "Please fill in all required fields." }
    return render(request, 'home/register.html', return_message)
