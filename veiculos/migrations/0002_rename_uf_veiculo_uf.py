# Generated by Django 5.1.3 on 2024-11-22 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='UF',
            new_name='uf',
        ),
    ]
