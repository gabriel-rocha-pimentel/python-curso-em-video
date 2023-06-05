"""

Escreva um programa que faça o computador pensar
em um número inteiro entre 0 e 5 e peça para o usuario
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela
se o usuário venceu ou perdeu.

import random
print('¨' * 20)
num = int(input('Digite um número entre 0 e 5 \n pra adivinhar o número que estou pensando : '))
print('¨' * 20)

value = random.randint(1, 5)

if value == num:
    print('CONGRATULATIONS!!! Você venceu :)')
else:
    print('Sinto muito, este resposta está errada.\n O número que pensei foi {}.'.format(value))


"""

from random import randint

num = int(input('{} \n Adivinhe o número que estou pensando : \n {}'.format(('__--__' * 20), ('__--__' * 20))))

if randint(1, 5) == num:
    print('CONGRATULATIONS!!! Você venceu :)')
else:
    print('Sinto muito, este resposta está errada.\n O número que pensei foi {}.'.format(randint(1, 5)))
