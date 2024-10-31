# DIR, HASATTR E GETATTR EM PYTHON

string = 'Daniel'
metodo = 'upper'

if hasattr(string, 'upper'):
  print('Existe upper aqui')
  print(getattr(string, metodo)())

else:
  print('Não existe o método aqui!')