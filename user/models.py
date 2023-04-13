from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()

class Player(models.Model):
    player = models.ForeignKey(Person, on_delete=models.CASCADE)
    averageYards = models.CharField()
    averageCatches = models.CharField()
       