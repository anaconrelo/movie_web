from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache

from movie_web.movie_web_uploads.forms import MovieForm
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

@never_cache
def uploads(request):
    form = MovieForm()
    context = {
        'heading': 'Upload Movie',
        'form': form,
    }
    return render(request, 'uploads.html', context)

@never_cache
def upload_movie_form(request):
    if is_ajax(request):
        if request.method == 'POST':
            try:
                form = MovieForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return JsonResponse({'result': 'success'})
                else:
                    print(form.errors)
                    return JsonResponse({'result': 'failed', 'error': form.errors})
            except Exception as e:
                print(e)
                return JsonResponse({'result': 'failed', 'error': str(e)})
    return JsonResponse({'result':'failed','error': 'Invalid request'})