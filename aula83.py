# EXERCICIOS - SISTEMA DE PERGUNTAS E RESPOSTAS

import os
from time import sleep


def clearScreen():
   os.system('cls')

def viewQuestions():
   for posicao, valor in enumerate(perguntas[0]['Opções']):
      print(f'{posicao+1}) {valor}')

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

while True:
  # PERGUNTA 1
  print(perguntas[0]["Pergunta"])
  viewQuestions()
  
  while True:
      escolha = str(input('Escolha: '))
      if escolha == perguntas[0]["Resposta"]:
        print("Parabens! Você acertou!")
        break
      else:  
        print('Resposta Incorreta, tente novamente!')  
        
  sleep(2)
  clearScreen()

  # PERGUNTA 2
  print(perguntas[1]["Pergunta"])
  viewQuestions()

  while True:
    escolha1 = str(input('Escolha: '))
    if escolha1 == perguntas[1]["Resposta"]:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Resposta Incorreta, tente novamente!")
  
  sleep(2)
  clearScreen()
  
  # PERGUNTA 3
  print(perguntas[2]["Pergunta"])
  viewQuestions()

  while True:
    escolha2 = str(input('Escolha: '))
    if escolha2 == perguntas[2]["Resposta"]:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Resposta Incorreta, tente novamente!")
    
  sleep(2)
  clearScreen()
    
  if escolha == perguntas[0]["Resposta"] and escolha1 == perguntas[1]["Resposta"] and escolha2 == perguntas[2]["Resposta"]:
      print('Parabens! Você acertou todas as perguntas!')
  break





