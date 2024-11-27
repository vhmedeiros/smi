from django.db import models
from veiculos.models import Veiculo
from django.utils.timezone import now

# Lista de tipos de notícias
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

# Modelo para as editorias de um veículo


class Editoria(models.Model):
    veiculo = models.ForeignKey(
        Veiculo,  # Relaciona uma editoria a um veículo
        on_delete=models.PROTECT,  # Evita exclusão de um veículo se houver editorias associadas
        # Permite acessar editorias a partir de um veículo com veiculo.editorias
        related_name='editorias'
    )
    name = models.CharField(max_length=200)  # Nome da editoria

    def __str__(self):
        return self.name  # Retorna o nome da editoria como representação do objeto


# Modelo para os tipos de notícias
class TipoDeNoticia(models.Model):
    tipo = models.CharField(
        max_length=50,  # Limite de 50 caracteres para o nome do tipo
        choices=TIPOS  # Opções definidas na lista TIPOS
    )

    def __str__(self):
        return self.tipo  # Retorna o tipo de notícia como representação do objeto


# Modelo principal para as notícias
class Noticia(models.Model):
    veiculo = models.ForeignKey(
        Veiculo,  # Relaciona a notícia a um veículo
        on_delete=models.PROTECT,  # Impede exclusão do veículo se houver notícias associadas
        related_name='noticias'  # Permite acessar notícias com veiculo.noticias
    )
    editoria = models.ForeignKey(
        Editoria,  # Relaciona a notícia a uma editoria
        on_delete=models.PROTECT,  # Impede exclusão da editoria se houver notícias associadas
        related_name='noticias'  # Permite acessar notícias com editoria.noticias
    )
    tipo_noticia = models.ForeignKey(
        TipoDeNoticia,  # Relaciona a notícia a um tipo de notícia
        on_delete=models.PROTECT,  # Impede exclusão do tipo se houver notícias associadas
        related_name='noticias'  # Permite acessar notícias com tipo_noticia.noticias
    )
    autor = models.CharField(
        max_length=200,  # Nome do autor, com limite de 200 caracteres
        null=True,  # Permite valor nulo
        blank=True  # Permite campo vazio no formulário
    )
    data_publicacao = models.DateTimeField(
        default=now,  # Data e hora padrão é o momento atual
        blank=True  # Permite campo vazio no formulário
    )
    hora = models.TimeField(
        null=True,  # Permite valor nulo
        blank=True  # Permite campo vazio no formulário
    )
    # Define automaticamente a data de criação
    data_cadastro = models.DateTimeField(auto_now_add=True)
    link_noticia = models.URLField(
        unique=True,  # Cada link de notícia deve ser único
        blank=True,  # Permite campo vazio no formulário
        null=True  # Permite valor nulo
    )
    titulo = models.CharField(max_length=255)  # Título da notícia
    subtitulo = models.CharField(
        max_length=255,  # Subtítulo da notícia
        null=True,  # Permite valor nulo
        blank=True  # Permite campo vazio no formulário
    )
    resumo = models.CharField(
        max_length=500,  # Resumo da notícia, com limite de 500 caracteres
        null=True,  # Permite valor nulo
        blank=True  # Permite campo vazio no formulário
    )
    conteudo = models.TextField(
        null=True,  # Permite valor nulo
        blank=True  # Permite campo vazio no formulário
    )

    class Meta:
        # Ordena as notícias da mais recente para a mais antiga
        ordering = ['-data_cadastro']

    def __str__(self):
        return self.titulo  # Retorna o título como representação do objeto


# Modelo para os anexos das notícias
class Anexo(models.Model):
    TIPOS_ANEXO = [
        ('IMAGEM', 'Imagem'),
        ('VIDEO', 'Vídeo'),
        ('AUDIO', 'Áudio'),
        ('DOCUMENTO', 'Documento'),
    ]

    noticia = models.ForeignKey(
        Noticia,  # Relaciona o anexo a uma notícia
        on_delete=models.CASCADE,  # Exclui o anexo se a notícia associada for excluída
        related_name='anexos'  # Permite acessar anexos com noticia.anexos
    )
    tipo = models.CharField(
        max_length=50,  # Tipo do anexo, com limite de 50 caracteres
        choices=TIPOS_ANEXO  # Opções definidas na lista TIPOS_ANEXO
    )
    arquivo = models.FileField(
        upload_to='anexos/'  # Define o diretório de upload dos anexos
    )
    descricao = models.CharField(
        max_length=255,  # Descrição opcional do anexo
        null=True,  # Permite valor nulo
        blank=True  # Permite campo vazio no formulário
    )

    def __str__(self):
        # Retorna o tipo e a descrição do anexo
        return f'{self.tipo} - {self.descricao or "Sem descrição"}'
