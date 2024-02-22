from django.contrib import admin
from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'value', 'emission_date', 'payment_date', 'time', 'type')
