from django.contrib import admin
from .models import Cliente, Contato, Produto, Contrato


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj_cpf', 'contato_1',
                    'email', 'cidade', 'UF', 'pais')
    list_filter = ('cidade', 'UF', 'pais')
    search_fields = ('razao_social', 'cnpj_cpf', 'email', 'cidade', 'UF')
    ordering = ('razao_social',)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('razao_social', 'cnpj_cpf', 'inscricao_estadual', 'inscricao_municipal')
        }),
        ('Contato', {
            'fields': ('contato_1', 'contato_2', 'email')
        }),
        ('Endereço', {
            'fields': ('logradouro', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'UF', 'pais')
        }),
    )


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'departamento',
                    'cargo', 'contato', 'email')
    list_filter = ('tipo', 'departamento', 'cargo')
    search_fields = ('nome', 'email', 'departamento', 'cargo')
    ordering = ('nome',)
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo', 'departamento', 'cargo')
        }),
        ('Contato', {
            'fields': ('contato', 'email', 'observacoes')
        }),
    )


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'empresa_contratada',
                    'inicio_vigencia', 'fim_vigencia', 'get_status', 'valor')
    list_filter = ('empresa_contratada', 'cobranca',
                   'is_assinado', 'prorrogacao')
    search_fields = ('numero', 'cliente__razao_social',
                     'empresa_contratada__razao_social')
    ordering = ('cliente', 'numero')
    fieldsets = (
        ('Informações do Contrato', {
            'fields': ('numero', 'descricao', 'objeto', 'informacoes_adicionais', 'valor')
        }),
        ('Vigência', {
            'fields': ('inicio_vigencia', 'fim_vigencia', 'is_assinado', 'prorrogacao', 'cobranca')
        }),
        ('Relacionamentos', {
            'fields': ('cliente', 'empresa_contratada', 'gestor_contrato', 'contato_financeiro', 'contato_operacional')
        }),
        ('Outros', {
            'fields': ('produtos', 'documentos')
        }),
    )
    readonly_fields = ('get_status',)  # Status calculado é somente leitura

    @admin.display(description='Status')
    def get_status(self, obj):
        return obj.status  # Usa a propriedade `status` do modelo
