from http import HTTPStatus
from django.test import TestCase
from apps.caneta.forms import CanetaForms

class TestFormsUsuario(TestCase):
    
    def test_campos_form_modelo(self):
        form = CanetaForms()
        self.assertIn("modelo", form.fields)
        self.assertInHTML(
            '<input type="text" name="modelo" class="item" max_length="100" placeholder="Informe o modelo da caneta" maxlength="45" required id="id_modelo">', str(form)
        )

    def test_campos_form_cor(self):
        form = CanetaForms()
        self.assertIn("cor", form.fields)
        self.assertInHTML(
            '<input type="text" name="cor" class="item" max_length="100" placeholder="Informe a cor da caneta" maxlength="45" required id="id_cor">', str(form)
        )

    def test_campos_form_ponta(self):
        form = CanetaForms()
        self.assertIn("ponta", form.fields)
        self.assertInHTML(
            '<input type="text" name="ponta" class="item" max_length="100" placeholder="Informe a ponta da caneta" maxlength="45" required id="id_ponta">', str(form)
        )    
        
      