from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['author', 'image', 'name', 'category', 'created_at']
    search_fields = ['name']
    list_filter = ['author', 'created_at']


# filters.py