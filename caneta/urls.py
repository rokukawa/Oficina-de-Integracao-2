from usuario.views import *
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
]
