from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.

class queue(models.Model):
    def __str__(self):
        return self.keyword

    keyword = models.CharField(max_length=100)
    number = models.CharField(max_length=4)
    email = models.EmailField()

class database(models.Model):
    def __str__(self):
        return self.keyword
    keyword = models.CharField(max_length=100)
    number = models.CharField(max_length=4)
    email = models.EmailField()
    time = models.DateTimeField()
    