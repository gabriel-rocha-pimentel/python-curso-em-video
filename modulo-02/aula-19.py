"""
CRIE UM PROGRAMA QUE LEIA UMA FRASE
QUALQUER E DIGA SE ELA É UM PALINDROMO.

DESCONSIDERANDO OS ESPAÇOS.
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t É UM PALINDROMO ?'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

frase = input('Escreva uma frase >>> ').strip()

palindromo = frase[::-1]

print('O inverso de [{}], é [{}].'.format(frase, palindromo))
if frase == palindromo:
      print('A palavra [{}], é um PALINDROMO!!'.format(frase))
else:
      print('A palavra [{}], não é um PALINDROMO!!'.format(frase))
