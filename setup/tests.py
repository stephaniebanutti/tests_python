from django.test import LiveServerTestCase  #testes para simular ações e fazer testes da aplicação
from selenium import webdriver # faz as ações da class
from selenium.webdriver.common.by import By
import time
from animais.models import Animal

class AnimaisTesteCase(LiveServerTestCase):
    
    def setUp(self): # Prepara o ambiente de teste
        self.browser = webdriver.Chrome('chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )
    def ftearDown(self): # fecha o ambiente de teste
        self.browser.quit()

    def test_procura_animal(self): # Sempre que eu quiser referenciar um teste, necessário colocar test_NOME_DA_DEF
        """ Procur um animal na barra de pesquisa """
        # Vini, deseja encontrar um novo animal,
        # para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, ".navbar") #vai na pagina e busca o navbar
        self.assertEqual('Busca Animal', brand_element.text)
        # Ele vê um campo para pesquisar animais pelo nome. 
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, "input#buscar-animal") #campo para digitar o animal escolhido
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: Leão') # dentro do input contem um plecheholder
        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('Leão') # digita o animal escolhido
        self.browser.find_element(By.CSS_SELECTOR, "form button").click() #botão para envio do dado digitado
        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, ".result-description")
        self.assertGreater(len(caracteristicas), 3)
        # Ele desiste de adotar um leão.
    