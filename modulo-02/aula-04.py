"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta
ou que passou do prazo.
"""

from datetime import date

print('{} \n '
      '\t\t\t\t\t\t\tPROGRAMA DE ALISTAMENTO MILITAR'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

data = int(input('Qual é o ano de nascimento : '))
ano = date.today()
idade = ano.year - data
idade_falta = 18 - idade
print('Quem nasceu em {} tem {} anos em {}.'.format(data, idade, ano.year))

if idade <= 18:
    print("Ainda faltam {} anos para o alistamento.\n"
          "Sua vez será em {}.".format(idade_falta, ano.year + idade_falta))
elif idade >= 18:
    print('Você já deveria ter se alistado, por favor,'
          'vá para a junta militar mais proxima da sua casa\n'
          'e evite pagar uma multa.')
