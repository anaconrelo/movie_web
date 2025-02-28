from django import forms

from movie_web_uploads.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'movie', 'image']
        labels = {
            'title': 'Tajuk',
            'description': 'Penerangan',
            'movie': 'Fail Video',
            'image': 'Gambar',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'movie': forms.FileInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
    