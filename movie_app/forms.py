from .models import Movie
from django import forms

class FormsMovies(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','desc','img']
