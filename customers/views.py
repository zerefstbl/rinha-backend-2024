from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response

from customers.models import Transacao, SaldoClientes

from customers.serializers import TransacaoSerializer, BasicTransactionSerializer

from django.db import transaction

from datetime import datetime

import pytz

sp_tz = pytz.timezone('America/Sao_Paulo')

class NewTransactionAPIView(CreateAPIView):
    serializer_class = TransacaoSerializer

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            customer = get_object_or_404(SaldoClientes.objects.select_for_update(), id=kwargs.get('id'))
            request.data['cliente'] = customer.id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExtractAPIView(APIView):
    def get(self, request, *args, **kwargs):
        customer = SaldoClientes.objects.get(id=kwargs.get('id'))
        transactions = Transacao.objects.select_related('cliente').filter(cliente=customer).order_by('-id')[:10]
        return Response({
            "saldo": {
                "total": customer.saldo,
                "data_extrato": datetime.now(sp_tz),
                "limite": customer.limite,
            },
            "ultimas_transacoes": BasicTransactionSerializer(transactions, many=True).data
        })
