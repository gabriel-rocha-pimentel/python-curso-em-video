"""

Desenvolva um prgrama que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 para viagens mais longas.

"""

km = float(input('Digite a quantidade kilometros rodados : Km '))

if km <= 200:
    print('Você deve pagar um valor de R${:.2f} Reais.'.format(km * 0.50))
else:
    print('Você deve pagar um valor de R${:.2f} Reais.'.format(km * 0.45))
