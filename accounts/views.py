from rest_framework import generics
from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountCreateListView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)#
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)#
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
