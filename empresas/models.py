from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
import re


class Empresa(models.Model):
    nome = models.CharField(max_length=200)  # razão social
    sigla = models.CharField(max_length=3)
    nome_fantasia = models.CharField(max_length=200, blank=True, null=True)
    cnpj = models.CharField(max_length=14, unique=True)
    dominio = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
