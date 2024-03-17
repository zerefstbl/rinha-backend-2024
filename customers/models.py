from django.db import models

from customers.exceptions import InsufficientLimit

from typing import Self, List

import pytz

from django.db import transaction

sp_tz = pytz.timezone('America/Sao_Paulo')

type_choices = (
    ('C', 'c'),
    ('D', 'd')
)

class SaldoClientes(models.Model):
    limite = models.IntegerField()
    saldo = models.IntegerField()

    class Meta:
        db_table = 'saldo_clientes'


    def check_limit(self, transaction_value: int) -> bool:
        if transaction_value - self.saldo > self.limite:
            raise InsufficientLimit
        return True

    @transaction.atomic
    def transaction(self, value: int, type: str) -> Self:
        if type == 'd' and self.check_limit(value):
            self.saldo += -value
        else:
            self.saldo += value
        self.save()
        return self

    @property
    def last_ten_transactions(self) -> List:
        return self.transacoes.order_by('-realizada_em')[:10]

class Transacao(models.Model):
    realizada_em = models.DateTimeField(auto_now_add=True)
    valor = models.IntegerField()
    descricao = models.CharField(max_length=10)
    tipo = models.CharField(
        choices=type_choices,
        max_length=10,
    )
    cliente = models.ForeignKey(SaldoClientes, related_name='transacoes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'transacoes'

    def save(self, *args, **kwargs):
        self.cliente.transaction(value=self.valor, type=self.tipo)
        return super().save(*args, **kwargs)
