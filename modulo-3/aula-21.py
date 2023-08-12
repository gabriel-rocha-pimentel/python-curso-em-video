"""
Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa via ler o nome
do jogador e quantas partidas ele jogo. Depois vai ler
a quantidade de gols feitos e cada partida.
No final, tudo isso será guardado em um dicionario
incluindo o total de gols feitos durante o campeonato.
"""
print('_' * 50)
print(f'{"+++++ Dicionario em Python +++++":^50}')
print('_' * 50)

total = 0
list_gols = list()
jogadores = {'jogador': '', 'gols': list_gols}

jogadores.update({'jogador': str(input("Nome do Jogador: "))})
partidas = int(input(f'Quantas partidas {jogadores["jogador"]} jogou? '))

for count, gols in enumerate(range(partidas)):
      list_gols.append(int(input(f'Quantos gols na partida {count}?\n>>> ')))
      jogadores.update({'gols': list_gols[:]})

for n in jogadores["gols"]:
      total += n

jogadores.update({"total": total})
print('-=' * 50)

print(jogadores)

print('-=' * 50)

for c, v in jogadores.items():
      print(f'O campo {c} tem o valor {v}')

print('-=' * 50)

print(f'O jogador {jogadores["jogador"]} jogou {partidas} partidas.')

for pos, value in enumerate(jogadores["gols"]):
      print(f'{f"=> Na partida {pos}, fez {value} gols.":^50}')

print(f'Foi um total de {total} gols')
