lista = []

for x in range(4):
  for y in range(4):
    lista.append((x, y))

lista1 = [
  (x, y) # MAPEAMENTO
  for x in range(4)
  for y in range(4)
]

lista2 = [
  [letra for letra in 'Luiz']
  for x in range(3)
]

print(lista)
print(lista1)
print(lista2) 