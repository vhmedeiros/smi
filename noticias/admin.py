from django.contrib import admin
from .models import Noticia, Editoria, TipoDeNoticia, Anexo


@admin.register(Editoria)
class EditoriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'veiculo')
    search_fields = ('name', 'veiculo__nome')
    list_filter = ('veiculo',)
    ordering = ('name',)
    fieldsets = (
        ('Informações da Editoria', {
            'fields': ('name', 'veiculo')
        }),
    )


@admin.register(TipoDeNoticia)
class TipoDeNoticiaAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    search_fields = ('tipo',)
    ordering = ('tipo',)
    fieldsets = (
        ('Informações do Tipo de Notícia', {
            'fields': ('tipo',)
        }),
    )


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'veiculo', 'editoria', 'tipo_noticia',
                    'data_publicacao', 'data_cadastro', 'autor')
    search_fields = ('titulo', 'veiculo__nome', 'editoria__name',
                     'tipo_noticia__tipo', 'autor', 'conteudo')
    list_filter = ('veiculo', 'editoria', 'tipo_noticia',
                   'data_publicacao', 'data_cadastro')
    ordering = ('-data_cadastro',)
    readonly_fields = ('data_cadastro',)
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('titulo', 'subtitulo', 'resumo', 'conteudo', 'link_noticia')
        }),
        ('Relacionamentos', {
            'fields': ('veiculo', 'editoria', 'tipo_noticia', 'autor')
        }),
        ('Datas', {
            'fields': ('data_publicacao', 'hora', 'data_cadastro')
        }),
    )


@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    # Define os campos exibidos na lista
    list_display = ('tipo', 'descricao', 'noticia')
    # Campos que podem ser pesquisados
    search_fields = ('descricao',)
    # Filtros laterais
    list_filter = ('tipo',)
    # Ordenação padrão dos registros no admin
    ordering = ('-id',)  # Ordena pelo ID mais recente
    # Organiza os campos no formulário de edição
    fieldsets = (
        ('Informações do Anexo', {
            'fields': ('noticia', 'tipo', 'arquivo', 'descricao')
        }),
    )
