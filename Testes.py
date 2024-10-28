dictonary = {
  'nome': 'Daniel',
  'sobrenome': 'Chicore',
  'numeros': [
    1, 2, 3, 4,
  ],
}

for indice, valor in enumerate(dictonary['numeros']):
  print(f'Indice: {indice+1}, Valor: {valor}')

perguntas = [
  {
    'Pergunta': 'Quanto é 2+2 ?',
    'Opções': ['1', '3', '4', '5'], # PERGUNTA 1
    'Resposta': '4',
  },
  {
    'Pergunta': 'Quanto é 5*5 ?', 
    'Opções': ['25', '55', '10', '51'], # PERGUNTA 2
    'Resposta': '25',
  },
  {
    'Pergunta': 'Quanto é 10/2 ?',
    'Opções': ['4', '5', '2', '1'], # PERGUNTA 3
    'Resposta': '5',
  }
]


def viewQuestions():
   for posicao, valor in enumerate(perguntas[0]['Opções']):
      print(f'{posicao+1}) {valor}')

viewQuestions()