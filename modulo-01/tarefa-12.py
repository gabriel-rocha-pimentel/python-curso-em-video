"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

Exemplo: Ana Maria de Souza
primeiro = Ana
Segundo = Souza
"""
nome = input('Qual é o seu nome ? ').strip()

lista = nome.split()

print('Seu prímeiro nome é {} e seu último nome é {}.'.format(lista[0], lista[len(lista)-1]))
