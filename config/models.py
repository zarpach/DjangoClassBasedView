from django.db import models
from django.contrib.auth import get_user_model

CATEGORY = (
    ('Nature', 'Природа'),
    ('Animals', 'Животные'),
    ('Cities', 'Города'),
    ('Cars', 'Машины')
)


class Photo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')  # для изображения
    name = models.CharField(max_length=255)  # для текста
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, choices=CATEGORY)


# python manage.py makemigrations
# python manage.py migrate


# urls.py