from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField()
