from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index
 
class AnimaisURLSTesteCase(TestCase):
    
    def setUp(self): #cria o cenario de teste
        self.factory = RequestFactory()

    def test_rota_url_index(self):
        """ Testa se a home da aplicação utiliza a função index da view """
        request = self.factory.get('/') #recebe a requisição, guardando meu endereço url
        with self.assertTemplateUsed('index.html'): #verifica se está utilizando o template
            response = index(request) # vai para o idex recebendo o meu parametro
            self.assertEqual(response.status_code, 200) #e retorna com status 200
