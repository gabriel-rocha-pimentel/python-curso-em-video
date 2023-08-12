"""
Faça um programa que leia nome e média
de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo
da estrutura na tela.
"""
print('_' * 50)
print(f'{"+++++ Dicionario em Python +++++":^50}')
print('_' * 50)
notas = dict()

notas['nome'] = str(input('Nome: '))
notas['media'] = float(input(f'Média de {notas["nome"]}: '))
print('-=' * 50)
print(f'\n- Nome é igual a {notas["nome"]}')
print(f'- Média é igual a {notas["media"]}')
if notas['media'] >= 7:
      notas['situação'] = 'PASSOU'
      print(f'- Situação é igual a {notas["situação"]}!!!')
elif notas['media'] < 5:
      notas['situação'] = 'REPROVADO'
      print(f'- Situação é igual a {notas["situação"]}!!!')
else:
      notas['situação'] = 'RECUPERAÇÃO'
      print(f'- Situação é igual a {notas["situação"]}!!!')
print(notas)
