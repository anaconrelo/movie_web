from django.urls import include, path

from movie_web_uploads.views import uploads, upload_movie_form

urlpatterns = [
    path('ups/', uploads, name='uploads'),
    path('upload_movie', upload_movie_form, name='uploads_movie'),
]