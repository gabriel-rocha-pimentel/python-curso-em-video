"""

Faça um programa que leia um ano qualquer e mostre se ele é Bisexto.

"""

ano = int(input('Digite um ano para por em analise : '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é considerado Bisexto.'.format(ano))
else:
    print('O ano {} não é considerado Bisexto'.format(ano))
