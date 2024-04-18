import django_filters
from .models import Photo


class PhotoSearch(django_filters.FilterSet):
    class Meta:
        model = Photo
        fields = ['name', 'author', 'category']
# filters.py
