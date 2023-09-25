# telegram_bot_app/models.py
from django.db import models
from django.contrib.auth.models import User

class TelegramBot(models.Model):
    token = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

