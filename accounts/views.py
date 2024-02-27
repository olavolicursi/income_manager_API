from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
