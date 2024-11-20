from django.db import models
from empresas.models import Empresa


class Assinatura(models.Model):
    # Relacionamento com a empresa responsável
    empresa_responsavel = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, related_name='assinaturas')

    # Informações gerais
    nome = models.CharField(max_length=200)
    # Usando o termo em português
    descricao = models.TextField(blank=True, null=True)
    cnpj_cpf = models.CharField(
        max_length=14, blank=True, null=True)  # CNPJ ou CPF
    razao_social = models.CharField(max_length=255, blank=True, null=True)
    codigo_do_assinante = models.CharField(
        max_length=100, blank=True, null=True)
    contrato = models.CharField(max_length=255, blank=True, null=True)

    # Valores e pagamentos
    valor_total = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    forma_de_pagamento = models.CharField(
        max_length=100, blank=True, null=True)
    vigencia = models.DateTimeField(blank=True, null=True)
    informacoes_sobre_pagamento = models.TextField(blank=True, null=True)

    # Credenciais de acesso
    usuario = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)

    # Contato
    # Suporta formatos internacionais
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)

    # Observações
    observacoes_sobre_o_acesso = models.TextField(blank=True, null=True)
    contato_do_veiculo = models.CharField(
        max_length=255, blank=True, null=True)

    # Campos de auditoria
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
