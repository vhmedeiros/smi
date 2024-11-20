# clientes/forms.py

from django import forms
from . import models


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = [
            'razao_social', 'cnpj_cpf', 'inscricao_estadual', 'inscricao_municipal',
            'contato_1', 'contato_2', 'email',
            'logradouro', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'UF', 'pais'
        ]
        widgets = {
            # Campos principais
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj_cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_municipal': forms.TextInput(attrs={'class': 'form-control'}),
            'contato_1': forms.TextInput(attrs={'class': 'form-control'}),
            'contato_2': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

            # Campos de endereço
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'UF': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            # Campos principais
            'razao_social': 'Razão Social',
            'cnpj_cpf': 'CNPJ/CPF',
            'inscricao_estadual': 'Inscrição Estadual',
            'inscricao_municipal': 'Inscrição Municipal',
            'contato_1': 'Contato Principal',
            'contato_2': 'Contato Secundário',
            'email': 'E-mail',

            # Campos de endereço
            'logradouro': 'Logradouro',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'cidade': 'Cidade',
            'UF': 'UF',
            'pais': 'País',
        }


class ContatoForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'contato': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nome': 'Nome',
            'departamento': 'Departamento',
            'cargo': 'Cargo',
            'contato': 'Contato',
            'email': 'E-mail',
            'observacoes': 'Observações',
            'tipo': 'Tipo de Contato',
        }


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = models.Produto
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do Produto',
        }


class ContratoForm(forms.ModelForm):
    class Meta:
        model = models.Contrato
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'empresa_contratada': forms.Select(attrs={'class': 'form-select'}),
            'gestor_contrato': forms.Select(attrs={'class': 'form-select'}),
            'contato_financeiro': forms.Select(attrs={'class': 'form-select'}),
            'contato_operacional': forms.Select(attrs={'class': 'form-select'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'objeto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'informacoes_adicionais': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'inicio_vigencia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fim_vigencia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_assinado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cobranca': forms.Select(attrs={'class': 'form-select'}),
            'prorrogacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'dia_pagamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'dia_emissao_nf': forms.NumberInput(attrs={'class': 'form-control'}),
            'produtos': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'documentos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'cliente': 'Cliente',
            'empresa_contratada': 'Empresa Contratada',
            'gestor_contrato': 'Gestor do Contrato',
            'contato_financeiro': 'Contato Financeiro',
            'contato_operacional': 'Contato Operacional',
            'numero': 'Número do Contrato',
            'descricao': 'Descrição',
            'objeto': 'Objeto',
            'informacoes_adicionais': 'Informações Adicionais',
            'inicio_vigencia': 'Início da Vigência',
            'fim_vigencia': 'Fim da Vigência',
            'is_assinado': 'Contrato Assinado',
            'cobranca': 'Cobrança',
            'prorrogacao': 'Prorrogação',
            'valor': 'Valor',
            'dia_pagamento': 'Dia de Pagamento',
            'dia_emissao_nf': 'Dia de Emissão da NF',
            'produtos': 'Produtos',
            'documentos': 'Documentos',
        }
