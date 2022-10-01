from http import HTTPStatus
from django.test import TestCase
from apps.usuario.forms import UsuarioForms

class TestFormsUsuario(TestCase):
    
    def test_campos_form_username(self):
        form = UsuarioForms()
        self.assertIn("username", form.fields)
        self.assertInHTML(
            '<input type="text" name="username" class="item" max_length="100" placeholder="Informe o nome" maxlength="30" required id="id_username">', str(form)
        )

    def test_campos_form_password(self):
        form = UsuarioForms()
        self.assertIn("password", form.fields)
        self.assertInHTML(
            '<input type="password" name="password" class="item" max_length="100" placeholder="Informe a senha" maxlength="128" required id="id_password">', str(form)
        )

    def test_campos_form_email(self):
        form = UsuarioForms()
        self.assertIn("email", form.fields)
        self.assertInHTML(
            '<input type="email" name="email" class="item" max_length="100" placeholder="Informe o email" maxlength="255" required id="id_email">', str(form)
        )    

    def test_campos_form_telefone_celular(self):
        form = UsuarioForms()
        self.assertIn("telefone_celular", form.fields)
        self.assertInHTML(
            '<input type="text" name="telefone_celular" class="item" max_length="100" placeholder="Informe o seu número de celular" data-mask="(00) 00000-0000" maxlength="20" id="id_telefone_celular">', str(form)
        )    

    def test_campos_form_telefone_residencial(self):
        form = UsuarioForms()
        self.assertIn("telefone_residencial", form.fields)
        self.assertInHTML(
            '<input type="text" name="telefone_residencial" class="item" max_length="100" placeholder="Informe o número do seu telefone residencial" data-mask="(00) 00000-0000" maxlength="20" id="id_telefone_residencial">', str(form)
        )
