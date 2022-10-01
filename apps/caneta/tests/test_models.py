import unittest
from apps.caneta.models import Caneta
from django.db import DataError, IntegrityError

class TestModelCaneta(unittest.TestCase):

    def test_caneta_existente(self):
        Caneta.objects.create(modelo='Tinta óleo', cor='verde', ponta='fina')
        caneta = Caneta.objects.get(modelo='Tinta óleo')
        self.assertEquals('verde', caneta.cor)
        
    def test_criar_caneta_campos_com_mais_de_45_caracteres(self):
        try:
            Caneta.objects.create(modelo='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', cor='amarelo', ponta='grossa')
            Caneta.objects.create(modelo='esferográfica', cor='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', ponta='grossa')
            Caneta.objects.create(modelo='esferográfica', cor='amarelo', ponta='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
            mensagem = 'Sucesso na criação de caneta'
        except DataError:
            mensagem = 'Erro na criação de caneta, campos não podem conter mais de 45 caracteres'
        
        self.assertEqual(mensagem, 'Erro na criação de caneta, campos não podem conter mais de 45 caracteres')
    
    def test_criar_caneta_com_campo_vazio(self):
        try:
            Caneta.objects.create(modelo=None, cor='rosa', ponta='1.6')
            Caneta.objects.create(modelo='feltro', cor=None, ponta='1.6')
            Caneta.objects.create(modelo='feltro', cor='rosa', ponta=None)
            mensagem = 'Sucesso na criação de caneta'
        except IntegrityError:
            mensagem = 'Erro na criação de caneta, campos não podem ser vazios'
        
        self.assertEqual(mensagem, 'Erro na criação de caneta, campos não podem ser vazios')
    
    def test_criar_caneta_com_sucesso(self):
        try:
            Caneta.objects.create(modelo='Pena', cor='marrom', ponta='0.7')
            mensagem = 'Sucesso na criação de caneta'
        except IntegrityError:
            mensagem = 'Erro na criação de caneta'
        
        self.assertEqual(mensagem, 'Sucesso na criação de caneta')
   
    def test_criar_caneta_com_menos_de_4_caracteres(self):
        try: 
            Caneta.objects.create(modelo='abc', cor='azul', ponta='fina')
            mensagem = 'Sucesso na criação de caneta'
        except DataError:
            mensagem = 'Erro na criação de caneta, campos não podem conter menos de 4 caracteres'

        self.assertEqual(mensagem, 'Erro na criação de caneta, campos não podem conter menos de 4 caracteres')
