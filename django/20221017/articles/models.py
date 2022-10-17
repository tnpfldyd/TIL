from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
# Create your models here.

class Profile(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(
        upload_to='thumbimage/',
        blank=True,
        processors=[Thumbnail(300, 200)],
        format = 'JPEG',
        options = {'quality': 90},
    )