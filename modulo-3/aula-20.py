"""
Crie um programa que leia nome, ano de nascimento
e carteira de trabalho de uma pessoa e cadastre-os(com idade)
em um dicionario se por acaso a CTPS for diferente de zero,
o dicionario recebera também o ano de contratação e o salãrio.
Calcule e acresente, além da idade, com quantos anos
a pessoa vai se aposentar.
"""
from datetime import datetime
ano_atual = datetime.today().year
print('_' * 50)
print(f'{"+++++ BOLETIM ESCOLAR +++++":^50}')
print('_' * 50)
cras = dict()
while True:
      cras['NOME'] = input('NOME: ')
      cras['NASCIMENTO'] = int(input('ANO DE NASCIMENTO: '))
      cras['CDT'] = int(input('CARTEIRA DE TRABALHO (0 NÃO TEM) : '))
      cras.copy()
      idade = ano_atual - cras['NASCIMENTO']
      if cras["CDT"] == 0:
            print('-=' * 50)
            print(f'- NOME TEM O VALOR {cras["NOME"]}')
            print(f'- IDADE TEM O VALOR {idade}')
            print(f'- CTPS TEM O VALOR {cras["CDT"]}')
            break
      else:
            cras["CONTRATO"] = int(input('ANO DE CONTRATAÇÃO: '))
            cras["SALARIO"] = float(input('SALÁRIO: R$'))
            print('-=' * 50)
            aposentadoria = (idade + 35) - (ano_atual - cras['CONTRATO'])

            print(f'- NOME TEM O VALOR {cras["NOME"]}')
            print(f'- IDADE TEM O VALOR {idade}')
            print(f'- CTPS TEM O VALOR {cras["CDT"]}')
            print(f'- CONTRATAÇÃO TEM O VALOR {cras["CONTRATO"]}')
            print(f'- SALÁRIO TEM O VALOR {cras["SALARIO"]}')
            print(f'- APOSENTADORIA TEM O VALOR {aposentadoria}')
            break
