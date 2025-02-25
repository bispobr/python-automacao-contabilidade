from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

email = 'email.teste@teste.com'
senha = '123456789'
site = 'https://contabil-devaprender.netlify.app/'

driver = webdriver.Edge()
driver.get(site)
sleep(3)

email = driver.find_element(By.XPATH,"//input[@type = 'email']")
sleep(1)
email.click()
email.send_keys(email)

senha = driver.find_element(By.XPATH,"//input[@type = 'password']")
sleep(1)
senha.click()
senha.send_keys(senha)

entrar = driver.find_element(By.XPATH,"//button[@type = 'submit']")
sleep(1)
entrar.click()

sleep(3)

acessar = driver.find_elements(By.XPATH,"//a[@class = 'btn btn-primary mt-auto']")
sleep(1)
acessar[0].click()