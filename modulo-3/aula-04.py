"""
DESENVOLVA UM PROGRAMA QUE LEIA 4 VALORES PELO TECLADO E GUARDE-OS
EM UMA TUPLA. NO FINAL, MOSTRE:

- QUANTAS VEZES APARECEU O VALOR 9
- EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3
- QUAIS FORAM OS NÚMEROS PARES.
"""
print('_' * 50)
print('\t\t\t++++++ ANALISE DE DADOS ++++++')
print('_' * 50)

numeros = (int(input('Digite um número : ')),
           int(input('Digite um número : ')),
           int(input('Digite um número : ')),
           int(input('Digite um número : '))
           )
par = 0
for num in numeros:
    if num % 2 == 0:
        par += 1

print(f'\nVocê escreveu os valores : {numeros}.')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1} posição.')
else:
    print('O valor 3 NÃO FOI ENCONTRADO!!!')
print(f'A quantidade de números pares digitados foi {par}.')
