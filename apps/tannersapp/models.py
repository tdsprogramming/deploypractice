from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    year_established = models.CharField(max_length=4)

class Musician(models.Model):
    name = models.CharField(max_length=200)
    instrument = models.CharField(max_length = 20)
    age = models.IntegerField()
    band = models.ManyToManyField(Band)