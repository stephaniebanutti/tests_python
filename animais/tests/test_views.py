from urllib import request
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'Cavalo',
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Não',
        )
 
    def test_index_views_retorna_caracteristicas_do_animal(self):
        """Verifica se a index retorna as caracteristas do animal, pesquisado"""
        response = self.client.get('/', 
            {'buscar': 'Cavalo'}
        )
        caracteristicas_animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristicas_animal_pesquisado[0].nome_animal, 'Cavalo')