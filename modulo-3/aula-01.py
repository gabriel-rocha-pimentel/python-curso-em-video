"""
CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA
COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE.

SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO ENTRE 0 E 20
E MOSTRÁ-LO POR EXTENSO.
"""
print('_' * 50)
print('\t\t\t\tNÚMERO POR EXTENSO')
print('_' * 50)

contagem_num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
contagem_string = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
                   "Oito", 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
                   "Quinze", 'Dezesseis', 'Dezessete', 'Deszoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Escreva um número entre 0 e 20 : '))
    value = bool(contagem_num.count(num))
    opcao = input('\nQuer continuar ? [S|N] : ').strip().upper()[0]

    if value:
        print(f'Você escreveu {contagem_string[num]}.')
    if opcao == 'S':
        continue
    else:
        print('OBRIGADO! Volte em breve.')
        break
