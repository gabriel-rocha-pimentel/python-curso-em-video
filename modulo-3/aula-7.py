"""
FAÇA UM PROGRAMA QUE LEIA 5 VALORES NÚMERICOS E GUARDE
EM UMA LISTA.
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR
DIGITADOS E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.
"""
print('_' * 50)
print(f'{"+++++ LISTAGEM DE PREÇOS +++++":^50}')
print('_' * 50)

numeros = []
maior = menor = 0

for n in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {n}: ')))
    menor = min(numeros)
    maior = max(numeros)

print(f'\nVocê digitou os valores {numeros}.')
print(f'O maior valor digitado foi {maior}, na posição : ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}', end=', ')
print(f'\nO menor valor digitado foi {menor}, na posição : ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}', end=', ')
