from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from movie_web.views import landing_page, movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('movies/', movies, name='movies'),
    path('uploadmovie/', include('movie_web_uploads.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
