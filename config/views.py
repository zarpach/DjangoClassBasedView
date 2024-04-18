from django.shortcuts import render, HttpResponse
from django.views.generic import (ListView,
                                  DeleteView,
                                  DetailView,
                                  UpdateView,
                                  CreateView, )
from .models import Photo
from .forms import PhotoCreationForm
from django.urls import reverse_lazy



class PhotoListView(ListView):
    paginate_by = 2
    model = Photo
    template_name = 'list.html'
    context_object_name = 'photos'


class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'create.html'
    success_url = reverse_lazy('photo:list')
    fields = ['name', 'image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
