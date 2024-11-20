# Generated by Django 5.1.3 on 2024-11-19 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodicidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeVeiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('sigla', models.CharField(blank=True, max_length=2, null=True, unique=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=20)),
                ('grande_imprensa', models.BooleanField(default=False)),
                ('pais', models.CharField(default='Brasil', max_length=100)),
                ('UF', models.CharField(max_length=2)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('prioritario', models.BooleanField(default=False)),
                ('valor_publicitario_padrao', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('altura_cm', models.IntegerField(blank=True, null=True)),
                ('largura_cm', models.IntegerField(blank=True, null=True)),
                ('endereco_do_site', models.URLField(blank=True, null=True)),
                ('identificador_url', models.CharField(blank=True, max_length=255, null=True)),
                ('endereco_do_flip', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_minimo_de_noticias', models.IntegerField(blank=True, null=True)),
                ('periodo_maximo_sem_noticia', models.IntegerField(blank=True, null=True)),
                ('url_da_stream', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('periodicidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='veiculos.periodicidade')),
                ('tipodeveiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='veiculos.tipodeveiculo')),
            ],
        ),
    ]
