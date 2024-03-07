from django.urls import path, include
from .views import (PhotoListView,
                    PhotoCreateView,
                    PhotoDetailView,
                    PhotoUpdateView,
                    PhotoDeleteView)

app_name = 'photo'

urlpatterns = [
    path('photos/', PhotoListView.as_view(), name='list'),
    path('photos/create/', PhotoCreateView.as_view(), name='create'),
    path('photos/<int:pk>', PhotoDetailView.as_view(), name='detail'),
    path('photos/update/<int:pk>', PhotoUpdateView.as_view(), name='update'),
    path('photos/delete/<int:pk>', PhotoDeleteView.as_view(), name='delete')
]
