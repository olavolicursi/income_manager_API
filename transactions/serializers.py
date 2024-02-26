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

    # def create(self, validated_data):
    #     # Remova 'account' do validated_data para evitar o erro
    #     account = validated_data.pop('account', None)

    #     # Crie a transação
    #     transaction = Transaction.objects.create(**validated_data)

    #     # Se 'user' estiver presente, ajuste o saldo do usuário
    #     if account:
    #         if type == "D":
    #             account.balance -= transaction.value
    #         elif type == "C":
    #             account.balance += transaction.value
    #         account.save()

    #     return transaction