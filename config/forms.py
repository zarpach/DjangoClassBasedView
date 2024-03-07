from django import forms
from .models import Photo


# forms.py
class PhotoCreationForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
