from rest_framework import generics
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryCreateListView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
