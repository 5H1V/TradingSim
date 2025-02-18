from django.shortcuts import render, HttpResponse
from .models import TodoItem

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def wallet(request):
    return render(request, "wallet.html")

def account(request):
    return render(request, "account.html")
