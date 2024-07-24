import requests, json
from django.shortcuts import render

def index(request):
    """Домашня сторінка Test Project."""
    return render(request, 'movierating/index.html')

def new_request(request):
    """Відобразити отримані результати."""
    response = requests.get(f'https://www.omdbapi.com/?r=json&t=batman&apikey=36cd6ae').json()
    with open(f'filename.json', 'w') as f:
        json.dump(response, f)
    with open (f'filename.json') as f:
        results = json.load(f)
    context = {'results': results}
    return render(request, 'movierating/new_request.html', context)