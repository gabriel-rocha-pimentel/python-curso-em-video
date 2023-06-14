"""
DESENVOLVA UM PROGRAMA QUE LEIA SEIS
NÚMEROS INTEIROS E MOSTRE A SOMA
APENAS DAQUELES QUE FOREM PARES.

SE O VALOR DIGITADO FOR IMPAR.
DESCONSIDERE-O.
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t ANALISE NÚMERICA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))
count = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite um número : '))
    par = num % 2

    if par == 0:
        soma = soma + num
        count = count + 1
print('A soma de todos os números pares é {}.\n'
      'E o total de números pares é {}'.format(soma, count))
