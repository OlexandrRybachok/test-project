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
        year = form['year'].value()
        responses = []
        page = 1
        active = True
        while active:
            response = requests.get(f'https://www.omdbapi.com/?r=json&s={data}&page={page}&y={year}&apikey=36cd6ae').json()
            page += 1
            responses.append(response)
            if response['Response'] == 'False':
                break
        request.session['responses'] = responses
        return redirect('movierating:results')
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movierating/new_request.html', context)

def results(request):
    """Відобразити отримані результати."""
    result = request.session['responses']
    context = {'result': result}
    return render(request, 'movierating/results.html', context)
