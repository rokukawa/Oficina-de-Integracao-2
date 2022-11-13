from http import HTTPStatus
from sqlite3 import DataError, IntegrityError
from django.test import TestCase
from apps.caneta.models import Lote

class TestFormsLote(TestCase):

    def test_lote_existente(self):
        Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade='10', caneta='esferográfica', fornecedor='Bic')
        lote = Lote.objects.get(codigo_maquina='1')
        self.assertEquals('10', lote.quantidade)
        
    def test_criar_lote_campos_com_mais_de_45_caracteres(self):
        try:
            Lote.objects.create(codigo_maquina='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', data_fabricação='10/11/2022', quantidade='10', caneta='esferográfica', fornecedor='Bic')
            Lote.objects.create(codigo_maquina='1', data_fabricação='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', quantidade='10', caneta='esferográfica', fornecedor='Bic')
            Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', caneta='esferográfica', fornecedor='Bic')
            Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade='10', caneta='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', fornecedor='Bic')
            Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade='10', caneta='esferográfica', fornecedor='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
            mensagem = 'Sucesso na criação do Lote'
        except DataError:
            mensagem = 'Erro na criação do Lote, campos não podem conter mais de 45 caracteres'
        
        self.assertEqual(mensagem, 'Erro na criação do Lote, campos não podem conter mais de 45 caracteres')
    
    def test_criar_lote_com_campo_vazio(self):
        try:
            Lote.objects.create(codigo_maquina=None, data_fabricação='10/11/2022', quantidade='10', caneta='esferográfica', fornecedor='Bic')
            Lote.objects.create(codigo_maquina='1', data_fabricação=None, quantidade='10', caneta='esferográfica', fornecedor='Bic')
            Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade=None, caneta='esferográfica', fornecedor='Bic')
            Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade='10', caneta=None, fornecedor='Bic')
            Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade='10', caneta='esferográfica', fornecedor=None)            
            mensagem = 'Sucesso na criação do Lote'
        except IntegrityError:
            mensagem = 'Erro na criação do Lote, campos não podem ser vazios'
        
        self.assertEqual(mensagem, 'Erro na criação do Lote, campos não podem ser vazios')
    
    def test_criar_lote_com_sucesso(self):
        try:
            Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade='10', caneta='esferográfica', fornecedor='Bic')
            mensagem = 'Sucesso na criação do Lote'
        except IntegrityError:
            mensagem = 'Erro na criação do Lote'
        
        self.assertEqual(mensagem, 'Sucesso na criação do Lote')