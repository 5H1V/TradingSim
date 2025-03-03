from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .models import PortfolioItem

API_KEY = ""

@csrf_exempt
def get_stock(request):
    if request.method == "POST":
        symbol = request.POST.get("symbol")
        response = requests.get(f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}")
        data = response.json()
        if "price" not in data:
            return render(request, "home.html", {"error": "Stock not found"})
        return render(request, "home.html", {"stock": {"symbol": symbol, "price": float(data["price"])}})
    return render(request, "home.html")

@csrf_exempt
def trade_stock(request):
    if request.method == "POST":
        data = json.loads(request.body)
        PortfolioItem.objects.create(symbol=data["symbol"], price=data["price"], shares=PortfolioItem[shares]+=1)
        return JsonResponse({"message": "Trade successful"})
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def get_portfolio(request):
    portfolio = list(PortfolioItem.objects.values("symbol", "price", "shares"))
    return render(request, "portfolio.html", {"portfolio": portfolio})
