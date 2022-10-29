from django.contrib import auth, messages
from django.shortcuts import render, redirect
from apps.caneta.forms import *
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


def atualiza_caneta(request):
    if request.method == 'POST':
        caneta_id = request.POST['caneta_id']
        c = Caneta.objects.get(pk=caneta_id)
        c.modelo = request.POST['modelo']
        c.cor = request.POST['cor']
        c.ponta = request.POST['ponta']
        c.save()
        return redirect('lista_canetas') 

def cadastro_lote(request):
    lote_form = LoteForms(request.POST or None)
    contexto = {'lote_form': lote_form}

    if request.method == 'POST':
        if lote_form.is_valid():
            lote_form.save()
            return redirect('lista_lote')
        else:
            return render(request, 'cadastrar/cadastro_lote.html', contexto)
    else:
        return render(request, 'cadastrar/cadastro_lote.html', contexto)


def lista_lote(request):
    lote = Lote.objects.all().order_by('codigo_maquina')

    search = request.GET.get('search')
    if search:
        lote = lote.filter(codigo_maquina__icontains=search)

    paginator = Paginator(lote, 3)

    page = request.GET.get('page')

    lista_lote = paginator.get_page(page)
    
    contexto = {'lista_lote': lista_lote}
    return render(request, 'listar/lista_lote.html', contexto)


def exclui_lote(request, lote_id):
    lote = Lote.objects.filter(pk=lote_id)
    lote.delete()
    return redirect('lista_lote')
        
        
def edita_lote(request, lote_id):
    edita_lote = Lote.objects.filter(pk=lote_id)
    contexto = {'edita_lote': edita_lote}
    return render(request, 'editar/edita_lote.html', contexto)