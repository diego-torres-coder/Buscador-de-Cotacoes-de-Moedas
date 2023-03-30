# Importa o módulo datetime com o apelido dt
from datetime import datetime as dt

# Importa o módulo requests
import requests

# Importa o tkinter com o apelido tk
import tkinter as tk

# Import a função para definar a fonte dos objetos
import tkinter.font as tkFont

# Importa a extensão ttk
from tkinter import ttk

# Importa a função para abrir arquivos do computador
from tkinter.filedialog import askopenfilename

# Importa o campo de data do tkcalendar
from tkcalendar import DateEntry

# Cria uma janela
janela = tk.Tk()

# Título da janela
janela.title('Buscador de Cotações de Moedas Estrangeiras')

# Configuração das colunas da janela
janela.columnconfigure(list(range(3)), weight=1)

# Definição das dimensões da janela
largura_janela = 700
altura_janela = 525

# Obtenção das dimensões da tela do computador
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Definição das coordenadas para centralizar a janela na tela
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

# Definição da geometria da janela
janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')

# Impede que a janela seja redimensionada
janela.resizable(False, False)

# Fonte dos títulos
fonte_titulo = tkFont.Font(family='Arial', size=16)

rotulo_cotacao_moeda = tk.Label(text='Cotação de Moeda', borderwidth=2, relief='solid')
rotulo_cotacao_moeda['font'] = fonte_titulo
rotulo_cotacao_moeda.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='NSEW')

rotulo_selecionar_moeda = tk.Label(text='Selecione a moeda desejada:')
rotulo_selecionar_moeda.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')


def obter_moedas_disponiveis() -> list:
    '''Retorna a lista de moedas disponíveis na API do Banco Central do Brasil (BACEN).'''
    # URL da API do Banco Central do Brasil para obter as moedas disponíveis
    url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json'

    # Resposta da requisição HTTP GET
    resposta = requests.get(url)

    # Dicionário com os dados da resposta
    dados = resposta.json()

    # Lista de moedas
    moedas_disponiveis = []

    # Percorre a lista de dicionários com os dados de cada moeda
    for valor in dados['value']:
        # Acrescenta o símbolo da moeda à lista de moedas
        moedas_disponiveis.append(valor['simbolo'])

    # Retorna a lista de moedas
    return moedas_disponiveis


menu_moedas_disponiveis = ttk.Combobox(values=obter_moedas_disponiveis())
menu_moedas_disponiveis.grid(row=1, column=2, padx=10, pady=10, sticky='NSEW')

rotulo_data_cotacao = tk.Label(text='Selecione a data da cotação:')
rotulo_data_cotacao.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')

campo_data_cotacao = DateEntry(year=2023, locale='pt_br')
campo_data_cotacao.grid(row=2, column=2, padx=10, pady=10, sticky='NSEW')

# Rótulo para a mensagem a ser exibida
rotulo_cotacao = tk.Label(text='')
rotulo_cotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')


def obter_cotacao():
    '''Obtém a cotação da moeda selecionada.'''
    # Moeda selecionada
    moeda_selecionada = menu_moedas_disponiveis.get()

    # Obtém a data selecionada
    data_selecionada = campo_data_cotacao.get()

    # Converte a string em um objeto datetime
    data_cotacao = dt.strptime(data_selecionada, '%d/%m/%Y') 

    # Converte a data numa string com o format mm-dd-aaaa
    data_cotacao = data_cotacao.strftime('%m-%d-%Y')

    # URL para obter a cotação de compra da moeda selecionada na data solicitada
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='{moeda_selecionada}'&@dataCotacao='{data_cotacao}'&$top=1&$skip=0&$orderby=dataHoraCotacao%20desc&$format=json&$select=cotacaoCompra,dataHoraCotacao"

    # Resposta da requisição
    resposta = requests.get(url)

    # Dicionário com os dados da requisição
    dados = resposta.json()

    # Obtém a cotação de compra da moeda
    cotacao = dados['value'][0]['cotacaoCompra']

    # Substitui o ponto pela vírgula
    cotacao = str(cotacao).replace('.', ',')

    # Texto com a cotação da moeda selecionada
    texto_cotacao = f'A cotação para a moeda {moeda_selecionada} em {data_selecionada} era de R$ {cotacao}'

    # Atualiza o parâmetro text do rótulo
    rotulo_cotacao['text'] = texto_cotacao


botao_obter_cotacao = tk.Button(text='Obter Cotação', command=obter_cotacao)
botao_obter_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='NSEW')

rotulo_cotacao_varias_moedas = tk.Label(text='Cotação de Múltiplas Moedas', borderwidth=2, relief='solid')
rotulo_cotacao_varias_moedas['font'] = fonte_titulo
rotulo_cotacao_varias_moedas.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='NSEW')

rotulo_selecionar_planilha = tk.Label(text='Selecione uma planilha do Excel com as moedas na coluna A:')
rotulo_selecionar_planilha.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')


def selecionar_planilha():
    # Obtém o caminho absoluto do arquivo selecionado
    caminho_planilha = askopenfilename()
    
    # Exibe o caminho do arquivo
    # rotulo_caminho_planilha['text'] = caminho_planilha
    
    
botao_selecionar_planilha = tk.Button(text='Selecionar Planilha', command=selecionar_planilha)
botao_selecionar_planilha.grid(row=5, column=2, padx=10, pady=10, sticky='NSEW')

rotulo_planilha_selecionada = tk.Label(text='Planilha selecionada:')
rotulo_planilha_selecionada.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')

rotulo_caminho_planilha = tk.Label(text='')
rotulo_caminho_planilha.grid(row=6, column=2, padx=10, pady=10, sticky='NSEW')

rotulo_data_inicial = tk.Label(text='Data Inicial:')
rotulo_data_inicial.grid(row=7, column=0, padx=10, pady=10, sticky='NSEW')

campo_data_inicial = DateEntry(year=2023, locale='pt_br')
campo_data_inicial.grid(row=7, column=1, padx=10, pady=10, sticky='NSEW')

rotulo_data_final = tk.Label(text='Data Final:')
rotulo_data_final.grid(row=8, column=0, padx=10, pady=10, sticky='NSEW')

campo_data_final = DateEntry(year=2023, locale='pt_br')
campo_data_final.grid(row=8, column=1, padx=10, pady=10, sticky='NSEW')


def obter_cotacoes():
    pass


botao_atualizar_cotacoes = tk.Button(text='Obter Cotações', command=obter_cotacoes)
botao_atualizar_cotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='NSEW')

rotulo_mensagem_sucesso = tk.Label(text='')
rotulo_mensagem_sucesso.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='NSEW')


def fechar_janela():
    '''Fecha a janela.'''
    janela.destroy()


botao_fechar_janela = tk.Button(text='FECHAR', command=fechar_janela)
botao_fechar_janela.grid(row=10, column=2, padx=10, pady=10, sticky='NSEW')

# Coloca a janela em loop
janela.mainloop()