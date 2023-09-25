#Google Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

#abrir o navegador e atualizar o chrome driver caso necessário
navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
navegador.get('https://univirtus.uninter.com/ava/web/')
navegador.maximize_window()

#tempo para abrir a página
time.sleep(1.5)

#colocando login
navegador.find_element(By.ID, 'ru').send_keys(############)
navegador.find_element(By.ID, 'senha').send_keys("***************")
navegador.find_element(By.ID, 'loginBtn').click()

#clicando no univirtus
time.sleep(1.0)
navegador.find_element(By.ID, 'loginBoxAva').click()
