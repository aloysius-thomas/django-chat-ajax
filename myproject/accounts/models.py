from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.utils import user_image_upload_location


class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    avatar = models.ImageField(upload_to=user_image_upload_location)

    def __str__(self):
        return self.get_full_name()
