import requests, json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm

def index(request):
    """Домашня сторінка Test Project."""
    return render(request, 'movierating/index.html')

def new_request(request):
    """Відображення форми для здійснення запиту."""
    if request.method == 'POST':
        form = MovieForm(data=request.POST)
        data = form['title'].value()
        response = requests.get(f'https://www.omdbapi.com/?r=json&s={data}&apikey=36cd6ae').json()
        with open(f'filename.json', 'w') as f:
            json.dump(response, f)
        return redirect('movierating:results')
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movierating/new_request.html', context)

def results(request):
    """Відобразити отримані результати."""
    with open (f'filename.json') as f:
        results = json.load(f)
    context = {'results': results}
    return render(request, 'movierating/results.html', context)
