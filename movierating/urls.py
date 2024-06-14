"""Defines URL patterns for movierating."""
from django.urls import path

from . import views

app_name = 'movierating'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that makes API call.
    path('new_request/', views.new_request, name='new_request'),
]
