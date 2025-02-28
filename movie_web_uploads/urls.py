from django.urls import include, path

from movie_web_uploads.views import upload_movie

urlpatterns = [
    path('', upload_movie, name='uploads'),
]