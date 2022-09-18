from django import forms
from django.db.models import fields
from django.forms import widgets
from usuario.models import *

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o email'}),
            'username': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o nome'}),
            'password': forms.PasswordInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe a senha'}),
            'telefone_celular': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o seu número de celular', 'data-mask':"(00) 00000-0000"}),
            'telefone_residencial': forms.TextInput(attrs={'class': 'item', 'max_length':100, 'placeholder':'Informe o número do seu telefone residencial', 'data-mask':"(00) 00000-0000"}),
        } 
        