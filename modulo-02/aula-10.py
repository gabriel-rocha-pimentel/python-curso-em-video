"""
Crie um programa que faça o computador jogar
Jokempô com você.
"""

from random import randint

print('{} \n '
      '\t\t\t\t\t\t\t\t JOGO - PEDRA PAPEL E TESOURA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

print('-=--=--=--=- OPÇÕES -=--=--=--=- \n'
      '[1] PEDRA \n'
      '[2] PAPEL \n'
      '[3] TESOURA \n')

player1 = int(input('Escolha uma opção : '))

player2 = int(randint(1, 3))

if player1 != player2:
    # computador vence
    if player1 == 1 and player2 == 2:
        print('Computador escolhe PAPEL'
              '\nCOMPUTADOR VENCE')
    elif player1 == 2 and player2 == 3:
        print('Computador escolhe TESOURA'
              '\nCOMPUTADOR VENCE')
    elif player1 == 3 and player2 == 1:
        print('Computador escolhe PEDRA'
              '\nCOMPUTADOR VENCE')

    # Jogador vence
    elif player1 == 2 and player2 == 1:
        print('Computador escolhe PEDRA'
              '\nJOGADOR VENCE')
    elif player1 == 3 and player2 == 2:
        print('Computador escolhe PAPEL'
              '\nJOGADOR VENCE')
    elif player1 == 1 and player2 == 3:
        print('Computador escolhe TESOURA'
              '\nJOGADOR VENCE')
else:
    print('EMPATE')
