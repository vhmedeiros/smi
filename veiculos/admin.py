from django.contrib import admin
from . import models


@admin.register(models.TipoDeVeiculo)
class TipoDeVeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla',)


@admin.register(models.Periodicidade)
class PeriodicidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(models.Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'tipodeveiculo',
        'periodicidade',
        'status',
        'grande_imprensa',
        'pais',
        'UF',
        'cidade',
        'prioritario',
        'valor_publicitario_padrao',
        'altura_cm',
        'largura_cm',
        'endereco_do_site',
        'identificador_url',
        'endereco_do_flip',
        'numero_minimo_de_noticias',
        'periodo_maximo_sem_noticia',
    )
    search_fields = ('nome',)


# admin.site.register(models.Veiculo, VeiculoAdmin)
