"""
Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""


# --- TITULO ---
print('{} \n '
      '\t\t\t\t\t\t\t\t PROGRAMA DE COMPARAÇÃO'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

num1 = int(input('Digite um número : '))
num2 = int(input('Digite outro para comparar : '))

if num1 > num2:
    print('{} é o maior.'.format(num1))
elif num1 == num2:
    print('{} e {} são iguais.'.format(num1, num2))
else:
    print('{} é o maior.'.format(num2))

