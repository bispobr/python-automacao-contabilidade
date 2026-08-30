# Automação de Processos Contábeis

Automação desenvolvida em Python para interação com um sistema web por meio do navegador Microsoft Edge, realizando autenticação e preenchimento automático de campos a partir de informações fornecidas por um arquivo DOCX.

O projeto tem como objetivo automatizar tarefas repetitivas de preenchimento e reduzir a execução manual dessas etapas.

## Funcionalidades

- Acesso automatizado ao sistema web
- Login automatizado
- Leitura de informações provenientes de arquivo DOCX
- Preenchimento automático de campos específicos
- Execução das tarefas por meio do navegador Microsoft Edge

## Tecnologias

- Python
- Selenium
- Microsoft Edge
- Arquivo DOCX como fonte de dados

## Requisitos

- Python instalado
- Microsoft Edge instalado
- Selenium
- Biblioteca compatível com a leitura do arquivo DOCX utilizado pelo projeto
- Acesso ao sistema web utilizado pela automação

## Como utilizar

Clone o repositório:

```bash
git clone https://github.com/bispobr/python-automacao-contabilidade.git
cd python-automacao-contabilidade
```

Instale as dependências necessárias conforme a implementação atual do projeto.

Em seguida, execute o arquivo principal:

```bash
python app.py
```

O arquivo DOCX utilizado pela automação deve estar disponível no local esperado pela aplicação.

## Fluxo da automação

```text
Início
  │
  ▼
Acessar sistema web
  │
  ▼
Realizar login
  │
  ▼
Ler dados do arquivo DOCX
  │
  ▼
Preencher campos
  │
  ▼
Finalizar processo
  │
  ▼
Fim
```

## Estrutura

O ponto de entrada identificado na documentação do projeto é o arquivo `app.py`.

Os demais arquivos e configurações devem ser consultados diretamente no código para identificar os requisitos específicos da automação.

## Status

Projeto de automação em Python voltado à redução de tarefas repetitivas em processos de preenchimento de informações em sistemas web.
