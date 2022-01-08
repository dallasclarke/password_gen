from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    return render(req, "generator/home.html", {"password": "fd3920fds"})

def password(req):
    return render(req, "generator/password.html")