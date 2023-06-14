"""
DESENVOLVA UM PROGRAMA QUE LEIA O
PRIMEIRO TERMO E A RAZÃO DE UMA PA.
NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS
DESSA PROGRESSÃO.
"""
print('{} \n '
      '\t\t\t\t\t\t\t\t 10 TERMOS DE UMA PA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

num = int(input('Digite o primeiro termo da PA : '))
razao = int(input('Agora digite a razão : '))

decimo = num + (10 - 1) * razao

for c in range(num, decimo + razao, razao):
      print('{}'.format(c), end=' --> ')
print('FIM!')
