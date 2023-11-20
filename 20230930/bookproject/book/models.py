from django.db import models
from .consts import MAX_RATE

# Create your models here.
CATEGORY = (("business","ビジネス"),("life","生活"),("other","その他"))
RATE_CHOICES = [(x,str(x)) for x in range(1,MAX_RATE)]


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100,choices=CATEGORY)

    def __str__(self):
        return self.title+"："+self.text
    
class BookReview(models.Model):
    book_info = models.ForeignKey(Book,on_delete=models.CASCADE)
    review_title = models.CharField(max_length=100)
    review_text = models.TextField()
    review_rate = models.IntegerField(choices=RATE_CHOICES)
    review_user = models.ForeignKey("auth.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.review_title+"："+self.review_text