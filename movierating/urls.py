"""Визначити URL шаблони для movierating."""
from django.urls import path

from . import views

app_name = 'movierating'
urlpatterns = [
    #Home page
    path('', views.index, name=''),
    #Page that makes API call.
    path('', views.new_request, name=''),
]
