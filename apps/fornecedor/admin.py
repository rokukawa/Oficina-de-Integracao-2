from django.contrib import admin
from .models import *
from django.contrib.auth import admin as auth_admin

# Register your models here.

#não está sendo usada a classe listandoUsuario

class listandoFornecedor(admin.ModelAdmin):
    list_display = ('nome_fornecedor', 'cnpj')
    list_display_links = ('nome_fornecedor', 'cnpj')
    search_fields = ('nome_fornecedor', 'cnpj',)
    list_per_page = 10
    
admin.site.register(Fornecedor, listandoFornecedor)