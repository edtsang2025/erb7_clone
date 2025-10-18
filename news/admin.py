from django.contrib import admin

# Register your models here.

from .models import Article
from django.forms import NumberInput
from django.db import models

class NewsConfigAdmin(admin.ModelAdmin):
    list_display = ('heading', 'summary', 'contents', 'photo_1', 'photo_2', 'is_published', 'post_date')
    list_display_links = ('heading',)
    list_editable = ('is_published',)
    search_fields = ('heading',)
    list_per_page = 25

admin.site.register(Article, NewsConfigAdmin)
