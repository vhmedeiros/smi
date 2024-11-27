import re
from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'sigla', 'nome_fantasia', 'cnpj', 'dominio']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 3}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'maxlength': 18,  # Allows formatted value in the form
                'placeholder': '00.000.000/0000-00'
            }),
            'dominio': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Razão Social',
            'sigla': 'Sigla',
            'nome_fantasia': 'Nome Fantasia',
            'cnpj': 'CNPJ',
            'dominio': 'Domínio',
        }

    def clean_cnpj(self):
        """
        Validates the CNPJ field, ensuring it has exactly 14 numeric characters
        and returns the unformatted value to be stored in the database.
        """
        cnpj = self.cleaned_data['cnpj']

        # Remove all non-numeric characters
        cnpj = re.sub(r'\D', '', cnpj)

        # Check if the cleaned CNPJ has exactly 14 digits
        if len(cnpj) != 14:
            raise forms.ValidationError(
                "O CNPJ deve conter exatamente 14 dígitos.")

        return cnpj
