from django.contrib import admin
from .models import films

class FilmsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}#Робимо так щоб працював slug

admin.site.register(films, FilmsAdmin)#Додаємо модель в адмін-панель