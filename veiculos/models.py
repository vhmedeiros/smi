from django.db import models


class TipoDeVeiculo(models.Model):
    # TIPOS = [
    #     ('Blog', 'Blog'),
    #     ('Impresso', 'Impresso'),
    #     ('Podcast', 'Podcast'),
    #     ('Rádio', 'Rádio'),
    #     ('Revista', 'Revista'),
    #     ('Site', 'Site'),
    #     ('Televisão', 'Televisão'),
    #     ('Videocast', 'Videocast'),
    # ]

    nome = models.CharField(max_length=500)
    sigla = models.CharField(max_length=2, unique=True, null=True, blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Periodicidade(models.Model):
    # PERIODOS = [
    #     ('Diário', 'Diário'),
    #     ('Semanal', 'Semanal'),
    #     ('Quinzenal', 'Quinzenal'),
    #     ('Mensal', 'Mensal'),
    #     ('Bimestral', 'Bimestral'),
    #     ('Trimestral', 'Trimestral'),
    #     ('Semestral', 'Semestral'),
    #     ('Anual', 'Anual'),
    # ]

    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    nome = models.CharField(max_length=500)
    tipodeveiculo = models.ForeignKey(
        TipoDeVeiculo, on_delete=models.PROTECT, related_name='veiculos'
    )
    periodicidade = models.ForeignKey(
        Periodicidade, on_delete=models.PROTECT, related_name='veiculos'
    )
    status = models.CharField(
        max_length=20,
        choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')],
        default='Ativo'
    )
    grande_imprensa = models.BooleanField(default=False)
    pais = models.CharField(max_length=100, default='Brasil')
    uf = models.CharField(max_length=2)  # Ex.: 'SP'
    cidade = models.CharField(max_length=100, blank=True, null=True)
    prioritario = models.BooleanField(default=False)
    valor_publicitario_padrao = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    altura_cm = models.IntegerField(blank=True, null=True)
    largura_cm = models.IntegerField(blank=True, null=True)
    endereco_do_site = models.URLField(blank=True, null=True)
    identificador_url = models.CharField(max_length=255, blank=True, null=True)
    endereco_do_flip = models.CharField(max_length=255, blank=True, null=True)
    numero_minimo_de_noticias = models.IntegerField(blank=True, null=True)
    periodo_maximo_sem_noticia = models.IntegerField(blank=True, null=True)
    url_da_stream = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
