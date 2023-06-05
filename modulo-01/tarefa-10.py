"""
Crie um programa que leia o nome de uma pessoa
e diga se ela tem 'Silva' no nome.
"""

nome = input('Qual é o seu nome ? ').lower().strip()

print('Seu nome tem o nome Silva : {}'.format('silva' in nome))
