from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.films_page, name="films"),#При переході на /fimls виконується функція films_page в views.py
    path('stream/<slug:slug>/', views.get_streaming_video, name='stream'), #Для перемотки відео
    path('<slug:slug>', views.page_film, name="films_id")#При переході на /назва фільму виконується функція page_film в views.py
]
