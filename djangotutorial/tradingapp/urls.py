from django.urls import path
from .views import (
    StockDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    PaymentView,
    wallet,
    account,
)

app_name = 'tradingapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('stock/<slug>/', StockDetailView.as_view(), name='stock'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('wallet/', wallet, name='wallet'),
    path('account/', account, name='account'),
]