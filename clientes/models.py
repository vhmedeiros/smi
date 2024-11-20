# from django.db import models
# # Import para validações de intervalo
# from django.core.validators import MinValueValidator, MaxValueValidator
# from empresas.models import Empresa  # Import do modelo Empresa


# # Modelo de Cliente
# class Cliente(models.Model):
#     # Dados de cadastro do cliente
#     razao_social = models.CharField(max_length=200)  # Nome da empresa/cliente
#     cnpj_cpf = models.CharField(
#         max_length=14, unique=True)  # CNPJ ou CPF único
#     inscricao_estadual = models.CharField(
#         # Inscrição estadual (opcional)
#         max_length=9, unique=True, null=True, blank=True)
#     inscricao_municipal = models.CharField(
#         # Inscrição municipal (opcional)
#         max_length=13, unique=True, null=True, blank=True)

#     # Endereço do cliente
#     logradouro = models.CharField(max_length=200)  # Rua ou avenida
#     numero = models.CharField(max_length=10)  # Número do endereço
#     complemento = models.CharField(
#         max_length=200, null=True, blank=True)  # Complemento (opcional)
#     bairro = models.CharField(max_length=30)  # Bairro
#     cep = models.CharField(max_length=9)  # CEP no formato
#     pais = models.CharField(max_length=100, default='Brasil')  # País
#     # Unidade Federativa (estado) - Ex.: 'SP'
#     UF = models.CharField(max_length=2)
#     cidade = models.CharField(
#         max_length=100, blank=True, null=True)  # Cidade (opcional)
#     contato_1 = models.CharField(max_length=20)  # Telefone principal
#     # Telefone secundário (opcional)
#     contato_2 = models.CharField(max_length=20, null=True, blank=True)
#     email = models.EmailField()  # E-mail do cliente

#     # Configurações do modelo
#     class Meta:
#         # Ordenação padrão pelo nome da razão social
#         ordering = ['razao_social']

#     # Representação textual
#     def __str__(self):
#         return self.razao_social


# # Modelo de Gestor do Contrato
# class GestorContrato(models.Model):
#     nome = models.CharField(max_length=200)  # Nome do gestor
#     departamento = models.CharField(
#         max_length=200, null=True, blank=True)  # Departamento (opcional)
#     cargo = models.CharField(max_length=200, null=True,
#                              blank=True)  # Cargo (opcional)
#     contato = models.CharField(max_length=20)  # Telefone
#     email = models.EmailField()  # E-mail
#     # Observações adicionais (opcional)
#     observacoes = models.CharField(max_length=200, null=True, blank=True)

#     class Meta:
#         ordering = ['nome']  # Ordenação padrão pelo nome do gestor

#     def __str__(self):
#         return self.nome


# # Modelo de Contato Financeiro
# class ContatoFinanceiro(models.Model):
#     # Nome do contato financeiro
#     nome = models.CharField(max_length=200, null=True, blank=True)
#     departamento = models.CharField(
#         max_length=200, null=True, blank=True)  # Departamento (opcional)
#     cargo = models.CharField(max_length=200, null=True,
#                              blank=True)  # Cargo (opcional)
#     contato = models.CharField(
#         max_length=20, null=True, blank=True)  # Telefone (opcional)
#     email = models.EmailField(null=True, blank=True)  # E-mail (opcional)
#     # Observações adicionais (opcional)
#     observacoes = models.CharField(max_length=200, null=True, blank=True)

#     class Meta:
#         ordering = ['nome']  # Ordenação padrão pelo nome do contato

#     def __str__(self):
#         return self.nome


# # Modelo de Contato Operacional
# class ContatoOperacional(models.Model):
#     # Nome do contato operacional
#     nome = models.CharField(max_length=200, null=True, blank=True)
#     departamento = models.CharField(
#         max_length=200, null=True, blank=True)  # Departamento (opcional)
#     cargo = models.CharField(max_length=200, null=True,
#                              blank=True)  # Cargo (opcional)
#     contato = models.CharField(
#         max_length=20, null=True, blank=True)  # Telefone (opcional)
#     email = models.EmailField(null=True, blank=True)  # E-mail (opcional)
#     # Observações adicionais (opcional)
#     observacoes = models.CharField(max_length=200, null=True, blank=True)

#     class Meta:
#         ordering = ['nome']  # Ordenação padrão pelo nome do contato

#     def __str__(self):
#         return self.nome


# # Modelo de Contrato
# class Contrato(models.Model):
#     # Relacionamentos
#     cliente = models.ForeignKey(
#         Cliente, on_delete=models.PROTECT, related_name='contratos')  # Cliente associado
#     empresa_contratada = models.ForeignKey(
#         Empresa, on_delete=models.PROTECT, related_name='contratos')  # Empresa contratada
#     gestor_contrato = models.ForeignKey(
#         GestorContrato, on_delete=models.PROTECT, related_name='contratos')  # Gestor do contrato
#     contato_financeiro = models.ForeignKey(
#         # Contato financeiro
#         ContatoFinanceiro, on_delete=models.PROTECT, related_name='contratos')
#     contato_operacional = models.ForeignKey(
#         # Contato operacional
#         ContatoOperacional, on_delete=models.PROTECT, related_name='contratos')

#     # Campos gerais
#     # Número identificador do contrato
#     numero = models.CharField(max_length=60)
#     descricao = models.TextField()  # Descrição geral do contrato
#     objeto = models.TextField()  # Objeto do contrato (ex.: serviço, produto)
#     informacoes_adicionais = models.TextField()  # Informações complementares
#     status = models.CharField(
#         max_length=20,
#         # Status do contrato
#         choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')],
#         default='Ativo'
#     )

