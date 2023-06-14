"""
FAÇA UM PROGRAMA QUE CALCULE A SOMA
ENTRE TODOS OS NÚMEROS IMPARES QUE
SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM
NO INTERVALO DE 1 ATÉ 500.
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t ANALISE NÚMERICA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

for c in range(1, 501):
      resto = c % 3

      if resto == 0:
            print('A soma é {}'.format(c + c))
