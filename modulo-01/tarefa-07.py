"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

--> O nome com todas as letras maiúsculas.
--> O nome com todas minúsculas.
--> Quantas letras ao todo (sem considerar espaços).
--> Quantas letras tem o primeiro nome.
"""

nome = input('Olá! Meu nome é python, qual é o seu ? ').strip()
print('\n Prazer em te conhecer {}, vou mostrar algumas curiosidades sobre seu nome abaixo.'.format(nome))

num_nome = nome.split()

print('O seu nome em LETRAS MAIUSCULAS é assim : {}. \n'
      'O seu nome em letras minusculas é assim : {}. \n'
      'O número de letras do seu nome é {}. \n'
      'O seu primeiro nome tem {} letras.'
      .format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), len(num_nome[0])))
