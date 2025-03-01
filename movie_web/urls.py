from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from movie_web.views import landing_page, movies, uploads, upload_movie_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('movies/', movies, name='movies'),
    path('uploads/', uploads, name='uploads'),
    path('upload_movie', upload_movie_form, name='uploads_movie'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
