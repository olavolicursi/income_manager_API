from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreateListView.as_view(), name='user-create-list'),
    path('users/<int:pk>', views.UserRetrieveUpdateDestroyView.as_view(), name='user-detail-view'),
]
