from http import HTTPStatus
from django.test import TestCase
from apps.fornecedor.forms import FornecedorForms


class TestFormsFornecedor(TestCase):

    def test_campos_form_nome_fornecedor(self):
        form = FornecedorForms()
        self.assertIn("nome_fornecedor", form.fields)
        self.assertInHTML(
            '<input type="text" name="nome_fornecedor" class="item" max_length="100" placeholder="Informe o nome do forneceedor" maxlength="100" required id="id_nome_fornecedor">', str(form)
        )

    def test_campos_form_cnpj(self):
        form = FornecedorForms()
        self.assertIn("cnpj", form.fields)
        self.assertInHTML(
            '<input type="text" name="cnpj" class="item" max_length="100" placeholder="Informe o CNPJ" maxlength="45" required id="id_cnpj">', str(form)
        )

    def test_campos_form_calular(self):
        form = FornecedorForms()
        self.assertIn("celular", form.fields)
        self.assertInHTML(
            '<input type="text" name="celular" class="item" max_length="100" placeholder="Informe o telefone celular" data-mask="(00) 00000-0000" maxlength="20" required id="id_celular">', str(form)
        )

    def test_campos_form_comercial(self):
        form = FornecedorForms()
        self.assertIn("comercial", form.fields)
        self.assertInHTML(
            '<input type="text" name="comercial" class="item" max_length="100" placeholder="Informe o telefone comercial" data-mask="(00) 00000-0000" maxlength="20" required id="id_comercial">', str(form)
        )

    def test_campos_form_residencial(self):
        form = FornecedorForms()
        self.assertIn("residencial", form.fields)
        self.assertInHTML(
            '<input type="text" name="residencial" class="item" max_length="100" placeholder="Informe o telefone residencial" data-mask="(00) 00000-0000" maxlength="20" required id="id_residencial">', str(form)
        )

    def test_campos_form_rua(self):
        form = FornecedorForms()
        self.assertIn("rua", form.fields)
        self.assertInHTML(
            '<input type="text" name="rua" class="item" max_length="100" placeholder="Informe o nome da rua" maxlength="45" required id="id_rua">', str(form)
        )

    def test_campos_form_numero(self):
        form = FornecedorForms()
        self.assertIn("numero", form.fields)
        self.assertInHTML(
            '<input type="text" name="numero" class="item" max_length="45" placeholder="Informe o número" data-mask="000000" maxlength="45" required id="id_numero">', str(form)
        )

    def test_campos_form_cidade(self):
        form = FornecedorForms()
        self.assertIn("cidade", form.fields)
        self.assertInHTML(
            '<input type="text" name="cidade" class="item" max_length="100" placeholder="Informe a cidade" maxlength="45" required id="id_cidade">', str(form)
        )

    def test_campos_form_cep(self):
        form = FornecedorForms()
        self.assertIn("cep", form.fields)
        self.assertInHTML(
            '<input type="text" name="cep" class="item" max_length="100" placeholder="Informe o CEP" data-mask="00000-000" maxlength="45" required id="id_cep">', str(form)
        )

    def test_campos_form_bairro(self):
        form = FornecedorForms()
        self.assertIn("bairro", form.fields)
        self.assertInHTML(
            '<input type="text" name="bairro" class="item" max_length="100" placeholder="Informe o nome do bairro" maxlength="45" required id="id_bairro">', str(form)
        )

    def test_campos_form_complemento(self):
        form = FornecedorForms()
        self.assertIn("bairro", form.fields)
        self.assertInHTML(
            '<input type="text" name="complemento" class="item" max_length="100" placeholder="Informe o complemento" maxlength="45" required id="id_complemento">', str(form)
        )
