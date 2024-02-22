from django.db import models
from accounts.models import Account
from categories.models import Category


TRANSACTION_TYPE_CHOICES = (
    ('C', 'C'),
    ('D', 'D')
)


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.FloatField()
    emission_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    time = models.TimeField()
    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
