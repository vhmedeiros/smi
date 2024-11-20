# Generated by Django 5.1.3 on 2024-11-19 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('cnpj_cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('razao_social', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_do_assinante', models.CharField(blank=True, max_length=100, null=True)),
                ('contrato', models.CharField(blank=True, max_length=255, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('forma_de_pagamento', models.CharField(blank=True, max_length=100, null=True)),
                ('vigencia', models.DateTimeField(blank=True, null=True)),
                ('informacoes_sobre_pagamento', models.TextField(blank=True, null=True)),
                ('usuario', models.CharField(blank=True, max_length=100, null=True)),
                ('senha', models.CharField(blank=True, max_length=100, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('site', models.CharField(blank=True, max_length=255, null=True)),
                ('observacoes_sobre_o_acesso', models.TextField(blank=True, null=True)),
                ('contato_do_veiculo', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assinaturas', to='empresas.empresa')),
            ],
        ),
    ]
