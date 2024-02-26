from rest_framework import generics
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
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionListDetailSerializer
        return TransactionSerializer

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         # Exigir autenticação para solicitações POST
    #         return [permissions.IsAuthenticated()]
    #     return super().get_permissions()

    
class TransactionListFilter(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        name = self.kwargs.get("name", None)
        return Transaction.objects.filter(category_id__name__icontains=name)


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
