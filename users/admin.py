from django.contrib import admin
from .models import PhotoUser

@admin.register(PhotoUser)
class ModelNameAdmin(admin.ModelAdmin):
    pass