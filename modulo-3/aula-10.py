"""
CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS
E COLOCAR EM UMA LISTA. DEPOIS DISSO, MOSTRE:

1 - QUANTOS NÚMEROS FORAM DIGITADOS.
2 - A LISTA DE VALORES, ORDENADA DE FORMA
DECRESCENTE.
3 - SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO
NA LISTA.
"""
print('_' * 50)
print(f'{"+++++ EXTRAINDO DADOS +++++":^50}')
print('_' * 50)

numeros = []
n = 0

while True:
    numero = int(input('\nEscreva um número : '))
    if n == 0 or numero >= numeros[0]:
        numeros.insert(0, numero)
        print('Numero inserido no inicio da lista...')

    elif len(numeros) >= 2:
        p = 0
        while p <= len(numeros):
            if numeros[p] >= numero >= numeros[p + 1]:
                numeros.insert(p + 1, numero)
                print(f'Numero inserido na posição {p} da lista...')
                break
            else:
                numeros.append(numero)
            p += 1
            break
    else:
        numeros.append(numero)
    n += 1

    opcao = input('Quer continuar ? [SIM | NÃO] : ').strip().upper()[0]
    if opcao == 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(numeros)}.')
print(f'Os valores em ordem decrescente são {numeros}.')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
