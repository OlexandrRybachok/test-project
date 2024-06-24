from django import forms

class Movie(forms.Form):
    title = forms.CharField(label="Title", max_length=200)