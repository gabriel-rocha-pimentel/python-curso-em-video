"""
CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS
PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO
DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA.

NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS
E QUAL FOI A SOMA ENTRE ELES.
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t CONSIDERE A SOMA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

soma = count = 0
while True:
      num = int(input('Escreva um valor (Escreva 999 para parar): '))
      if num != 999:
            count += 1
            soma += num
      else:
            break
print(f'\nA soma dos {count} valores foi {soma}!')
