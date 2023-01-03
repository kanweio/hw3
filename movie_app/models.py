from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=5)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True, related_name='reviews')


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True, related_name='movies')

    def __str__(self):
        return self.title
