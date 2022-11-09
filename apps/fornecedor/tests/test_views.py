from django.test import TestCase
from django.test.client import Client
from apps.fornecedor.models import Fornecedor
from django.urls import reverse


class TestViewsFornecedor(TestCase):

    def setUp(self):
        self.client = Client()

        self.fornecedor_inseridos = []
        self.fornecedor_inseridos.append(Fornecedor.objects.create(nome_fornecedor='Bic', cnpj='22.596.366/0001-08', celular='00991998899', comercial='00991998888',
                                         residencial='1325684784', rua='Alberto Carazzai', numero='580', cidade='Cornelio', cep='86300-000', bairro='centro', complemento='casa'))
        self.fornecedor_inseridos.append(Fornecedor.objects.create(nome_fornecedor='Faber Castell', cnpj='81.746.475/0001-23', celular='99999999999',
                                         comercial='99999999999', residencial='1234567891', rua='Rebolsas', numero='978', cidade='Londrina', cep='86025-800', bairro='centro', complemento='casa'))

    def test_cadastrar_post(self):
        response = self.client.get(reverse('cadastro_fornecedor'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastrar/cadastro_fornecedor.html')

    def test_cadastrar_fornecedor(self):

        str_url = reverse('cadastro_fornecedor')
        self.client.post(str_url, {'nome_fornecedor': 'atacado', 'cnpj': '30.277.061/0001-61', 'celular': '43991885566', 'comercial': '43991885566',
                         'residencial': '4335784856', 'rua': 'Duque de Caxias', 'numero': '709', 'cidade': 'Londrina', 'cep': '86015-981', 'bairo': 'centro', 'complemento': 'casa'})

        fornecedor_criado = Fornecedor.objects.filter(
            nome_fornecedor='atacado',
            cnpj='30.277.061/0001-61',
            celular='43991885566',
            comercial='43991885566',
            residencial='4335784856',
            rua='Duque de Caxias',
            numero='709',
            cidade='Londrina',
            cep='86015-981',
            bairro='centro',
            complemento='casa'

        )

        fornecedor_self = Fornecedor.objects.get(
            nome_fornecedor='Bic'
        )

        self.assertNotEqual(0, len(fornecedor_criado),
                            'Não foi possível encontrar a instancia inserida.')
        self.assertEqual(fornecedor_self.cnpj, '22.596.366/0001-08',
                         'Não foi possível encontrar a instancia inserida.')

    def test_edita_fornecedor(self):

        id_atualizar = self.fornecedor_inseridos[1].id

        str_url = reverse('edita_fornecedor', kwargs={
                          'fornecedor_id': id_atualizar})

        self.client.post(str_url)

        fornecedor_self = Fornecedor.objects.get(
            id=id_atualizar
        )

        self.assertEqual(fornecedor_self.cnpj,
                         '81.746.475/0001-23', 'Argumentos divergentes.')
