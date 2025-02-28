from django.shortcuts import render
from django.views.decorators.cache import never_cache

from movie_web_uploads.forms import MovieForm

# Create your views here.

@never_cache
def upload_movie(request):
    form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'uploads.html', context)