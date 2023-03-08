from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect

def index(request):
    return HttpResponse('Страница приложения women.')

def categories(request, catid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if year > '2022':
        return redirect('home', permanent=True)
        #raise Http404()

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
