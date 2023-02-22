#Google Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#abrir o navegador e atualizar o chrome driver caso necessário
navegador = webdriver.Chrome(ChromeDriverManager().install())
navegador.get('https://univirtus.uninter.com/ava/web/')
navegador.maximize_window()

#tempo para abrir a página
time.sleep(1.5)

#colocando login
navegador.find_element(By.ID, 'ru').send_keys(*******************)
navegador.find_element(By.ID, 'senha').send_keys("***************")
navegador.find_element(By.ID, 'loginBtn').click()

#clicando no univirtus
time.sleep(1.0)
navegador.find_element(By.ID, 'loginBoxAva').click()

#fechar popup
from selenium.common.exceptions import NoSuchElementException
time.sleep(1.5)

try:
	navegador.find_element(By.ID,'fecharModalPopup').click()
    
except NoSuchElementException:
    pass

#link para abrir disciplinas em andamento
time.sleep(1.5)
navegador.find_element(By.XPATH, '//*[@id="escola_9"]').click()
time.sleep(0.5)
navegador.find_element(By.XPATH,'//*[@id="curso_633"]/div[1]/h4/a/span[2]').click()
