"""
ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO
QUALQUER E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA
SEQUÊNCIA DE FIBONACCI.
"""
# F(n + 2) = F(n + 1) + F(n) ,

print('*{}*\n'
      '\t\t\t\t SEQUÊNCIA DE FIBONACCI'
      '\n*{}*'.format('_' * 50, '_' * 50))

termos = int(input('\nQuantos termos você quer mostrar ? '))
t1 = 0
t2 = 1
count = 3

print('{}'.format('~' * 50))
print('{} --> {}'.format(t1, t2), end=' --> ')
while count < termos + 1:
    count += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{}'.format(t3), end=' --> ')

print('FIM')
print('{}'.format('~' * 50))
