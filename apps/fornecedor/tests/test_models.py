import unittest
from apps.fornecedor.models import Fornecedor
from django.db import DataError, IntegrityError


class TestModelFornecedor(unittest.TestCase):

    def test_fornecedor_existente(self):
        Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888',
                                  residencial='1325684784', rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
        fornecedor = Fornecedor.objects.get(nome_fornecedor='Jose')
        self.assertEquals('22.596.366/0001-08', fornecedor.cnpj)

    def test_campos_fornecedor_com_limite_de_20_caracteres(self):
        try:
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='0099199889999999999999999', comercial='00991998888',
                                      residencial='1325684784', rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='0099199889999999999999999',
                                      residencial='1325684784', rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888',
                                      residencial='0099199889999999999999999', rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            mensagem = 'Sucesso na criação de fornecedor'
        except DataError:
            mensagem = 'Erro na criação de fornecedor, campos não podem conter mais de 20 caracteres'

        self.assertEqual(
            mensagem, 'Erro na criação de fornecedor, campos não podem conter mais de 20 caracteres')

    def test_campos_fornecedor_com_limite_de_45_caracteres(self):
        try:
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08888888888888888888888888888888888789', celular='00991998899', comercial='00991998888',
                                      residencial='1325684784', rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888', residencial='1325684784',
                                      rua='Alberto Carazzaiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888', residencial='1325684784',
                                      rua='Alberto Carazzai', numero='5801111111111111111111111111111111111111111111111111111', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888', residencial='1325684784',
                                      rua='Alberto Carazzai', numero='580', cidade='Cornelioiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', cep='86300-000', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888', residencial='1325684784',
                                      rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-0001111111111111111111111111111111111111111111111', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888', residencial='1325684784',
                                      rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centroiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888', residencial='1325684784',
                                      rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casaiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            mensagem = 'Sucesso na criação de fornecedor'
        except DataError:
            mensagem = 'Erro na criação de fornecedor, campos não podem conter mais de 45 caracteres'

        self.assertEqual(
            mensagem, 'Erro na criação de fornecedor, campos não podem conter mais de 45 caracteres')

    def test_criar_fornecedor_com_campo_vazio(self):
        try:
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular=None, comercial='00991998888', residencial='1325684784',
                                      rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial=None, residencial='1325684784',
                                      rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888',
                                      residencial=None, rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            mensagem = 'Sucesso na criação de fornecedor'
        except DataError:
            mensagem = 'Erro na criação de fornecedor, campos não podem ser vazios'

        self.assertEqual(
            mensagem, 'Erro na criação de fornecedor, campos não podem ser vazios')

    def test_criar_fornecedor_com_sucesso(self):
        try:
            Fornecedor.objects.create(nome_fornecedor='Jose', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888',
                                      residencial='1325684784', rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa')
            mensagem = 'Sucesso na criação de fornecedor'
        except IntegrityError:
            mensagem = 'Erro na criação de fornecedor'

        self.assertEqual(mensagem, 'Sucesso na criação de fornecedor')
