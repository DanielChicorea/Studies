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

pessoa = {
  'nome': 'Daniel',
  'sobrenome': 'Chicorea',
}

print(len(pessoa))
print(pessoa.__len__())

print(list(pessoa.keys()))

print(list(pessoa.values()))

print(list(pessoa.items()))

print(pessoa.setdefault('idade', 29))

print(list(pessoa.items()))
