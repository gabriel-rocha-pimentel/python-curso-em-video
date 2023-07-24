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
gordo = list()
magro = list()
maior = menor = count = 0

while True:
      nome = input('\nEscreva seu Nome : ')
      peso = float(input('Escreva seu Peso : '))

      dados.append(nome)
      dados.append(peso)
      pessoas.append(dados[:])
      dados.clear()

      if count == 0:
            maior = menor = pessoas[count][1]
      else:
            if pessoas[count][1] > maior:
                  maior = pessoas[count][1]

            if pessoas[count][1] < menor:
                  menor = pessoas[count][1]

      count += 1
      sair = input('Você quer continuar ? [SIM | NÃO]\n>>> ').strip().upper()[0]
      if sair == 'N':
            break

for p in pessoas:
      if p[1] == maior:
            gordo.append(p[0])
      elif p[1] == menor:
            magro.append(p[0])

print(f'\nAo todo, você cadastrou {count} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de {gordo}')
print(f'O menor peso foi de {menor:.2f}Kg. Peso de {magro}.')
