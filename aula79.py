# MANIPULANDO CHAVES E VALORES EM DICIONARIOS

pessoa = {} # DICIONARIO CRIADO


chave = 'nome' # CHAVE CRIADA

pessoa[chave] = 'Daniel' # DEFINIDO O VALOR DA CHAVE
pessoa['sobrenome'] = 'Chicorea' # CRIADA UMA NOVA CHAVE E DEFINIDO SEU VALOR


print(pessoa) 

pessoa[chave] = 'Maria' # DEFINIDO O VALOR DA CHAVE

print(pessoa)

# del pessoa['sobrenome']
# print(pessoa)

print(pessoa['nome']) # MOSTRANDO O VALOR DA CHAVE NOME

if pessoa.get('sobrenome') is None:
  print('NÃO EXISTE')

else:
  print(pessoa['sobrenome'])

# VERIFICAÇÃO PARA SABER SE A CHAVE SOBRENOME EXISTE
# SE NÃO EXISTIR MOSTRAR MENSAGEM "NÃO EXISTE"

# SE EXISTIR, MOSTRAR VALOR DA CHAVE 'SOBRENOME'