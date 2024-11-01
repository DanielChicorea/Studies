"""
MÉTODOS ÚTEIS DOS DICIONÁRIOS EM PYTHON

LEN - QUANTAS CHAVES
KEYS = ITERÁVEL COM AS CHAVES
VALUES = ITERÁVEL COM OS VALORES
ITEMS = ITERÁVEL COM AS CHAVES E VALORES
SETDEFAULT = ADICIONA VALOR SE A CHAVE NÃO EXISTE
COPY = RETORNA UMA CÓPIA RASA (SHALLOW COPY)
GET - OBTÉM UMA CHAVE
POP - APAGA UM ITEM COM A CHAVE ESPECIFICADA (DEL)
POITEM - APAGA O ÚLTIMO ITEM ADICIONADO
UPDATE - ATUALIZA UM DICIONÁRIO COM OUTRO
"""
import copy

Dict1 = {
  'Chave 1': 1,
  'Chave 2': 2,
  'Lista 1': [0, 1, 2]
}

Dict2 = Dict1.copy()
Dict3 = copy.deepcopy(Dict1)


Dict2 = Dict1

Dict1['Chave 2'] = 4
Dict1['Lista 1'][0] = 2

print(Dict2)
print(Dict3)
print(Dict1)