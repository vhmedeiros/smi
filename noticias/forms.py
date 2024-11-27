from django import forms
from .models import Noticia, Anexo, Editoria, TipoDeNoticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'veiculo', 'editoria', 'tipo_noticia', 'autor', 'data_publicacao', 'hora',
            'link_noticia', 'titulo', 'subtitulo', 'resumo', 'conteudo'
        ]
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'editoria': forms.Select(attrs={'class': 'form-select'}),
            'tipo_noticia': forms.Select(attrs={'class': 'form-select'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'link_noticia': forms.URLInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        labels = {
            'veiculo': 'Veículo',
            'editoria': 'Editoria',
            'tipo_noticia': 'Tipo de Notícia',
            'autor': 'Autor',
            'data_publicacao': 'Data de Publicação',
            'hora': 'Hora de Publicação',
            'link_noticia': 'Link da Notícia',
            'titulo': 'Título',
            'subtitulo': 'Subtítulo',
            'resumo': 'Resumo',
            'conteudo': 'Conteúdo',
        }


class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = ['tipo', 'arquivo', 'descricao', 'noticia',]
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'noticia': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'tipo': 'Tipo de Anexo',
            'arquivo': 'Arquivo',
            'descricao': 'Descrição',
            'noticia': 'Notícia',
        }


class EditoriaForm(forms.ModelForm):
    class Meta:
        model = Editoria
        fields = ['veiculo', 'name']
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'veiculo': 'Veículo',
            'name': 'Editoria',
        }


class TipoDeNoticiaForm(forms.ModelForm):
    class Meta:
        model = TipoDeNoticia
        fields = ['tipo']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'tipo': 'Tipo de Notícia',
        }
