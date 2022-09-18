from usuario.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('dashboard', views.dashboard, name="dashboard")
]