"""
FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER
E MOSTRE O SEU FATORIAL
"""
from math import factorial
print('*{}*\n '
      '\t\t\t\t\t\t\t\t ANALISE NÚMERICA'
      '\n*{}*'.format('-+-' * 30, '-+-' * 30))

fatorial = int(input('Escreva um número\n'
                     'para calcular seu Fatorial : '))
count = fatorial + 1

print('Calculando {}! = '.format(fatorial), end='')
while count > 0:
    count -= 1
    if count >= 1:
        print(count, end=' x ')
    else:
        print(count, end=' = ')
print(factorial(fatorial), end='')

