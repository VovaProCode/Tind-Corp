from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home")#При переході на сайт виконується функція home в views.py
]
