from django.urls import path

from . import views

urlpatterns = [
    path("", views.hompage, name="home"),
    path("login/", views.login, name="login"),
]
