from django.contrib import admin

# Register your models here.

from .models import Job_Listing
from django.forms import NumberInput
from django.db import models

class JobListingsConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'summary', 'qualifications', 'city', 'is_published', 'post_date')
    list_display_links = ('title', 'department')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(Job_Listing, JobListingsConfigAdmin)
