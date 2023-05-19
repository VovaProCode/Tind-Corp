from django.shortcuts import render

#Функція home яка викликається при переході на сайт
def home(request):
    return render(request, "home/home.html")#Рендер сторінки

# Create your views here.
