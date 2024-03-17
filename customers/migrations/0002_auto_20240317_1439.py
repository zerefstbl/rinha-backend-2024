# Generated by Django 5.0.2 on 2024-03-17 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    def create_default_users(apps, _):
        from customers.models import SaldoClientes

        SaldoClientes.objects.create(
            id=1,
            saldo=0,
            limite=100000
        )
        SaldoClientes.objects.create(
            id=2,
            saldo=0,
            limite=80000
        )
        SaldoClientes.objects.create(
            id=3,
            saldo=0,
            limite=1000000
        )
        SaldoClientes.objects.create(
            id=4,
            saldo=0,
            limite=10000000
        )
        SaldoClientes.objects.create(
            id=5,
            saldo=0,
            limite=500000
        )

    operations = [
        migrations.RunPython(create_default_users),
    ]