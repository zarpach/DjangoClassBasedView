from django.db import models
from django.contrib.auth import get_user_model
from users.models import PhotoUser

CATEGORY = (
    ('Nature', 'Природа'),
    ('Animals', 'Животные'),
    ('Cities', 'Города'),
    ('Cars', 'Машины')
)


class Photo(models.Model):
    author = models.ForeignKey(PhotoUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')  # для изображения
    name = models.CharField(max_length=255)  # для текста
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, choices=CATEGORY)


# (1) python manage.py makemigrations users
# (2) python manage.py migrate


# urls.py