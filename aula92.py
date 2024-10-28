def executa(funcao, *args):
  return funcao(*args)

# def soma(x, y):
#   return x + y

print(
  executa(
    lambda x, y: x + y,
    2, 5
  ),
  # executa(soma, 2, 3)
)

# def criarMultiplicacao(multiplicador):
#   def multiplica(numero):
#     return numero * multiplicador
#   return multiplica

duplica = executa(
  lambda m: lambda n: m * n,
  6
)
print(duplica(4))

def saudacao(nome):
  return f'Ola, {nome}'

print(
  executa(
    lambda nome: nome,
    'Daniel'
  )
)