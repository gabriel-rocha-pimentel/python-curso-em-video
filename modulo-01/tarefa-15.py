"""

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.

"""

km = float(input('Insira aqui a velocidade do seu carro : Km '))

multa = (km - 80) * 7.00

if km > 80.0:
    print('\nVocê passou do limite.')
    print('E você devera pagar uma multa no valor de R${:.2f} Reais.'.format(multa))
else:
    print('\n Sua velocidade não está acima do limite de velocidade.')
