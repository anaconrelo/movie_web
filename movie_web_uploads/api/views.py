from movie_web_uploads.models import Movie
from movie_web_uploads.api.serializers import MovieSerializer
from rest_framework import generics

class MoviesList(generics.ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().order_by('-id')