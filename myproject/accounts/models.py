from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from accounts.utils import user_image_upload_location


class User(AbstractUser):
    username = models.EmailField(unique=True, help_text="")
    date_of_birth = models.DateField()
    # avatar = models.ImageField(upload_to=user_image_upload_location)

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('user-info', kwargs={'id': self.id})
