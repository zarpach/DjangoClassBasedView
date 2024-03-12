from django.shortcuts import render
from django.views.generic import (ListView,
                                  DeleteView,
                                  DetailView,
                                  UpdateView,
                                  CreateView,)
from .models import Photo
from .forms import PhotoCreationForm
from django.urls import reverse_lazy


class PhotoListView(ListView):
    model = Photo
    template_name = 'list.html'
    context_object_name = 'photos'


class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'create.html'
    form_class = PhotoCreationForm
    success_url = reverse_lazy('photo:list')


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'detail.html'
    context_object_name = 'photo'


class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('photo:list')


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('photo:list')







# django-admin startapp users
