# Buscador de Cotações de Moedas

## Contextualização

Este projeto usa o `tkinter` para criar uma interface gráfica de usuário (GUI) para um sistema de busca de cotações de moedas, o qual faz requisições GET para a API do Banco Central do Brasil (BACEN) de cotações diárias e taxas de câmbio. Os recursos da API podem ser acessados através desta URL: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos


## Demo

Na imagem abaixo, tem-se uma captura de tela do sistema na qual o usuário buscou pela cotação do dólar canadense (CAD) no dia 30/03/203:

![Captura de Tela do Sistema](/sistema-buscador-cotacoes.png "Captura de Tela do Sistema para Cotação de uma Moeda")


Já na imagem a seguir, tem-se o cenário em que o usuário selecionou uma planilha do Excel com os símbolos das moedas na coluna A para obter as cotações para estas moedas no intervalo de datas especificado (01/03/2023 até 30/03/2023):

![Captura de Tela do Sistema](/sistema-busca-cotacoes.png "Captura de Tela do Sistema para Cotações de Diversas Moedas")

Na imagem a seguir, temos uma captura de tela da planilha gerada:

![Captura de Tela da Planilha](/planilha-cotacoes.png "Captura de Tela da Planilha Gerada")

Confira também o arquivo `Cotacoes.xlsx` que está neste repositório.

## Bibliotecas Utilizadas

Estas foram as bibliotecas utilizadas neste projeto:

- pandas
- tkinter
- datetime
- requests

## Como Reproduzir este Projeto

Primeiramente, navegue até a pasta em que deseja clonar este projeto. Em seguida, digite este comando:

```bash
git clone https://github.com/diego-torres-coder/Buscador-de-Cotacoes-de-Moedas.git
```

Com o projeto já clonada, navegue para a pasta deste projeto com o seguinte comando:

```bash
cd Buscador-de-Cotacoes-de-Moedas/
```
Depois, crie um ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Com o ambiente virtual ativo, instale as dependências do projeto:

```bash
pip install numpy pandas openpyxl requests tkcalendar
```

Alternativamente, você pode instalar as dependências deste projeto a partir de `requirements.txt`:

```bash
pip install -r requirements.txt
```

Agora execute o script `main.py`:

```bash
python3 main.py
```


