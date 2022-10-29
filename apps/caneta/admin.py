from django.contrib import admin
from .models import *
from django.contrib.auth import admin as auth_admin

# Register your models here.

# não está sendo usada a classe listandoUsuario


class listandoCaneta(admin.ModelAdmin):
    list_display = ('modelo', 'cor', 'ponta')
    list_display_links = ('modelo', 'cor', 'ponta')
    search_fields = ('modelo', 'cor', 'ponta',)
    list_per_page = 10

admin.site.register(Caneta, listandoCaneta)

class listandoLote(admin.ModelAdmin):
    list_display = ('codigo_maquina', 'data_fabricação')
    list_display_links = ('codigo_maquina', 'data_fabricação')
    search_fields = ('codigo_maquina', 'data_fabricação',)
    list_per_page = 10
    
admin.site.register(Lote, listandoLote)
