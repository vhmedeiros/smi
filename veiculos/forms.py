from django import forms
from .models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'  # Todos os campos serão exibidos
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'tipodeveiculo': forms.Select(attrs={'class': 'form-select'}),
            'periodicidade': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'grande_imprensa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'prioritario': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'UF': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_publicitario_padrao': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'altura_cm': forms.NumberInput(attrs={'class': 'form-control'}),
            'largura_cm': forms.NumberInput(attrs={'class': 'form-control'}),
            'endereco_do_site': forms.URLInput(attrs={'class': 'form-control'}),
            'identificador_url': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco_do_flip': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_minimo_de_noticias': forms.NumberInput(attrs={'class': 'form-control'}),
            'periodo_maximo_sem_noticia': forms.NumberInput(attrs={'class': 'form-control'}),
            'url_da_stream': forms.URLInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
            'tipodeveiculo': 'Tipo de Veículo',
            'periodicidade': 'Periodicidade',
            'status': 'Status',
            'grande_imprensa': 'Grande Imprensa',
            'prioritario': 'Prioritário',
            'pais': 'País',
            'UF': 'UF',
            'cidade': 'Cidade',
            'valor_publicitario_padrao': 'Valor Publicitário Padrão',
            'altura_cm': 'Altura (cm)',
            'largura_cm': 'Largura (cm)',
            'endereco_do_site': 'Endereço do Site',
            'identificador_url': 'Identificador de URL',
            'endereco_do_flip': 'Endereço do Flip',
            'numero_minimo_de_noticias': 'Número Mínimo de Notícias',
            'periodo_maximo_sem_noticia': 'Período Máximo sem Notícia (dias)',
            'url_da_stream': 'URL da Stream',

        }
