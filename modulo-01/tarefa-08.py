"""
Faça um programa que leia um número de 0 a 9.999 e mostre na tela
cada um dos dígitos separados.

Exemplo : Digite 1.834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

num = int(input('Insira um número por favor - - - > '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade : {} \n'
      'Dezena : {} \n'
      'Centena : {} \n'
      'Milhar : {}.'.format(u, d, c, m))
