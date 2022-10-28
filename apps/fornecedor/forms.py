from django import forms
from django.db.models import fields
from django.forms import widgets
from apps.fornecedor.models import *
from oficina2.validation import *

class FornecedorForms(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        widgets = {
            'nome_fornecedor': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o nome do forneceedor'}),
            'cnpj': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o CNPJ', 'data-mask':"00.000.000/0000-00"}),
            'celular': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o telefone celular', 'data-mask':"(00) 00000-0000"}),
            'comercial': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o telefone comercial', 'data-mask':"(00) 00000-0000"}),
            'residencial': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o telefone residencial', 'data-mask':"(00) 00000-0000"}),
            'rua': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o nome da rua'}),
            'numero': forms.TextInput(attrs={'class': 'item', 'max_length':45, 'placeholder':'Informe o número','data-mask':"000000"}),
            'cidade': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a cidade'}),
            'cep': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o CEP', 'data-mask':"00000-000"}),
            'bairro': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o nome do bairro'}),
            'complemento': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o complemento'}),
        }

    def clean(self):
        lista_de_erros = {}
        nome_fornecedor = self.cleaned_data.get('nome_fornecedor')
        cnpj = self.cleaned_data.get('cnpj')
        celular = self.cleaned_data.get('celular')
        comercial = self.cleaned_data.get('comercial')
        residencial = self.cleaned_data.get('residencial')
        rua = self.cleaned_data.get('rua')
        numero = self.cleaned_data.get('numero')
        cidade = self.cleaned_data.get('cidade')
        cep = self.cleaned_data.get('cep')
        bairro = self.cleaned_data.get('bairro')
        complemento = self.cleaned_data.get('complemento')

        campo_vazio(nome_fornecedor, 'nome_fornecedor', lista_de_erros)

        campo_contem_numero(nome_fornecedor, 'nome_fornecedor', lista_de_erros)
        campo_contem_numero(rua, 'rua', lista_de_erros)
        campo_contem_numero(cidade, 'cidade', lista_de_erros)
        campo_contem_numero(bairro, 'bairro', lista_de_erros)

        campo_contem_letra(cnpj, 'cnpj', lista_de_erros)
        campo_contem_letra(celular, 'celular', lista_de_erros)
        campo_contem_letra(comercial, 'comercial', lista_de_erros)
        campo_contem_letra(residencial, 'residencial', lista_de_erros)
        campo_contem_letra(cep, 'cep', lista_de_erros)
        campo_contem_letra(numero, 'numero', lista_de_erros)

        campo_contem_simbolos(nome_fornecedor, 'nome_fornecedor', lista_de_erros)
        campo_contem_simbolos(rua, 'rua', lista_de_erros)
        campo_contem_simbolos(cidade, 'cidade', lista_de_erros)
        campo_contem_simbolos(bairro, 'bairro', lista_de_erros)
        campo_contem_simbolos(complemento, 'complemento', lista_de_erros)

        fornecedor_existente(cnpj, 'cnpj', lista_de_erros)

        remove_espaço(nome_fornecedor)
        remove_espaço(rua)
        remove_espaço(bairro)
        remove_espaço(cidade)
        remove_espaço(complemento)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data
        
