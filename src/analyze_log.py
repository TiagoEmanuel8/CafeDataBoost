import csv
import collections

def leitura_csv(path_file):
    with open(path_file) as file:
        dados_csv = csv.reader(file)
        dados_lista = [indice for indice in dados_csv]
    return dados_lista

def pedidos_preferidos_maria(data):
    filtra_pratos = [indice[1] for indice in data if indice[0] == 'maria']
    resposta = collections.Counter(filtra_pratos)
    return max(resposta, key=resposta.get)

def arnaldo_pedidos_hamburguer(data):
    filtra_prato = [item[1] for item in data if item[0] == 'arnaldo']
    return filtra_prato.count('hamburguer')

def joao_nunca_pediu(data):
    pratos_joao = {item[1] for item in data if item[0] == 'joao'}
    pratos_gerais = {item[1] for item in data if item[1]}
    return pratos_gerais - pratos_joao

def joao_nao_frequentou(data):
    foi = {item[2] for item in data if item[0] == 'joao'}
    geral = {item[2] for item in data if item[1]}
    return geral - foi

def analyze_log(path_to_file):
    dados_csv = leitura_csv(path_to_file)
    with open("data/mkt_campaign.txt", "w") as file:
        file.write((pedidos_preferidos_maria(dados_csv)) + "\n")
        file.write(str(arnaldo_pedidos_hamburguer(dados_csv)) + "\n")
        file.write(f"{joao_nunca_pediu(dados_csv)}\n")
        file.write(f"{joao_nao_frequentou(dados_csv)}\n")
