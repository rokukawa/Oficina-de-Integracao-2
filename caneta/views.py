from django.contrib import auth, messages
from django.shortcuts import render, redirect
from caneta.forms import *
from django.core.paginator import Paginator

# Create your views here.


def cadastro_caneta(request):
    caneta_form = CanetaForms(request.POST or None)
    contexto = {'caneta_form': caneta_form}

    if request.method == 'POST':
        if caneta_form.is_valid():
            caneta_form.save()
            return redirect('lista_canetas')
        else:
            return render(request, 'cadastrar/cadastro_caneta.html', contexto)
    else:
        return render(request, 'cadastrar/cadastro_caneta.html', contexto)


def lista_canetas(request):
    canetas = Caneta.objects.all().order_by('modelo')

    search = request.GET.get('search')
    if search:
        canetas = canetas.filter(modelo__icontains=search)

    paginator = Paginator(canetas, 4)

    page = request.GET.get('page')

    lista_canetas = paginator.get_page(page)

    contexto = {'lista_canetas': lista_canetas}
    return render(request, 'listar/lista_canetas.html', contexto)


def exclui_caneta(request, caneta_id):
    caneta = Caneta.objects.filter(pk=caneta_id)
    caneta.delete()
    return redirect('lista_canetas')


def edita_caneta(request, caneta_id):
    edita_caneta = Caneta.objects.filter(pk=caneta_id)
    contexto = {'edita_caneta': edita_caneta}
    return render(request, 'editar/edita_caneta.html', contexto)
