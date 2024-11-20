from django.db import models
from veiculos.models import Veiculo
from django.utils.timezone import now


class Editoria(models.Model):
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.PROTECT, related_name='editorias')
    name = models.CharField(max_length=200)


class TipoDeNoticia(models.Model):
    TIPOS = [
        ('ANÚNCIO/PUBLICIDADE', 'Anúncio/Publicidade'),
        ('AO VIVO E CHAMADA', 'Ao Vivo e Chamada'),
        ('ARTIGO', 'Artigo'),
        ('CARTA/EMAIL', 'Carta/Email'),
        ('CHAMADA DE CAPA', 'Chamada de Capa'),
        ('CHARGE', 'Charge'),
        ('CINEMA', 'Cinema'),
        ('COLUNA', 'Coluna'),
        ('CRÔNICA', 'Crônica'),
        ('CURTAS', 'Curtas'),
        ('DEBATE', 'Debate'),
        ('EDITAL', 'Edital'),
        ('EDITORIAL', 'Editorial'),
        ('ENTREVISTA', 'Entrevista'),
        ('ESCALADA', 'Escalada'),
        ('FEED', 'Feed'),
        ('IGTV', 'IGTV'),
        ('INSERÇÃO ELEITORAL', 'Inserção Eleitoral'),
        ('MATÉRIA', 'Matéria'),
        ('MATÉRIA COM CHAMADA', 'Matéria com chamada'),
        ('NOTA', 'Nota'),
        ('PROGRAMA ELEITORAL', 'Programa eleitoral'),
        ('Reportagem', 'Reportagem'),
        ('Stories', 'Stories'),

    ]

    tipo = models.CharField(max_length=50, choices=TIPOS)

    def __str__(self):
        return self.tipo


class Noticia(models.Model):
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.PROTECT, related_name='noticias'
    )
    editoria = models.ForeignKey(
        Editoria, on_delete=models.PROTECT, related_name='noticias'
    )
    tipo_noticia = models.ForeignKey(
        TipoDeNoticia, on_delete=models.PROTECT, related_name='noticias'
    )
    autor = models.CharField(max_length=200, null=True, blank=True)
    data_publicacao = models.DateTimeField(default=now, blank=True)
    hora = models.TimeField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    link_noticia = models.URLField(unique=True)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, null=True, blank=True)
    resumo = models.CharField(max_length=500, null=True, blank=True)
    conteudo = models.TextField(null=True, blank=True)

    # Campos para anexos
    foto = models.ImageField(upload_to='foto/', null=True, blank=True)
    a4 = models.FileField(upload_to='a4/', null=True, blank=True)
    img = models.ImageField(upload_to='img/', null=True, blank=True)
    printscreen = models.ImageField(
        upload_to='printscreen/', null=True, blank=True)

    class Meta:
        ordering = ['-data_cadastro']

    def __str__(self):
        return self.titulo
