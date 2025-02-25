from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from docx import Document  
import os  
 
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

def cadastro_documento_word(path):
    path= r'C:\relatorio\relatorio.docx'
    documento_word = Document(path)

    ativo_circulante= ''
    caixa_equivalente = ''
    contas_receber = ''
    estoques = ''
    ativo_nao_circulante = ''
    imobilizado = ''
    intangivel=''
    total_ativo = ''

    for tabela in documento_word.tables:
        for linha in tabela.rows:
            if 'Ativo Circulante' in linha.cells[0].text.strip():
                ativo_circulante = linha.cells[1].text.strip()
            elif 'Caixa e Equivalentes' in linha.cells[0].text.strip():
                caixa_equivalente = linha.cells[1].text.strip()
            elif 'Contas a Receber' in linha.cells[0].text.strip():
                contas_receber = linha.cells[1].text.strip()
            elif 'Estoques' in linha.cells[0].text.strip():
                estoques = linha.cells[1].text.strip()
            elif 'Ativo Não Circulante' in linha.cells[0].text.strip():
                ativo_nao_circulante = linha.cells[1].text.strip()
            elif 'Imobilizado' in linha.cells[0].text.strip():
                imobilizado = linha.cells[1].text.strip()
            elif 'Intangível' in linha.cells[0].text.strip():
                intangivel = linha.cells[1].text.strip()
            elif 'Total do Ativo' in linha.cells[0].text.strip():
                total_ativo = linha.cells[1].text.strip()


    caixa_ativo_circulante = driver.find_element(By.ID,'ativo_circulante')
    sleep(1)
    caixa_ativo_circulante.click()
    caixa_ativo_circulante.send_keys(ativo_circulante)

    caixa_caixa_equivalentes = driver.find_element(By.ID,'caixa_equivalentes')
    sleep(1)
    caixa_caixa_equivalentes.click()
    caixa_caixa_equivalentes.send_keys(caixa_equivalente)

    caixa_contas_receber = driver.find_element(By.ID,'contas_receber')
    sleep(1)
    caixa_contas_receber.click()
    caixa_contas_receber.send_keys(contas_receber)

    caixa_estoques = driver.find_element(By.ID,'estoques')
    sleep(1)
    caixa_estoques.click()
    caixa_estoques.send_keys(estoques)

    caixa_ativo_nao_circulante = driver.find_element(By.ID,'ativo_nao_circulante')
    sleep(1)
    caixa_ativo_nao_circulante.click()
    caixa_ativo_nao_circulante.send_keys(ativo_nao_circulante)

    caixa_imobilizado = driver.find_element(By.ID,'imobilizado')
    sleep(1)
    caixa_imobilizado.click()
    caixa_imobilizado.send_keys(imobilizado)

    caixa_intangivel = driver.find_element(By.ID,'intangivel')
    sleep(1)
    caixa_intangivel.click()
    caixa_intangivel.send_keys(intangivel)

    caixa_total_ativo = driver.find_element(By.ID,'total_ativo')
    sleep(1)
    caixa_total_ativo.click()
    caixa_total_ativo.send_keys(total_ativo)


    botao_cadastro =  driver.find_element(By.XPATH,"//button[@class = 'btn btn-primary']")
    sleep(1)
    botao_cadastro.click()


path_relatorio= r'C:\relatorio'

for nome_arquivo in os.listdir(path_relatorio):
    if nome_arquivo.endswith('.docx'):
        path_arquivo_word= os.path.join(path_relatorio,nome_arquivo)
        cadastro_documento_word(path_arquivo_word)