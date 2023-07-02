"""
CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEÁTORIOS
E COLOCAR EM UMA TUPLA.

DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM
INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.
"""
from random import randint
print('_' * 50)
print('\t\t\t++++++ MAIOR E MENOR VALOR ++++++')
print('_' * 50)

numeros = (randint(1 * 10, 5 * 10),
           randint(1 * 10, 5 * 10),
           randint(1 * 10, 5 * 10),
           randint(1 * 10, 5 * 10),
           randint(1 * 10, 5 * 10)
           )

maior = max(numeros)
menor = min(numeros)

print(f'Os valores sorteados foram :'
      f'\n[{numeros[0]}],'
      f'\n[{numeros[1]}],'
      f'\n[{numeros[2]}],'
      f'\n[{numeros[3]}],'
      f'\n[{numeros[4]}]'
      )
print(f'O maior valor sorteado foi [{maior}]')
print(f'E o menor valor sorteado foi [{menor}]')
