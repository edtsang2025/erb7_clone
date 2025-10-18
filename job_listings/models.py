from django.db import models
from datetime import datetime
from hotel_listings.choices import city_choices
from . choices import category_choices

# Create your models here.

class Job_Listing(models.Model):
    title = models.CharField(max_length=200)
    department = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    category = models.TextField(max_length=50, choices=category_choices.items())    
    city = models.CharField(max_length=50, choices=city_choices.items())
    is_published = models.BooleanField(default=True)    
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.title
