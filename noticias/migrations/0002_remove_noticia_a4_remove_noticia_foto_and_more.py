# Generated by Django 5.1.3 on 2024-11-21 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='a4',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='img',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='printscreen',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='link_noticia',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('IMAGEM', 'Imagem'), ('VIDEO', 'Vídeo'), ('AUDIO', 'Áudio'), ('DOCUMENTO', 'Documento')], max_length=50)),
                ('arquivo', models.FileField(upload_to='anexos/')),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anexos', to='noticias.noticia')),
            ],
        ),
    ]
