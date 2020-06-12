from django.contrib.auth import get_user_model
from django.db import models

from chat.utils import attachment_upload_location


class Chat(models.Model):
    chat_type = models.CharField(max_length=64)


class Participant(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.CharField(max_length=512)
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=attachment_upload_location)
    attachment_type = models.CharField(max_length=64)

