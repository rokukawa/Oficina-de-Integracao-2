from django.test.client import Client
from http import HTTPStatus
from django.test import TestCase
from apps.usuario.models import Usuario
from apps.usuario.views import cadastro_usuario
from django.urls import reverse


class TestViewsUsuario(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Usuario.objects.create(
            email='teste@teste.com', username='teste')
        self.user.set_password('teste')
        self.user.save()

    def test_rota_cadastrar_usuario(self):
        response = self.client.get('/cadastro/usuario')
        self.assertEqual(response.status_code, 200)

    def test_cadastrar_usuario_e_redirecionar_para_tela_de_login(self):
        form_data = {
            "username": "sucesso",
            "email": "sucesso@sucesso.com",
            "password": "sucesso",
            "telefone_celular": "",
            "telefone_residencial": "",
        }
        response = self.client.post('/cadastro/usuario', data=form_data)
        self.assertRedirects(response, '/')

    def test_login_usuario(self):
        login = self.client.login(email='teste@teste.com', password='teste')

        self.assertTrue(login)

    def test_login_senha_vazia(self):
        login = self.client.login(email='teste@teste.com', password='')
        
        self.assertFalse(login)

    def test_logout(self):
        self.client.login(email='teste@teste.com', password='teste')
        
        self.assertTrue(self.client.logout)

