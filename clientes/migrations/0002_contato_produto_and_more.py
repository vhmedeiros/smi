# Generated by Django 5.1.3 on 2024-11-20 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('departamento', models.CharField(blank=True, max_length=200, null=True)),
                ('cargo', models.CharField(blank=True, max_length=200, null=True)),
                ('contato', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('observacoes', models.CharField(blank=True, max_length=200, null=True)),
                ('tipo', models.CharField(choices=[('Financeiro', 'Financeiro'), ('Operacional', 'Operacional')], default='Financeiro', max_length=20)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='contrato',
            old_name='vigencia',
            new_name='fim_vigencia',
        ),
        migrations.RenameField(
            model_name='contrato',
            old_name='contrato_assinado',
            new_name='is_assinado',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='envio_nf',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='status',
        ),
        migrations.AddField(
            model_name='contrato',
            name='inicio_vigencia',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='documentos',
            field=models.FileField(blank=True, null=True, upload_to='contratos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='informacoes_adicionais',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='produtos',
        ),
        migrations.AlterField(
            model_name='contrato',
            name='contato_financeiro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='financeiro_contrato', to='clientes.contato'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='contato_operacional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='operacional_contrato', to='clientes.contato'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='gestor_contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gestor_contrato', to='clientes.contato'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='produtos',
            field=models.ManyToManyField(blank=True, related_name='contratos', to='clientes.produto'),
        ),
        migrations.DeleteModel(
            name='ContatoFinanceiro',
        ),
        migrations.DeleteModel(
            name='ContatoOperacional',
        ),
        migrations.DeleteModel(
            name='GestorContrato',
        ),
    ]