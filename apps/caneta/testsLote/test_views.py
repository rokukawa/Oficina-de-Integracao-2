from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from apps.caneta.models import Lote


class TestViewsLote(TestCase):

    def setUp(self):
        self.client = Client()

        self.lote_inseridos = []
        self.lote_inseridos.append(Lote.objects.create(codigo_maquina='1', data_fabricação='10/11/2022', quantidade='10', caneta='esferográfica', fornecedor='Bic'))
        self.lote_inseridos.append(Lote.objects.create(codigo_maquina='2', data_fabricação='11/11/2022', quantidade='20', caneta='gel', fornecedor='FaberCastel'))

    def test_cadastrar_post(self):
        response = self.client.get(reverse('cadastro_lote'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastrar/cadastro_lote.html')

    def test_cadastrar_lote(self):

        str_url = reverse('cadastro_lote')
        self.client.post(str_url, {'codigo_maquina': '3', 'data_fabricação': '12/11/2022', 'quantidade': '30', 'caneta': 'tinteiro','fornecedor': 'Stabilo'})

        lote_criado = Lote.objects.filter(
            codigo_maquina='3',
            data_fabricação='12/11/2022',
            quantidade='30',
            caneta='tinteiro',
            fornecedor='Stabilo'

        )

        lote_self = Lote.objects.get(
            codigo_maquina='3'
        )

        self.assertNotEqual(0, len(lote_criado),
                            'Não foi possível encontrar a instancia inserida.')
        self.assertEqual(lote_self.quantidade, '30',
                         'Não foi possível encontrar a instancia inserida.')

    def test_edita_lote(self):

        id_atualizar = self.lote_inseridos[1].id

        str_url = reverse('edita_lote', kwargs={
                          'lote_id': id_atualizar})

        self.client.post(str_url)

        lote_self = Lote.objects.get(
            id=id_atualizar
        )

        self.assertEqual(lote_self.quantidade,
                         '50', 'Argumentos divergentes.')
