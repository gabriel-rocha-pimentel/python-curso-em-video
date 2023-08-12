"""
Aprimore um dos desafios anteriores para que ele
fucione com vários jogadores, incluindo
um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""
print('_' * 50)
print(f'{"+++++ APRIMORANDO DICIONARIOS +++++":^50}')
print('_' * 50)
time = list()
count_gols = list()
jogadores = dict()
while True:
      jogadores.update({'nome': input('Nome do Jogador: ')})
      jogadores.update({'partidas': int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))})
      for count in range(1, jogadores['partidas'] + 1):
            count_gols.append(int(input(f'\tQuantos gols na partida {count}? ')))
      jogadores.update({'gols': count_gols[:]})
      count_gols.clear()
      time.append(jogadores.copy())

      stop = input('Quer continuar ? [SIM ou NÃO]\n>>> ').strip()[0]
      if stop in 'Nn':
            break
print('-=' * 45)
print(f"{'COD NOME':<15}{'GOLS':<15}{'TOTAL':<15}")
print('-' * 45)
for pos, jogadores in enumerate(time):
      nome_jogador = jogadores["nome"]
      num_gols = jogadores["gols"]
      total_gols = sum(num_gols)

      print(f'{f"{pos} {nome_jogador}":<15}', end='')
      print(f'{f"{num_gols}":<15}', end='')
      print(f'{f"{total_gols}":<15}')

while True:
      data = int(input('Mostrar dados de qual jogador ? (999 para parar)\n>>> '))
      if data == 999:
            break
      elif data >= len(time):
            print(f'ERROR! Não existe jogador com o código {data}!')
      else:
            jogador = time[data]
            print(f'LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
            count = 1
            for gol in jogador["gols"]:
                  print(f'No jogo {count} fez {gol} gols.')
                  count += 1
print('<< VOLTE SEMPRE >>')
