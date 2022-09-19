from fornecedor.models import Fornecedor
from caneta.models import Caneta, Relatorio


def campo_contem_numero(valor_campo, nome_campo, lista_de_erros):
    nome_do_campo = nome_campo.replace('_', ' ')

    if valor_campo is None:
        valor_campo = ''

    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = f'Campo {nome_do_campo} não pode conter números.'


def campo_contem_letra(valor_campo, nome_campo, lista_de_erros):
    nome_do_campo = nome_campo.replace('_', ' ')

    if valor_campo is None:
        valor_campo = ''

    if any(char.isalpha() for char in valor_campo):
        lista_de_erros[nome_campo] = f'Campo {nome_do_campo} não pode conter letras.'


def campo_vazio(valor_campo, nome_campo, lista_de_erros):
    if valor_campo is None:
        valor_campo = ''
        lista_de_erros[nome_campo] = f'Campo {nome_campo} não pode conter apenas espaço em branco.'


def campo_contem_simbolos(valor_campo, nome_campo, lista_de_erros):
    nome_do_campo = nome_campo.replace('_', ' ')
    simbolos_invalidos = '"!@#$%^&*()_-+={}[],.?º'"'"

    if valor_campo is None:
        valor_campo = ''

    for char in valor_campo:
        if char in simbolos_invalidos:
            lista_de_erros[nome_campo] = f'Campo {nome_do_campo} não pode conter símbolos.'
            break


def fornecedor_existente(valor_campo, nome_campo, lista_de_erros):
    fornecedor = Fornecedor.objects.filter(cnpj=valor_campo)

    if fornecedor.count() != 0:
        lista_de_erros[nome_campo] = 'CNPJ já existe.'


def relatorio_existente(valor_campo, nome_campo, lista_de_erros):
    relatorio = Relatorio.objects.filter(codigo=valor_campo)

    if relatorio.count() != 0:
        lista_de_erros[nome_campo] = 'Código do relatório já existe.'


def caneta_existente(modelo_campo, nome_campo, cor_campo, ponta_campo, lista_de_erros):
    caneta = Caneta.objects.filter(modelo=modelo_campo).filter(
        cor=cor_campo).filter(ponta=ponta_campo)

    if caneta.count() != 0:
        lista_de_erros[nome_campo] = f'Caneta já existe.'


def remove_espaço(valor_campo):
    if valor_campo is None:
        valor_campo = ''
    valor_campo = valor_campo.strip()
