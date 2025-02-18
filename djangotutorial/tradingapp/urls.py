from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="Login"),
    path("home/", views.home, name="Home"),
    path("account/", views.account, name="Account"),
    path("wallet/", views.wallet, name="Wallet"),
]