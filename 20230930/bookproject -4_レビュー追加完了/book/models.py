from django.db import models
from . import consts

# Create your models here.
CATEGORY = (("business","ビジネス"),("life","生活"),("other","その他"))
RATE_CHOICES = [(x,str(x)) for x in range(0,consts.MAX_RATE+1)]


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100,choices=CATEGORY)

    def __str__(self):
        return self.title+"："+self.text
    
class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.title+"："+self.text