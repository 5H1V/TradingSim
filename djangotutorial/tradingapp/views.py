from django.shortcuts import render, HttpResponse
from .models import TodoItem

def login(request):
    return render(request, "main/login.html")

def home(request):
    return render(request, "main/home.html")

def wallet(request):
    return render(request, "main/wallet.html")
