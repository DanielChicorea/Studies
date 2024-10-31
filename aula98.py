# DICTIONARY COMPREHENSION E SET COMPREHENSION

produto = {
  'nome': 'caneta azul',
  'preco': 2.5,
  'categoria': 'escritório',
}

dc = {
  chave: valor.upper()
  if isinstance(valor, str) else valor
  for chave, valor
  in produto.items()
  if chave != 'categoria'
}

print(dc)

lista = [
  ('a', 'valor a'),
  ('b', 'valor b'),
  ('c', 'valor c')
]

dc = {
  chave: valor
  for chave, valor
  in lista
}

print(dc)