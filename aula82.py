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

# print(pessoa.get('sobrenome'))
# print(pessoa.get('idade', 'Não existe!'))

# print(pessoa)
# pessoa.pop('nome')
# print(pessoa)

# pessoa.setdefault('idade', 80)
# print(pessoa)
# pessoa.popitem()
# print(pessoa)

# pessoa.update({
#   'nome': 'Otavio',
#   'idade': 20,
# })
# print(pessoa)

# pessoa.update(nome = 'Julia')
# print(pessoa)

# tupla = (('nome', 'Igor'), ('sobrenome', 'Monteiro'))
# pessoa.update(tupla)
# print(pessoa)