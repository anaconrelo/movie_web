import os
from django.db import models
from django.forms import ValidationError

def validate_extension_movie(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Hanya fail MP4 sahaja.')
    
def validate_extension_image(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.PNG', '.JPG', '.JPEG', '.GIF', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Hanya fail MP4 sahaja.')
    
movies = 'movie/%Y/%m/'
images = 'movieimage/%Y/%m/'
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    movie = models.FileField(upload_to=movies, validators=[validate_extension_movie])
    image = models.FileField(upload_to=images, validators=[validate_extension_image])

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return self.title