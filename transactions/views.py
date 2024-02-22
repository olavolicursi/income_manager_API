from rest_framework import generics
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionCreateListView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
