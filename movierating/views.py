import requests
from django.shortcuts import render, redirect

# from .models import Movie
from .forms import MovieForm

def index(request):
    """The home page for Test Project."""
    return render(request, 'movierating/index.html')

def new_request(request):
    """Show fields for input."""
    if request.method != 'POST':
        form = f'http://www.omdbapi.com/?t={MovieForm()}&apikey=36cd6ae'
    else:
        form = f'http://www.omdbapi.com/?t={MovieForm(data=request.POST)}&apikey=36cd6ae'
        if form.is_valid():
            form.save()
            return redirect('movierating:new_request')

        # r = requests.get(f'https://http://127.0.0.1:8000/{url}/save', params=request.GET)

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'movierating/new_request.html', context)