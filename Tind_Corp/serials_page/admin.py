from django.contrib import admin
from django.db import models
from django import forms
from .models import Base, serias

#Робимо inline class для серій
class seriasAdmin(admin.TabularInline):
    model = serias
    extra = 1#Мінімум одне inline поле


@admin.register(Base)#Декоратор для моделі Base(серіли)
class SerialsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}#Робимо так щоб робило slug
    inlines = [seriasAdmin]#Додаємо inline поле


