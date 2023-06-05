"""
Crie um programa que leia um número Real qualquer pelo teclado,
e mostre na tela a sua porção inteira.
"""

from math import floor

num = float(input('\033[0;32mDigite um número : '))

print('\033[0;32mA porção inteira do seu número é {} '.format(floor(num)))
