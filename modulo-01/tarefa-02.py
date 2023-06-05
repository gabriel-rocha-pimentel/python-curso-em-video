"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo ratãngulo, calcule
e mostre o comprimento da hipotenusa.
"""
from math import hypot

cat_oposto = float(input('Insira aqui o cateto oposto : '))
cat_adjacente = float(input('Insira aqui o cateto adjacente : '))

print('O comprimento da Hipotenusa é {:.2f}'.format(hypot(cat_oposto, cat_adjacente)))
