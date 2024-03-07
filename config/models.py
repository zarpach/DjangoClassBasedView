from django.db import models

CATEGORY = (
    ('Nature', 'Природа'),
    ('Animals', 'Животные'),
    ('Cities', 'Города'),
    ('Cars', 'Машины')
)


class Photo(models.Model):
    image = models.ImageField(upload_to='media/')  # для изображения
    name = models.CharField(max_length=255)  # для текста
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, choices=CATEGORY)


# urls.py