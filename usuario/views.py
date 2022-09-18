from usuario.models import Usuario
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from usuario.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def cadastro_usuario(request):
    usuario_form = UsuarioForms(request.POST or None)
    contexto = {'usuario_form': usuario_form}

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        telefone_celular = request.POST['telefone_celular']
        telefone_residencial = request.POST['telefone_residencial']

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'O campo e-mail já existe.')
            return render(request, 'cadastrar/cadastro_usuario.html', contexto)

        usuario = Usuario.objects.create_user(email=email, username=username, password=password, telefone_celular=telefone_celular, telefone_residencial=telefone_residencial)
        usuario.save()

        return redirect('login')
    else:
        return render(request, 'cadastrar/cadastro_usuario.html', contexto)

def dashboard(request):
    return render(request, 'dashboard.html')