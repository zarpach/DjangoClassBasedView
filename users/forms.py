from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PhotoUser


# forms.py
class UserForm(UserCreationForm):
    class Meta:
        model = PhotoUser
        fields = ['username', 'email']