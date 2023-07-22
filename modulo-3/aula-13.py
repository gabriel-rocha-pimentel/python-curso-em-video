"""
Faça um programa que leia nome e peso
de várias pessoas, guardando tudo em uma lista.
No final, mostre:

a - Quantas pessoas foram cadastrados.
b - Uma listagem com as pessoas mais pesadas.
c - Uma listagem com as pessoas mais leves.
"""
print('_' * 50)
print(f'{"+++++ ANALISE DE DADOS +++++":^50}')
print('_' * 50)
pessoas = list()
dados = list()
maior = menor = 0
count = 0

while True:
      nome = input('\nEscreva seu Nome : ')
      peso = int(input('Escreva seu Peso : '))

      dados.append(nome)
      dados.append(peso)
      pessoas.append(dados[:])
      dados.clear()

      count += 1
      sair = input('Você quer continuar ? [SIM | NÃO]\n>>> ').strip().upper()[0]
      if sair == 'N':
            break
print(max(pessoas))
print(f'\nAo todo, você cadastrou {count} pessoas.')
print(f'O maior peso foi de {0:.2f}Kg. Peso de ')
print(f'O menor peso foi de {0:.2f}Kg. Peso de .')