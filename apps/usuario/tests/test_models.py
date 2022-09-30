import unittest
from usuario.models import Usuario
from django.db import DataError, IntegrityError

class TestModelUsuario(unittest.TestCase):

    def test_usuario_existente(self):
        Usuario.objects.create(username='Oficina', email='oficina@oficina.com')
        usuario = Usuario.objects.get(email='oficina@oficina.com')
        self.assertEquals('Oficina', usuario.username)
        
    def test_criar_usuario_com_telefone_com_mais_de_20_caracteres(self):
        try:
            Usuario.objects.create(username='Oficina', email='oficinatelefone@oficina.com', telefone_celular='123456789123456789123456')
            mensagem = 'Sucesso na criação de usuário'
        except DataError:
            mensagem = 'Erro na criação de usuário, campo telefone é inválido'
        
        self.assertEqual(mensagem, 'Erro na criação de usuário, campo telefone é inválido')
    
    def test_criar_usuario_com_email_ja_existente(self):
        Usuario.objects.create(username='Oficina', email='oficinaexistente@oficina.com')
        try:
            Usuario.objects.create(username='Oficina', email='oficinaexistente@oficina.com')
            mensagem = 'Sucesso na criação de usuário'
        except IntegrityError:
            mensagem = 'Erro na criação de usuário, campo email já existe'
        
        self.assertEqual(mensagem, 'Erro na criação de usuário, campo email já existe')
    
    def test_criar_usuario_com_email_null(self):
        try:
            Usuario.objects.create(username='Oficina', email=None)
            mensagem = 'Sucesso na criação de usuário'
        except IntegrityError:
            mensagem = 'Erro na criação de usuário, campo email não pode ser nulo'
        
        self.assertEqual(mensagem, 'Erro na criação de usuário, campo email não pode ser nulo')
    
    def test_criar_usuario_nome_com_mais_de_30_caracteres(self):
        try:
            Usuario.objects.create(username='usernamecommaisdetrintacaracteres', email='oficinanome30@oficina.com')
            mensagem = 'Sucesso na criação de usuário'
        except DataError:
            mensagem = 'Erro na criação de usuário, campo nome não pode conter mais que 30 caracteres'

        self.assertEqual(mensagem, 'Erro na criação de usuário, campo nome não pode conter mais que 30 caracteres')
        
