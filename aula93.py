# Empacotamento e Desempacotamento de dicionarios

# a, b = 1, 2
# a, b = b, a
# print(a, b)

# pessoa = {
#   'nome': 'Aline',
#   'sobrenome': 'Souza',
# }

# dados_pessoa = {
#   'idade': 18,
#   'altura': 1.6,
# }

# pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)


# args e kwargs
# args já vimos
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
  print('NÃO NOMEADOS', args)
  
  for chave, valor in kwargs.items():
    print(chave, valor) 

# mostro_argumentos_nomeados(nome = 'Joana', qlq = 123)
# mostro_argumentos_nomeados(1, 2, 3, 4)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
  'configuracao1': 1,
  'configuracao2': 2,
  'configuracao3': 3,
  'configuracao4': 4,
  'configuracao5': 5,
}

mostro_argumentos_nomeados(**configuracoes)
mostro_argumentos_nomeados('Daniel', 'Nicoly')
