# LIST COMPREHENSION EM PYTHON
# LIST COMPREHENSION É UMA FORMA RÁPIDA PARA CRIAR LISTAS
# A PARTIR DE ITERÁVEIS

# print(list(range(0, 10)))

# lista = []
# for numero in range(0, 11):
#   if numero % 2 == 0:
#     lista.append(numero)
#   else:
#     continue

lista = [numero for numero in range(11)]
print('Minha Lista Primária', lista)

lista1 = [
  numero * 2
  for numero in range(11)
]

print('Minha Lista Secundária', lista1)