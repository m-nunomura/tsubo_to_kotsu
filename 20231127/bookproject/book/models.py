from django.db import models
from . import consts

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(null=True,blank=True)
    category = models.CharField(max_length=100,choices=consts.CATEGORY)
    user = models.ForeignKey("auth.user",on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=consts.RATE_CHOISES)
    user = models.ForeignKey("auth.user",on_delete=models.CASCADE)

    def __str__(self):
        return self.title