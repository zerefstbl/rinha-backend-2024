from django.urls import path

from customers.views import NewTransactionAPIView, ExtractAPIView

urlpatterns = [
    path('<int:id>/transacoes', NewTransactionAPIView.as_view()),
    path('<int:id>/extrato', ExtractAPIView.as_view()),
]

