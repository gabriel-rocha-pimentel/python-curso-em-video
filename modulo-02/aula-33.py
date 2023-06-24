"""
FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O PC.
O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER,
MOSTRANDO O TOTAL DE VITORIAS CONSECUTIVAS QUE ELE
CONQUISTOU NO FINAL DO JOGO.
"""
from random import randrange
print('{} \n '
      '\t\t\t\t\t\t\t\tVAMOS JOGAR PAR OU ÍMPAR'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

count = jogadas = player_1 = player_2 = 0

while True:
      player_1 = int(input('Escreva um número : '))
      player_2 = randrange(player_1 + player_1)

      opcao = input('Par ou Ímpar ? [P | I] >>> ').upper()[0]
      jogadas = player_1 + player_2

      if jogadas % 2 == 0:
            resultado = 'PAR'
      else:
            resultado = 'IMPAR'

      print(f'\nVocê jogou {player_1} e o computador {player_2}.\n'
            f'Total de {jogadas} DEU {resultado}.')

      if opcao == resultado[0].upper() and opcao != ' ':
            count += 1
            print('Você VENCEU!!')
            print('Vamos jogar novamente...')
      else:
            print('Você PERDEU!!')
            print('-=-' * 30)
            print(f'GAME OVER! Você venceu {count} vezes.')
            break

print(f'\nVocê jogou {player_1} e o computador {player_2}.\n'
      f'Total de {jogadas} DEU {resultado}.')
print(f'GAME OVER! Você venceu {count} vezes.')
