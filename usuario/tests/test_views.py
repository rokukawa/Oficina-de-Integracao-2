from http import HTTPStatus
from django.test import TestCase
from usuario.views import cadastro_usuario

class TestViewsUsuario(TestCase):

    def test_rota_cadastrar_usuario(self):
        response = self.client.get('/cadastro/usuario')
        self.assertEqual(response.status_code, 200)

    def test_cadastrar_usuario_e_redirecionar_para_tela_de_login(self):
        form_data = {
            "username": "teste",
            "email": "teste@teste.com",
            "password": "teste",
            "telefone_celular": "",
            "telefone_residencial": "",
        }
        response = self.client.post('/cadastro/usuario', data=form_data)
        self.assertRedirects(response, '/')

