from django.shortcuts import render
from .models import films
from .services import open_file
from django.http import StreamingHttpResponse
from django.http import JsonResponse


#Функція films_page яка виконується при переході на /films
def films_page(request):
    list_films = films.objects.all()#Беремо всі записи із БД(із БД фільмів)
    return render(request, "films_page/film.html", {"films_list": list_films}) #Рендер сторінки з передачою list_films на сторінку

#Функція page_film яка виконується при переході на /назва фільму
def page_film(request, slug):
    shablon_list_films = films.objects.filter(slug=slug).first()#Беремо запис із БД по фільтру slug(назва фільму)
    return render(request, "films_page/film_shablon.html", {"list_shablon": shablon_list_films})#Рендер сторінки з передачою shablon_list_films

def get_streaming_video(request, slug):
    file, status_code, content_length, content_range = open_file(request, slug)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response
