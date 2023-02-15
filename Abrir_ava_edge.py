from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

navegador = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
navegador.get('https://univirtus.uninter.com/ava/web/')
navegador.maximize_window()

#tempo para carregar a página
time.sleep(1.5)

#colocando login
navegador.find_element(By.ID, 'ru').send_keys(*******************)
navegador.find_element(By.ID, 'senha').send_keys("***************")
navegador.find_element(By.ID, 'loginBtn').click()

#clicando no univirtus
time.sleep(1.0)
navegador.find_element(By.ID, 'loginBoxAva').click()
