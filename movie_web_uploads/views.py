from django.shortcuts import render
from django.views.decorators.cache import never_cache

from movie_web.views import is_ajax
from movie_web_uploads.forms import MovieForm
from django.http import JsonResponse

# Create your views here.
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