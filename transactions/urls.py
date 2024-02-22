from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.TransactionCreateListView.as_view(), name='transaction-create-list'),
    path('transactions/<int:pk>', views.TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail-view'),
]