from rest_framework import serializers
from customers.models import SaldoClientes, Transacao

from datetime import datetime

import pytz

sp_tz = pytz.timezone('America/Sao_Paulo')

class BasicTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        exclude = ['id', 'cliente']

class TransacaoSerializer(serializers.Serializer):
    valor = serializers.IntegerField(write_only=True)
    tipo = serializers.CharField(write_only=True)
    descricao = serializers.CharField(write_only=True, max_length=10)
    limite = serializers.IntegerField(source='cliente.limite', read_only=True)
    saldo = serializers.IntegerField(source='cliente.saldo', read_only=True)
    cliente = serializers.PrimaryKeyRelatedField(queryset=SaldoClientes.objects.all(), write_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Transacao.objects.create(**validated_data)

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaldoClientes
        fields = ['last_ten_transactions']

    def to_representation(self, instance):
        representation = {
            "saldo": {
                "total": instance.saldo,
                "data_extrato": datetime.now(sp_tz),
                "limite": instance.limite,
            },
            "ultimas_transacoes": [
                BasicTransactionSerializer(instance.last_ten_transactions, many=True).data
            ]
        }
        return representation

