from django.db import models
from . import consts

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100,choices=consts.CATEGORY)

    def __str__(self):
        return self.title