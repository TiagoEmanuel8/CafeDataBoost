import csv
import collections


# lendo o csv
def leitura_csv(path_file):
    with open(path_file) as file:
        dados_csv = csv.reader(file)
        # quero ler o csv e iterar em lista
        dados_lista = [indice for indice in dados_csv]
    return dados_lista


# prato mais pedido por maria
def pedidos_preferidos_maria(data):
    filtra_pratos = [indice[1] for indice in data if indice[0] == 'maria']
    # counter vai me trazer as chaves e valores dos pratos de maria, num dict
    resposta = collections.Counter(filtra_pratos)
    # esse key é semelhante ao object.key() do js
    return max(resposta, key=resposta.get)


# quantas vezes arnaldo pediu hamburguer?
def arnaldo_pedidos_hamburguer(data):
    # mesmo raciocínio da função anterior
    filtra_prato = [item[1] for item in data if item[0] == 'arnaldo']
    return filtra_prato.count('hamburguer')


# quais pratos joão nunca pediu?
# para fazer esses requisito, fiz baseado na teoria de conjuntos
def joao_nunca_pediu(data):
    # filtra todos os pratos do joão
    pratos_joao = {item[1] for item in data if item[0] == 'joao'}
    # filtra todos os pratos do csv
    pratos_gerais = {item[1] for item in data if item[1]}
    # complementar de conjuntos
    return pratos_gerais - pratos_joao


# quais dias joão nunca foi na lanchonete?
# mesmo raciocínio da função anterior
def joao_nao_frequentou(data):
    foi = {item[2] for item in data if item[0] == 'joao'}
    geral = {item[2] for item in data if item[1]}
    return geral - foi


# escrevendo nos arquivos
def analyze_log(path_to_file):
    dados_csv = leitura_csv(path_to_file)
    with open("data/mkt_campaign.txt", "w") as file:
        file.write((pedidos_preferidos_maria(dados_csv)) + "\n")
        file.write(str(arnaldo_pedidos_hamburguer(dados_csv)) + "\n")
        file.write(f"{joao_nunca_pediu(dados_csv)}\n")
        file.write(f"{joao_nao_frequentou(dados_csv)}\n")
