from django.shortcuts import render
from django.views.decorators.cache import never_cache

from movie_web.views import is_ajax
from movie_web_uploads.forms import MovieForm
from django.http import JsonResponse

# Create your views here.
