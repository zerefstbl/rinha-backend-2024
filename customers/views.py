from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from rest_framework import status
from rest_framework.response import Response

from customers.models import Transacao, SaldoClientes

from customers.serializers import ExtratoSerializer, TransacaoSerializer


class NewTransactionAPIView(CreateAPIView):
    serializer_class = TransacaoSerializer

    def create(self, request, *args, **kwargs):
        customer = get_object_or_404(SaldoClientes, id=kwargs.get('id'))
        request.data['cliente'] = customer.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExtractAPIView(RetrieveAPIView):
    serializer_class = ExtratoSerializer

    lookup_field = 'id'

    def get_object(self):
        return get_object_or_404(SaldoClientes, id=self.kwargs.get('id'))
