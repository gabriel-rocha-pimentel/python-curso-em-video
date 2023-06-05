"""
Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.
"""

import math

angulo = float(input('Escreva um ângulo : '))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('Os resultados estão logo abaixo:'
      ' \n Seno >>> {:.2f}'
      '\n Cosseno >>> {:.2f}'
      '\n Tangente >>> {:.2f}'
      .format(seno, cos, tang))
