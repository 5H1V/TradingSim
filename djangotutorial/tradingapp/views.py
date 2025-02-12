from django.shortcuts import render, HttpResponse
from .models import TodoItem

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def wallet(request):
    items = TodoItem.objects.all()
    return render(request, "wallet.html", {"wallet": items})
