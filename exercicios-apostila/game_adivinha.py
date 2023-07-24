from random import random
from math import floor
print('*' * 50)
print(f'*{"JOGO DE ADIVINHAÇÃO":^50}*')
print('*' * 50)
print('Você tem 5 oportunidades de vitória.\n'
      'Conforme o jogo avança você recebe dicas.\n'
      'Adivinhe o número antes que suas chances acabem.\n'
      'BOA SORTE !')
print('*' * 50)
n = random() * 100
numero = floor(n)
chances = 5

for rodadas in range(1, 6):
      chances -= 1

      chute = int(input('\nEu estou pensando em um número, qual você acha que é ?\n>>> '))
      print(f'Você digitou : {chute}')

      acertou = chute == numero
      maior = chute > numero
      menor = chute < numero

      if acertou:
            print('Parabén :)\nVOCÊ ACERTOU !!!')
      elif maior:
            print('Você está indo longe demais, tente um número menor.')
      elif menor:
            print('Seja mais ousado e tente um número maior.')
      print(f'Você está na {rodadas} rodada e chegou com {chances} chances.')
print('*' * 50)
print(f'A resposta correta é {numero}.')
print('GAME OVER')
