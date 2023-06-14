"""
CRIE UM PROGRAMA QUE LEIA O ANO
DE NASCIMENTO DE SETE PESSOAS. NO FINAL,
MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM
A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
"""

from datetime import date

print('{} \n '
      '\t\t\t\t\t\t\t\t MINHA IDADE'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

ano_nascimento = 0
idade = 0
maior_idade = 0
menor_idade = 0

for c in range(1, 8):
      ano_nascimento = int(input('Em que ano a {}ª nasceu ? '.format(c)))

      data_atual = date.today().year
      idade = data_atual - ano_nascimento

      if idade >= 18:
            maior_idade += 1
      else:
            menor_idade += 1
print('\nAo todo tivemos {} pessoas maiores de idade.'.format(maior_idade))
print('Também tivemos {} pessoas menores de idade.'.format(menor_idade))
