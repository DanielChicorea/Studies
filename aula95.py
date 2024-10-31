# LIST COMPREHENSION EM PYTHON
# LIST COMPREHENSION É UMA FORMA RÁPIDA PARA CRIAR LISTAS
# A PARTIR DE ITERÁVEIS

produtos = [
  {'nome': 'p1', 'preco': 10},
  {'nome': 'p2', 'preco': 20},
  {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
  {**produto, 'preco': produto['preco'] * 1.05}
  if produto['preco'] > 15 else {**produto}
  for produto in produtos
]

# print(*novos_produtos, sep = '\n')
print(novos_produtos, sep = '\n')
