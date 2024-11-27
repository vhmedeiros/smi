from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    # Exibe colunas relevantes na listagem
    list_display = ('nome', 'sigla', 'nome_fantasia', 'cnpj',
                    'dominio', 'created_at', 'updated_at')
    # Filtros disponíveis na lateral da listagem
    list_filter = ('created_at', 'updated_at')
    # Campos de busca
    search_fields = ('nome', 'nome_fantasia', 'cnpj', 'dominio')
    # Ordenação padrão
    ordering = ('nome',)
    # Estrutura de campos no formulário de edição
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'sigla', 'nome_fantasia', 'cnpj', 'dominio')
        }),
        ('Datas de Registro', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    # Campos que não podem ser editados
    readonly_fields = ('created_at', 'updated_at')
