from django.db import models

class Genre(models.Model):
    title = models.TextField()

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Movie(models.Model):
    director = models.ForeignKey('Director' , on_delete = models.CASCADE)
    genre = models.ForeignKey('Genre' , on_delete = models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()
    screening = models.BooleanField()

