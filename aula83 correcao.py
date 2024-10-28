perguntas = [
  {
    'Pergunta': 'Quanto é 2 + 2 ?',
    'Opções': ['1', '3', '4', '5'], # PERGUNTA 1
    'Resposta': '4',
  },
  {
    'Pergunta': 'Quanto é 5 x 5 ?', 
    'Opções': ['25', '55', '10', '51'], # PERGUNTA 2
    'Resposta': '25',
  },
  {
    'Pergunta': 'Quanto é 10 / 2 ?',
    'Opções': ['4', '5', '2', '1'], # PERGUNTA 3
    'Resposta': '5',
  }
]

qtdAcertos = 0
for pergunta in perguntas:
  print('Pergunta', pergunta['Pergunta'])
  print()
  
  opcoes = pergunta['Opções']
  for i, opcao in enumerate(opcoes):
    print(f'{i})', opcao)
  print()

  escolha = input('Escolha uma opção: ')

  escolhaInteiro = None
  acertou = False
  qtdOpcoes = len(opcoes)
  
  if escolha.isdigit():
    escolhaInteiro = int(escolha)

  if escolhaInteiro is not None:
    if escolhaInteiro >= 0 and escolhaInteiro < qtdOpcoes:
      if opcoes[escolhaInteiro] == pergunta['Resposta']:
        acertou = True

  if acertou:
    qtdAcertos += 1
    print('Acertou')
  else:
    print('Errou')

  print()