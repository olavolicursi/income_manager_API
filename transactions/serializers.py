from rest_framework import serializers
from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

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