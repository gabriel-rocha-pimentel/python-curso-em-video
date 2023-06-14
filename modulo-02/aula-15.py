"""
REFAÇA O DESAFIO 009, MOSTRANDO
A TABUADA DE UM NÚMERO QUE O USUÁRIO
ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t CONSULTA DE TABUADA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))


num = int(input('Digite um valor : '))

for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c))
