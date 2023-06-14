"""
FAÇA UM PROGRAMA QUE LEIA
UM NÚMERO INTEIRO E DIGA SE ELE
É OU NÃO UM NÚMERO PRIMO.
"""
# MEU CÓDIGO DO EXERCÍCIO
print('{} \n '
      '\t\t\t\t\t\t\t\t ANALISE NÚMERICA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

num = int(input('Digite um número : '))
lista = []

for a in range(1, num + 1):
    if num % a == 0:
        lista += [a]
        print(a, end=' ')

primo = len(lista)
print('\nO número {} foi divisivel {} vezes.'
      .format(num, primo))

if primo == 2:
    print('O número {} é PRIMO!!'.format(num))
else:
    print('Tente novamente, o número {} não é PRIMO!!'.format(num))

print('\n{}\n'.format('-=-' * 20))

# CÓDIGO DO PROFESSOR GUANABARA

num = int(input('Digite um número : '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
