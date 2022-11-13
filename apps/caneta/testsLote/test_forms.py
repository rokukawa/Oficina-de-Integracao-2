from http import HTTPStatus
from django.test import TestCase
from apps.caneta.forms import LoteForms

class TestFormsLote(TestCase):
    
    def test_campos_form_codigo_maquina(self):
        form = LoteForms()
        self.assertIn("codigo_maquina", form.fields)
        self.assertInHTML(
            '<input type="text" name="codigo_maquina" class="item" max_length="100" placeholder="Informe o código de fabricação da máquina da caneta" maxlength="45" required id="id_codigo_maquina">', str(form)
        )

    def test_campos_form_data_fabricação(self):
        form = LoteForms()
        self.assertIn("data_fabricação", form.fields)
        self.assertInHTML(
            '<format_key = "DATE_INPUT_FORMATS" name="data_fabricação" class="item" max_length="100" type="date" placeholder="Informe a data de fabricação da caneta" required id="id_data_fabricação">', str(form)
        )

    def test_campos_form_quantidade(self):
        form = LoteForms()
        self.assertIn("quantidade", form.fields)
        self.assertInHTML(
            '<input type="number" name="quantidade" class="item" max_length="100" placeholder="Informe a quantidade de caneta" required id="id_quantidade">', str(form)
        )    

    def test_campos_form_caneta(self):
        form = LoteForms()
        self.assertIn("caneta", form.fields)
        self.assertInHTML(
            '<input type="select" name="caneta" class="item" max_length="100" placeholder="Informe o tipo de caneta" id="id_caneta">', str(form)
        )    

    def test_campos_form_fornecedor(self):
        form = LoteForms()
        self.assertIn("fornecedor", form.fields)
        self.assertInHTML(
            '<input type="select" name="fornecedor" class="item" max_length="100" placeholder="Informe o fornecedor de caneta"  id="id_fornecedor">', str(form)
        )
