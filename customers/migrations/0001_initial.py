# Generated by Django 5.0.2 on 2024-03-17 03:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaldoClientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limite', models.IntegerField()),
                ('saldo', models.IntegerField()),
            ],
            options={
                'db_table': 'saldo_clientes',
            },
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realizada_em', models.DateTimeField(auto_now_add=True)),
                ('valor', models.IntegerField()),
                ('descricao', models.CharField(max_length=10)),
                ('tipo', models.CharField(choices=[('C', 'c'), ('D', 'd')], max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacoes', to='customers.saldoclientes')),
            ],
            options={
                'db_table': 'transacoes',
            },
        ),
    ]