#     # Campos adicionais
#     vigencia = models.DateField()  # Data de vigência do contrato
#     contrato_assinado = models.BooleanField(
#         default=False)  # Indica se o contrato foi assinado
#     cobranca = models.CharField(
#         max_length=20,
#         choices=[('Mensal', 'Mensal'), ('Trimestral', 'Trimestral'),
#                  ('Anual', 'Anual')],  # Tipo de cobrança
#         default='Mensal'
#     )
#     # Indica se o contrato é prorrogável
#     prorrogacao = models.BooleanField(default=False)
#     # Valor total do contrato
#     valor = models.DecimalField(max_digits=15, decimal_places=2)
#     dia_pagamento = dia_emissao_nf = models.IntegerField(
#         null=True,
#         blank=True,
#         validators=[
#             MinValueValidator(1),  # Dia mínimo
#             MaxValueValidator(31)  # Dia máximo
#         ],
#         help_text="Escolha o dia do mês (1-31) para pagamento."
#     )
#     # Indica se a nota fiscal foi enviada
#     envio_nf = models.BooleanField(default=False)
#     dia_emissao_nf = models.IntegerField(
#         null=True,
#         blank=True,
#         validators=[
#             MinValueValidator(1),  # Dia mínimo
#             MaxValueValidator(31)  # Dia máximo
#         ],
#         help_text="Escolha o dia do mês (1-31) para emissão da NF."
#     )  # Dia do mês para emissão de NF

#     # Produtos relacionados ao contrato
#     # implementar - tem que ser uma caixinha que marca as coisas
#     produtos = models.TextField(null=True, blank=True)

#     documentos = models.FileField(
#         upload_to='contratos/documentos/', null=True, blank=True)  # Documentos anexados
#     # # Lista de eventos relacionados ao contrato
#     # eventos = models.TextField(null=True, blank=True)

#     # Configurações do modelo
#     class Meta:
#         # Ordenação padrão por cliente e número do contrato
#         ordering = ['cliente', 'numero']

#     # Representação textual
#     def __str__(self):
#         return f"Contrato {self.numero} - {self.cliente.razao_social}"


from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from empresas.models import Empresa


# Mixin para endereço
class EnderecoMixin(models.Model):
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=9)
    pais = models.CharField(max_length=100, default='Brasil')
    UF = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


# Modelo de Cliente
class Cliente(EnderecoMixin):
    razao_social = models.CharField(max_length=200)
    cnpj_cpf = models.CharField(max_length=14, unique=True)
    inscricao_estadual = models.CharField(
        max_length=9, unique=True, null=True, blank=True
    )
    inscricao_municipal = models.CharField(
        max_length=13, unique=True, null=True, blank=True
    )
    contato_1 = models.CharField(max_length=20)
    contato_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()

    class Meta:
        ordering = ['razao_social']

    def __str__(self):
        return self.razao_social


# Modelo de Contato
class Contato(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    departamento = models.CharField(max_length=200, null=True, blank=True)
    cargo = models.CharField(max_length=200, null=True, blank=True)
    contato = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    observacoes = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(
        max_length=20,
        choices=[('Financeiro', 'Financeiro'), ('Operacional', 'Operacional')],
        default='Financeiro'
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} - {self.tipo}"


# Modelo de Produto
class Produto(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


# Modelo de Contrato


class Contrato(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name='contratos'
    )
    empresa_contratada = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, related_name='contratos'
    )
    gestor_contrato = models.ForeignKey(
        Contato, on_delete=models.PROTECT, related_name='gestor_contrato'
    )
    contato_financeiro = models.ForeignKey(
        Contato, on_delete=models.PROTECT, related_name='financeiro_contrato'
    )
    contato_operacional = models.ForeignKey(
        Contato, on_delete=models.PROTECT, related_name='operacional_contrato'
    )
    numero = models.CharField(max_length=60)
    descricao = models.TextField()
    objeto = models.TextField()
    informacoes_adicionais = models.TextField(blank=True, null=True)
    inicio_vigencia = models.DateField(
        default='2024-01-01')  # Data de início da vigência
    fim_vigencia = models.DateField()  # Data de término da vigência
    is_assinado = models.BooleanField(default=False)
    cobranca = models.CharField(
        max_length=20,
        choices=[('Mensal', 'Mensal'), ('Trimestral',
                                        'Trimestral'), ('Anual', 'Anual')],
        default='Mensal'
    )
    prorrogacao = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    dia_pagamento = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
        help_text="Escolha o dia do mês (1-31) para pagamento."
    )
    dia_emissao_nf = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
        help_text="Escolha o dia do mês (1-31) para emissão da NF."
    )
    # essa parte de produtos vai ser os serviços e veiculos contratados, tem que ser uma class
    produtos = models.ManyToManyField(
        Produto, related_name='contratos', blank=True)
    documentos = models.FileField(
        upload_to='contratos/%Y/%m/%d/', null=True, blank=True)

    # Calcula e retorna o status com base na vigência
    @property
    def status(self):
        today = date.today()
        if self.fim_vigencia and self.fim_vigencia < today:
            return "Inativo"
        return "Ativo"

    class Meta:
        ordering = ['cliente', 'numero']

    def __str__(self):
        return f"Contrato {self.numero} - {self.cliente.razao_social}"
