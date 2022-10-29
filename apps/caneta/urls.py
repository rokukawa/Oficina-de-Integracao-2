from apps.usuario.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/caneta', views.cadastro_caneta, name='cadastro_caneta'),
    path('lista/canetas', views.lista_canetas, name='lista_canetas'),
    path('exclui/caneta/<int:caneta_id>',
         views.exclui_caneta, name='exclui_caneta'),
    path('edita/caneta/<int:caneta_id>',
         views.edita_caneta, name='edita_caneta'),
    path('atualiza/caneta', views.atualiza_caneta, name='atualiza_caneta'),
    path('cadastro/lote', views.cadastro_lote, name='cadastro_lote'),
    path('lista/lote', views.lista_lote, name='lista_lote'),
    path('exclui/lote/<int:lote_id>', views.exclui_lote, name='exclui_lote'),
    path('atualiza/lote', views.atualiza_lote, name='atualiza_lote'),
]
