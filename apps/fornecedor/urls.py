from apps.usuario.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/fornecedor', views.cadastro_fornecedor, name='cadastro_fornecedor'),
    path('lista/fornecedores', views.lista_fornecedores, name='lista_fornecedores'),
    path('exclui/fornecedor/<int:fornecedor_id>', views.exclui_fornecedor, name='exclui_fornecedor'),
    path('edita/fornecedor/<int:fornecedor_id>', views.edita_fornecedor, name='edita_fornecedor'),
    path('atualiza/fornecedor', views.atualiza_fornecedor, name='atualiza_fornecedor')
]