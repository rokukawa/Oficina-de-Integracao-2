from django.test import TestCase
from caneta.models import Caneta


class TestModelsCaneta(TestCase):

    def setUp(self):

        self.caneta1 = Caneta.objects.create(
            modelo='feltro',
            cor='amarelo',
            ponta='fina'
        )