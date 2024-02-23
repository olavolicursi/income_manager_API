from django.db import models
from accounts.models import Account
from categories.models import Category


TRANSACTION_TYPE_CHOICES = (
    ('C', 'C'),
    ('D', 'D')
)


class Transaction(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.FloatField()
    emission_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
    description = models.TextField(null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
