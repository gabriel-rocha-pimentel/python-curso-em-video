"""
CRIE UM PROGRAMA ONDE O USURÁRIO POSSA DIGITAR
CINCO VALORES NÚMERICOS E CADASTRE-OS EM UMA LISTA,
JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT()).

NO FINAL, MOSTRE A LISTA ORDENADA NA TELA.
"""
print('_' * 50)
print(f'{"+++++ LISTA ORDENADA +++++":^50}')
print('_' * 50)

numeros = []
for n in range(0, 5):
    numero = int(input('\nEscreva um número : '))
    if n == 0 or numero >= numeros[-1]:
        numeros.append(numero)
        print('Numero inserido no final da lista...')
    else:
        p = 0
        while p < len(numeros):
            if numero <= numeros[p]:
                numeros.insert(p, numero)
                print(f'Numero inserido na posição {p} da lista...')
                break
            p += 1
print('-='*30)
print(f'Os valores digitados em ordem são {numeros}.')
