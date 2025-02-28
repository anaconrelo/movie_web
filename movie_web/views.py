from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache

from movie_web_uploads.models import Movie

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
@never_cache
def landing_page(request):
    movies = Movie.objects.all().order_by('-id')
    context = {
        'heading': 'Anaconrelo Movie Web',
        'movies': movies,
    }
    return render(request, 'movies.html', context)