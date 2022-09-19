from django import forms
from caneta.models import *
from oficina2.validation import *


class CanetaForms(forms.ModelForm):
    class Meta:
        model = Caneta
        fields = ('modelo', 'cor', 'ponta')
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'item', 'max_length': 100, 'placeholder': 'Informe o modelo da caneta'}),
            'cor': forms.TextInput(attrs={'class': 'item', 'max_length': 100, 'placeholder': 'Informe a cor da caneta'}),
            'ponta': forms.TextInput(attrs={'class': 'item', 'max_length': 100, 'placeholder': 'Informe a ponta da caneta'}),
        }

    def clean(self):
        lista_de_erros = {}
        modelo = self.cleaned_data.get('modelo')
        cor = self.cleaned_data.get('cor')
        ponta = self.cleaned_data.get('ponta')

        campo_vazio(modelo, 'modelo', lista_de_erros)
        campo_vazio(cor, 'cor', lista_de_erros)
        campo_vazio(ponta, 'ponta', lista_de_erros)

        campo_contem_numero(cor, 'cor', lista_de_erros)
        campo_contem_simbolos(cor, 'cor', lista_de_erros)
        campo_contem_simbolos(modelo, 'modelo', lista_de_erros)
        campo_contem_simbolos(ponta, 'ponta', lista_de_erros)

        caneta_existente(modelo, 'modelo', cor, ponta, lista_de_erros)

        remove_espaço(modelo)
        remove_espaço(cor)
        remove_espaço(ponta)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data
