from django.test import TestCase
from django.test.client import Client
from apps.caneta.models import Caneta
from django.urls import reverse

class TestViewsCaneta(TestCase):

    def setUp(self):
        client = Client()

        self.caneta_inseridas = []
        self.caneta_inseridas.append(Caneta.objects.create(modelo='feltro', cor='verde', ponta='fina'))
        self.caneta_inseridas.append(Caneta.objects.create(modelo='gel', cor='laranja', ponta='grossa'))
        self.caneta_inseridas.append(Caneta.objects.create(modelo='base de óleo', cor='preto', ponta='grossa'))

    
    def test_cadastrar_post(self):
        response = self.client.get(reverse('cadastro_caneta'))
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastrar/cadastro_caneta.html')
    
    def test_cadastrar(self):
        #fazer a requisição pela rota criada na url
        str_url = reverse('cadastro_caneta')
        self.client.post(str_url, {'modelo': 'esferográfica', 'cor': 'azul', 'ponta': 'fina'})

        caneta_criada = Caneta.objects.filter(
            modelo='esferográfica',
            cor='azul',
            ponta='fina'
        )

        caneta_self = Caneta.objects.get(
            modelo='feltro'
        )

        self.assertNotEqual(0, len(caneta_criada), 'Não foi possível encontrar a instancia inserida.')
        self.assertEqual(caneta_self.cor, 'verde', 'Não foi possível encontrar a instancia inserida.')


    def test_edita_caneta(self):
        #recuperando a caneta criada no setUp
        id_atualizar = self.caneta_inseridas[1].id
        
        #fazer a requisição pela rota criada na url
        str_url = reverse('edita_caneta', kwargs={'caneta_id':id_atualizar})

        self.client.post(str_url)

        caneta_self = Caneta.objects.get(
            id=id_atualizar
        )
        
        self.assertEqual(caneta_self.cor, 'laranja', 'Argumentos divergentes.')

