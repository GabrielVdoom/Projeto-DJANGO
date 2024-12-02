from django import forms
from .models import CadastroForm


class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroForm
        fields = ['nome_completo', 'cpf', 'usuario', 'senha', 'email', 'telefone', 'genero', 'data_nascimento']
        widgets = {
            'senha': forms.PasswordInput(),  # Usa PasswordInput para ocultar a senha
        }