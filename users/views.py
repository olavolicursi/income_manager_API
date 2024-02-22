from rest_framework import generics
from django.contrib.auth.models import User
from users.serializers import UserSerializer


class UserCreateListView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
