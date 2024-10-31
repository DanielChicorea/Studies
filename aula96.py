produtos = [
  {'nome': 'p1', 'preco': 10},
  {'nome': 'p2', 'preco': 20},
  {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
  {**produto, 'preco': produto['preco'] * 1.05}
  if produto['preco'] > 20 else {**produto}
  for produto in produtos
  if produto['preco'] > 10

]

# MAPEAMENTO É QUANDO ESTOU MANIPULANDO OS DADOS DE UMA LISTA
# MODIFICANDO OS VALORES MAS MANTENDO O MESMO TAMANHO

# FILTRO É QUANDO QUERO RETIRAR VALORES DETERMINADOS DA MINHA LISTA
# MODIFICANDO O TAMANHO DA LISTA


print(novos_produtos)
