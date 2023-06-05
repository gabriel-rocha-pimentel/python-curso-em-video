"""
Faça um programa que leia nome, CPF, endereço, idade e altura.
E imprima tudo em um relatório organizado.
"""
print('Por favor insira abaixo algumas informações.')
nome = input('Insira seu Nome : ')
cpf = input('Insira seu CPF : ')
local = input('Insira seu Endereço atual : ')
idade = input('Insira sua Idade atual : ')
alt = input('Insira sua Altura atual : ')

print('\nPor favor confirme suas informações abaixo.\n'
      'Seu nome completo : {}.\n'
      'Seu CPF : {}. \n'
      'Seu endereço atual : {}. \n'
      'Sua idade atual : {}. \n'
      'E por fim sua altura : {}.'
      .format(str(nome), int(cpf), str(local), int(idade), float(alt)))
