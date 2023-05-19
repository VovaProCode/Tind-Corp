from django.shortcuts import render
from .models import Base, serias
from films_page.models import films
from .services import open_file
from django.http import StreamingHttpResponse
from django.http import JsonResponse

#Функція для переходу на сторінку /serials
def serials_page(request):
    list_serials = Base.objects.all()#Беремо із БД всі записи
    return render(request, "serials_page/serial.html", {"serials_list": list_serials})#Рендер сторінки з передачою list_serials

#Функція для переходу на сторінку /назва серіала
def page_serial(request, slug):
    shablon_list = Base.objects.filter(slug=slug).first()#Беремо із БД запис по фільтру slug
    serias_list = serias.objects.filter(Base=shablon_list)#Беремо із БД серій запис по фільтру shablon_lit
    return render(request, "serials_page/serial_shablon.html", {"list_shablon": shablon_list, "list_serias": serias_list})#Рендер сторінки
    # з передачою shablon_list і serias_list

#Функція для переходу на сторінку /search а також для пошуку
def Search_django(request):
    if request.method == "POST": #Якщо користувач відправив POST request
        searched = request.POST["searched"]#Беремо запрос користувача(те що він ввів)
        search_items = Base.objects.filter(title__iregex=searched)#Беремо із БД записи по фільтру searched
        search_items_films = films.objects.filter(title__iregex=searched)#Те саме що зверху робимо але уже з бД фільмів
        return render(request, "serials_page/search.html", {"searched": searched, "search_items": search_items, "search_items_films": search_items_films})#Рендер
        #сторінки з передачою searched, search_items, search_items_films
    elif "term" in request.GET:
        qs = Base.objects.filter(title__iregex=request.GET.get("term"))#Беремо із БД записи по фільтру term
        qs_films = films.objects.filter(title__iregex=request.GET.get("term"))#Беремо із БД фільмів записи по фільтру term
        titles = list()
        for i in qs:
            titles.append(i.title)
        for d in qs_films:
            titles.append(d.title)
        #Додаємо всі результати перебору в список titles
        return JsonResponse(titles, safe=False)
    else:
        return render(request, "serials_page/search.html", {})#Якщо користувач нічого не ввів то буде звичайний рендер сторінки

#Функція для перемотки відео
def get_streaming_video(request, slug):
    file, status_code, content_length, content_range = open_file(request, slug)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


# class Search_django(ListView):
#     template_name = "serials_page/search.html" # здесь была опечатка
#     context_object_name = "news"
#     paginate_by = 5
#
#     def get_queryset(self):
#         return Base.objects.filter(title__iregex=self.request.GET.get("q"))
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["q"] = self.request.GET.get("q")
#         return context
