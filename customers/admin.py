from django.contrib import admin

from customers.models import Transacao, SaldoClientes

admin.site.register(Transacao)
admin.site.register(SaldoClientes)
