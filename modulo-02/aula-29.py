"""
CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
O PROGRAMA SÓ VAI PARA QUANDO O VALOR DIGITADO FOR 999,
QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NUMEROS
FORAM DIGITADOS E QUAL FOI SOMA ENTRE ELES (DESCONSIDERANDO O FLAG)
"""

print('*{}*\n '
      '\t\t\t\t\t\t\t\t ANALISE NÚMERICA'
      '\n*{}*'.format('-+-' * 30, '-+-' * 30))

n1 = num1 = 0
while not num1 >= 999:
      n1 += 1
      num1 += int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(n1 - 1, num1 - 999))

