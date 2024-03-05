from django.shortcuts import render
from django.views.generic import ListView


class PhotoListView(ListView):
    template_name = 'index.html'

