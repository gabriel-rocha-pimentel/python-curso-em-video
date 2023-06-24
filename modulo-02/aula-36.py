"""
CRIE UM PROGRAMA QUE SIMULE UM CAIXA ELETRONICO.
NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO
(NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA
VALOR SERÃO ENTREGUES.

OBSERVAÇÃO --> CONSIDERE QUE O CAIXA POSSUI VALORES FIXOS DE:
R$50, R$20 R$10 E R$1
"""
print('{} \n'
      '\t\t\t\t\t\t\t\tIternetional BANK'
      '\n {}'.format('-=-' * 30, '-=-' * 30))
num_notas = 0
valor = int(input('Insira o valor do saque : R$'))

for num_notas in range(valor):
      num_notas += 1
      if num_notas == 100:
            print(f'Total de {int(valor / 100)} cédulas de R$100')
      elif num_notas == 50:
            print(f'Total de {int(valor / 50)} cédulas de R$50')
      elif num_notas == 20:
            print(f'Total de {int(valor / 20)} cédulas de R$20')
      elif num_notas == 10:
            print(f'Total de {int(valor / 10)} cédulas de R$10')
      elif num_notas == 1:
            print(f'Total de {int(valor / 1)} cédulas de R$1')
print('=' * 30)
