"""
DICIONÁRIOS EM PYTHON (TIPO DICT)

DICIONÁRIOS SÃO ESTRUTURAS DO TIPO PAR DE "CHAVE" E "VALOR"
CHAVES PODEM SER CONSIDERADAS COMO O "INDICE" QUE VIMOS
NA LISTA E PODEM SER DE TIPOS IMUTÁVEIS
COMO: STR, INT, FLOAT, BOOL, TUPLE, ETC.
O VALOR PODE SER DE QUALQUER TIPO, INCLUINDO OUTRO DICIONÁRIO
USAMOS AS CHAVES {} OU A CLASSE DICT PARA CRIAR DICIONÁRIOS
IMUTÁVEIS: STR, INT, FLOAT, BOOL, TUPLE
MUTÁVEIS: DICT, LIST
"""

pessoa = {
  'nome': 'Daniel',
  'sobrenme': 'Chicorea',
  'idade': 18,
  'altura': 1.8,
  'enderecos': [
    {'Rua': 'tal tal', 'número': 123},
    {'Rua': 'outra rua', 'número': 321},
  ]
}

print(pessoa['nome'])
print(pessoa['sobrenme'])

for chave in pessoa:
  print(chave, pessoa[chave])