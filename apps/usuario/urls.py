from apps.usuario.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]