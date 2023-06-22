"""
FAÇA UM JOGO ONDE O COMPUTADOR  VAI PENSAR EM UM NÚMERO ENTRE 0 E 10.
SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR,
MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.
"""
from random import randint

print('{} \n '
      '\t\t\t\t\t\t\t\t JOGO - ADIVINHAÇÃO'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

player1 = int(input('Adivinhe um número : '))
player2 = randint(0, 10)
jogadas = 0

while not player1 == player2:
      if player2 > player1:
            player1 = int(input('\nO número deveria ser maior...\nTente outra vez : '))
      elif player2 < player1:
            player1 = int(input('\nO número deveria ser menor...\nTente outra vez : '))
      jogadas += 1

print('\nPARABÉNS JOGADOR!!! Acertou com apenas {} jogadas'.format(jogadas + 1))
