from django.urls import path
from .views import get_stock, trade_stock, get_portfolio

urlpatterns = [
    path("", get_stock, name="get_stock"),
    path("trade/", trade_stock, name="trade_stock"),
    path("portfolio/", get_portfolio, name="get_portfolio"),
]
