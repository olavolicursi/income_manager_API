from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer, TransactionListDetailSerializer
from django_filters import rest_framework as filters


class TransactionFilter(filters.FilterSet):
    emission_date = filters.CharFilter(lookup_expr='icontains')
    category_id = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Transaction
        fields = ['emission_date', 'category_id__name']


class TransactionCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionListDetailSerializer
        return TransactionSerializer


class TransactionListFilter(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionListDetailSerializer

    def get_queryset(self):
        name = self.kwargs.get("name", None)
        return Transaction.objects.filter(category_id__name__icontains=name)


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
