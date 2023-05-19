from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Search_django

urlpatterns = [
    path("", views.serials_page, name="serials"), #При переході на сторінку /serials виконується функція serials_page в views.py
    path('stream/<slug:slug>/', views.get_streaming_video, name='stream'), #Для перемотки відео
    path('<slug:slug>', views.page_serial, name="serials_id"), #При переході на сторніку /назва серіалу виконується функція page_serial в views.py
    path('search/', views.Search_django, name="search_qqq")#При переході на сторінку /search виконується функція Search_django в views.py
]
