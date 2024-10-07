import requests, json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm

def index(request):
    """Домашня сторінка Test Project."""
    return render(request, 'movierating/index.html')

def new_request(request):
    """Відображення форми та здійснення запиту."""
    if request.method == 'POST':
        form = MovieForm(data=request.POST)
        data = form['title'].value()
        page = 1
        active = True
        while active:
            response = requests.get(f'https://www.omdbapi.com/?r=json&s={data}&page={page}&apikey=36cd6ae').json()
            page += 1
            with open('filename.json', 'a') as f:
                json.dump(response, f)
            if response['Response'] == 'False':
                break
            
        return redirect('movierating:results')
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movierating/new_request.html', context)

def results(request):
    """Відобразити отримані результати."""
    with open ('filename.json') as f:
        result = json.load(f)
    context = {'result': result}
    return render(request, 'movierating/results.html', context)
