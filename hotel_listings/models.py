from django.db import models
from datetime import datetime
from . choices import city_choices

# Create your models here.
    
class Hotel_Listing(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50, choices=city_choices.items())
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=50, unique=True, blank=True)
    phone = models.CharField(max_length=20,default='00000000')    
    rooms = models.IntegerField()
    restaurants = models.IntegerField()
    facilities = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    is_onsale = models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    list_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-list_date',)
        indexes = [models.Index(fields=['list_date'])]

    def __str__(self):
        return self.name    
    
    