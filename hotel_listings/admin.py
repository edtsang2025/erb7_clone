from django.contrib import admin

# Register your models here.

from .models import Hotel_Listing
from django.forms import NumberInput
from django.db import models

class Hotel_listingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'email', 'phone', 'rooms', 'restaurants', 'facilities', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'is_published', 'is_onsale', 'discount')
    list_display_links = ('name', 'email', 'phone')
    list_editable = ('is_published','is_onsale',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Hotel_Listing, Hotel_listingAdmin)
