from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):
        return self.user_id.username
