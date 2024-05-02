from django.db import models
from django.contrib.auth.models import (AbstractUser,
                                        PermissionsMixin)


class PhotoUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=155, unique=True)
    email = models.EmailField()


