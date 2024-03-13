from rest_framework import serializers
from transactions.models import Transaction
from categories.serializers import CategorySerializer
from accounts.serializers import AccountSerializer


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionListDetailSerializer(serializers.ModelSerializer):
    account_id = AccountSerializer()
    category_id = CategorySerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'account_id', 'value', 'emission_date', 'payment_date', 'due_date', 'time', 'type',
                  'description', 'category_id']
