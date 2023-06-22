"""
LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS
10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE.
"""

print('*{}*\n '
      '\t\t\t\t\t\t\t\t GERADOR DE PA'
      '\n*{}*'.format('-+-' * 30, '-+-' * 30))

primeiro_termo = int(input('Escreva o Primeiro termo da PA : '))
razao = int(input('Escreva a Razão da PA : '))

count = 1
while count <= 10:
      print(primeiro_termo, end=' => ')
      primeiro_termo += razao
      count += 1

print('FIM')

