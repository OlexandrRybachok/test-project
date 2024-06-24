import requests, json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Movie

def index(request):
    """Домашня сторінка Test Project."""
    return render(request, 'movierating/index.html', {
        'form': Movie(), 
        'title': new_request,
        })

def new_request(request):
    """Створит поле для вводу і відобразити отримані результати."""
    if request.method == 'POST':
        form = Movie(requests.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            data = requests.get(f'http://www.omdbapi.com/?t={title}&apikey=36cd6ae')
            moviedata = data.json()
            return HttpResponse(moviedata)
    else:
        form = Movie()

    return render(request, 'movierating/index.html', {"form": form})