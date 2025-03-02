from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache

from movie_web_uploads.forms import MovieForm
from movie_web_uploads.models import Movie
from movie_web_uploads.forms import MovieForm
from django.http import JsonResponse

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
@never_cache
def landing_page(request):
    return redirect('movies')

@never_cache
def movies(request):
    movies = Movie.objects.all().order_by('-id')
    context = {
        'heading': 'Anaconrelo Movie Web',
        'movies': movies,
    }
    return render(request, 'movies.html', context)