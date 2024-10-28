# Exemplo de uso dos SETS

letras = set()

while True:
  letra = input('Digite uma letra: ')
  letras.add(letra)
  print(letras)

  if 'l' in letras:
    print('Parabéns!')
    break