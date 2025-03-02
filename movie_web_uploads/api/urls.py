from django.urls import path
from movie_web_uploads.api import views

urlpatterns = [
    path('list/', views.MoviesList.as_view()),
]
