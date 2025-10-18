from django.db import models
from datetime import datetime

# Create your models here.

class Article(models.Model):
    heading = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    contents = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)    
    is_published = models.BooleanField(default=True)    
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.heading
