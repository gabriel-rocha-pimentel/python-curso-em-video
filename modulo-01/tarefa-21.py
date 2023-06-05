"""
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triãngulo.
"""

print('{} \n ANALISANDO TRIÂNGULOS \n {}'.format(('-=-' * 20), ('-=-' * 20)))

a = float(input('Insira o valor da primeira reta : '))
b = float(input('Insira o valor da segunda reta : '))
c = float(input('Insira o valor da terceira reta : '))

if a < b + c and b < a + c and c < a + b:
    print('Os comprimentos estão corretos portanto formam um Triângulo.')
else:
    print('Estes valores não combinam. Tente novamente.')
