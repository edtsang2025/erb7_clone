from django.contrib import admin

# Register your models here.

from .models import Doctor
from django.forms import NumberInput
from django.db import models

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_mvp', 'hire_date')
    list_display_links = ('name', 'email', 'phone')
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 25

# admin.site.register(Doctor, DoctorAdmin)
